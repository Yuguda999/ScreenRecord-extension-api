import requests

# Define the URL of your Flask API endpoint
api_url = 'http://localhost:5000/api'  # Update with your actual API URL

# Create a sample video file to upload
video_file_path = 'sample_video.mp4'  # Update with the path to your video file

# Create a dictionary with the file data
files = {'video': ('sample_video.mp4', open(video_file_path, 'rb'))}

try:
    # Send a POST request to upload the video file
    response = requests.post(api_url, files=files)

    # Check the response from the server
    if response.status_code == 200:
        print("Video uploaded and processed successfully.")
    else:
        print("Error:", response.status_code)
        print(response.json())  # Print the error message from the server, if available

except Exception as e:
    print("An error occurred:", str(e))
