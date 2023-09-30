# Video Processing API Documentation

## Table of Contents

- [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
- [API Endpoints](#api-endpoints)
  - [1. POST /api](#1-post-api)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Conclusion](#conclusion)

## Introduction

The Video Processing API is a Flask-based web service that allows users to upload video blobs, compress them, convert them to a specific resolution, and save them as MP4 files. This documentation provides an overview of the API, its endpoints, and how to use it.

### Prerequisites

Before using the API, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- FFmpeg
- MoviePy

You can install Flask, FFmpeg, and MoviePy using pip:

```bash
pip install Flask moviepy
```

## API Endpoints

### 1. POST https://yms.pythonanywhere.com/api

This endpoint allows users to upload a video blob, which will be processed and saved as an MP4 file.

#### Request

- **Method:** POST
- **Content-Type:** application/octet-stream (Binary data)

#### Request Body

- The request body should contain the video blob as raw binary data.

#### Response

- If successful, the API responds with a JSON message indicating that the video was uploaded, compressed, converted, and saved successfully.
  ```json
  {
    "message": "Video uploaded, compressed, converted, and saved successfully"
  }
  ```
- If there is an error during processing, the API responds with an error message.
  ```json
  {
    "error": "Error details here"
  }
  ```

## Usage

To use the Video Processing API, follow these steps:

1. Start the Flask server by running the provided Python script:

   ```bash
   python your_api_script.py
   ```

2. Send a POST request to the `/api` endpoint with the video blob as the request body.

   Example using Python requests library:

   ```python
   import requests

   video_blob = open('your_video.mp4', 'rb').read()  # Replace 'your_video.mp4' with the actual video file
   response = requests.post('http://localhost:5000/api/upload_video', data=video_blob)

   if response.status_code == 200:
       print("Video processing successful!")
   else:
       print("Error:", response.json()['error'])
   ```

## Error Handling

- If the video blob is not provided or is invalid, the API responds with a 500 Internal Server Error.
- If FFmpeg encounters an error during video processing, the API captures the stderr output and provides a detailed error message in the response.
