from flask import Flask, request, jsonify, send_file
import base64
import os
import uuid
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import speech_recognition as sr

app = Flask(__name__)
video_data = {}

@app.route('/upload', methods=['POST'])
def upload_video():
    try:
        data = request.json
        base64_string = data['video_base64']

        # Decode the Base64 string to binary data
        video_binary = base64.b64decode(base64_string)
        video_id = str(uuid.uuid4())

        # Specify a directory to temporarily save the video
        save_path = 'temp_videos/'

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        filename = f'{video_id}.mp4'
        video_path = os.path.join(save_path, filename)

        # Save the video to the temporary path
        with open(video_path, 'wb') as file:
            file.write(video_binary)

        # Store the video ID and file path in the dictionary
        video_data[video_id] = video_path

        # Transcribe the video (optional)
        transcribe_video(video_path, video_id)

        return jsonify({'video_id': video_id})

    except Exception as e:
        return jsonify({'error': str(e)})

def transcribe_video(video_path, video_id):
    try:
        # Extract audio from the video
        audio_path = os.path.join('temp_audios', f'{video_id}.wav')
        ffmpeg_extract_audio(video_path, audio_path)

        # Initialize the speech recognition recognizer
        recognizer = sr.Recognizer()

        # Transcribe the audio
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)

        # Perform speech recognition
        text = recognizer.recognize_google(audio)  # You can choose a different recognizer or language here

        # Generate an SRT file with the transcription
        srt_path = os.path.join('transcriptions', f'{video_id}.srt')
        with open(srt_path, 'w') as srt_file:
            srt_file.write("1\n")
            srt_file.write("00:00:00,000 --> 00:00:10,000\n")
            srt_file.write(text)

        # Clean up temporary files (optional)
        os.remove(audio_path)

    except Exception as e:
        print(f"Error transcribing video {video_id}: {str(e)}")

@app.route('/get_video/<video_id>', methods=['GET'])
def get_video(video_id):
    try:
        video_path = video_data.get(video_id)

        if video_path:
            return send_file(
                video_path,
                as_attachment=True,
                download_name='video.mp4',
                mimetype='video/mp4'
            )
        else:
            return jsonify({'error': 'Video not found'})

    except Exception as e:
        return jsonify({'error': str(e)})
