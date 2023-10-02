import requests
import base64
import json
# Define the API endpoint for uploading videos
url = 'http://127.0.0.1:5000/api'  # Replace with your API endpoint
url = 'https://yms.pythonanywhere.com/upload'  # Replace with your API endpoint

# Define the path to the local video file you want to convert to base64
video_file_path = r"ScreenRecordExtensionApi\me.MP4"

# Read the local video file and encode it as base64
with open('laptop.mp4', 'rb') as video_file:
    video_data = video_file.read()
    base64_video = base64.b64encode(video_data).decode()

# Make a POST request to upload the base64 video
payload = {'video_base64': base64_video}
headers = {
    'Content-Type': 'application/json'
}

# Send the POST request
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Print the response from the server
print(response.text)



