from flask import Flask, request, jsonify, send_file
import base64
import os
import uuid

app = Flask(__name__)

# Dictionary to store video data
video_data = {}

@app.route('/upload', methods=['POST'])
def upload_video():
    try:
        data = request.json 
        base64_string = data['video_base64'] 

        # Decode the Base64 string to binary data
        video_binary = base64.b64decode(base64_string)

        # Generate a unique ID for the video
        video_id = str(uuid.uuid4())

        # Specify a directory to temporarily save the video
        save_path = 'temp_videos/'

        # Ensure the directory exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Generate a unique filename based on the video ID
        filename = f'screenrecord-{video_id}.mp4'

        # Save the video to the temporary path
        with open(os.path.join(save_path, filename), 'wb') as file:
            file.write(video_binary)

        # Store the video ID and file path in the dictionary
        video_data[video_id] = os.path.join(save_path, filename)

        # Return the video ID as a response
        return jsonify({'video_id': video_id})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_video/<video_id>', methods=['GET'])
def get_video(video_id):
    try:
        # Retrieve the file path associated with the video ID
        video_path = video_data.get(video_id)

        if video_path:
            # Send the video file as a download response
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
