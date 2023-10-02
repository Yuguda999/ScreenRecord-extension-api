from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def upload_video():
    try:
        data = request.json  # Assuming you are sending the Base64 string as JSON
        base64_string = data['video_base64']  # Assuming the JSON key is 'video_base64'

        # Decode the Base64 string to binary data
        video_binary = base64.b64decode(base64_string)

        # Define the path to save the video locally
        save_path = 'saved_videos/'

        # Ensure the directory exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Generate a unique filename (you can customize this)
        filename = 'video.mp4'  # You may want to change the file extension based on the actual video format

        # Save the video to the specified path
        with open(os.path.join(save_path, filename), 'wb') as file:
            file.write(video_binary)

        return jsonify({'message': 'Video saved successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
if __name__ == '__main__':
    app.run(debug=True)