from flask import Flask, request, jsonify
import io
import ffmpeg
from moviepy.editor import VideoFileClip

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def upload_video():
   
    video_file = request.files['video']

    try:
        # Read the video blob into memory
        video_blob = io.BytesIO(video_file.read())

        # Compress the video blob
        compressed_video_blob = ffmpeg.input('pipe:0').output('pipe:1', vf='scale=640:360').run(input=video_blob, capture_stdout=True, capture_stderr=True, overwrite_output=True)

        # Convert the compressed video blob to the original video format
        original_video = VideoFileClip(io.BytesIO(compressed_video_blob))

        # Save the original video to disk
        original_filename = 'original_video.mp4'
        original_video.write_videofile(original_filename)

        # Close video objects
        original_video.close()

        return jsonify({'message': 'Video saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
