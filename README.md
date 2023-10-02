# ScreenRecord-extension-api

The Video Upload API processes Base64-encoded video strings as follows:

1. **Receiving the Base64 String**: When a POST request is made to the `/upload` endpoint of the API, it expects a JSON request with a key named `video_base64`, which should contain the Base64-encoded video data. For example:

   ```json
   {
       "video_base64": "Base64-encoded video data"
   }
   ```

2. **Decoding Base64 Data**: The API decodes the Base64 string into binary video data using the `base64.b64decode()` method provided by Python's `base64` module.

   ```python
   video_binary = base64.b64decode(base64_string)
   ```

   This step transforms the Base64-encoded data into its original binary format, representing the video file.

3. **Saving the Video**: The binary video data is then saved to a temporary directory on the server, allowing the API to work with the video as a file.

4. **Generating a Unique Identifier**: To associate the uploaded video with a unique identifier, the API generates a UUID (Universally Unique Identifier) using Python's `uuid` module. This unique identifier, often referred to as `video_id`, is returned in the API response.

5. **Response**: The API responds to the client with a JSON message containing the generated `video_id`.

   ```json
   {
       "video_id": "unique_video_id"
   }
   ```

   This `video_id` serves as a reference for retrieving the uploaded video later.

6. **Retrieving the Video**: To retrieve the video, a GET request is made to the `/get_video/<video_id>` endpoint, where `<video_id>` is the unique identifier provided earlier. The API looks up the associated file path for the given `video_id`, reads the video data, and responds by sending the video file for download.

This process allows clients to submit videos in Base64 format, have them decoded and saved on the server, and obtain a unique identifier to later retrieve the video. It simplifies video upload and retrieval while ensuring each video is associated with a distinct identifier for easy access.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Upload Videos**: Submit video files as Base64-encoded data and receive a unique video ID.
- **Retrieve Videos**: Get videos by providing the associated video ID.
- **Simple and Lightweight**: Easy-to-use API for video management.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- Flask (Python web framework)
- Required libraries (e.g., `base64`, `os`, `uuid`)

## Getting Started

1. Clone this repository to your server or development environment:

   ```bash
   git clone https://github.com/yourusername/video-upload-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd video-upload-api
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:

   ```bash
   python app.py
   ```

   The server will run on `http://localhost:5000` by default.

## API Documentation

For detailed API usage instructions and documentation, please refer to the [API Documentation](API_DOCUMENTATION.md).

## Usage

1. Make a POST request to upload a video:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"video_base64": "YourBase64DataHere"}' http://yourserver/upload
   ```

2. Receive a unique video ID in response.

3. To retrieve the uploaded video, use the video ID:

   ```bash
   curl -OJ http://yourserver/get_video/<video_id>
   ```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.

## License
