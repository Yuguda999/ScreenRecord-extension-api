# Screen Record Extension API Documentation

Welcome to the Video Upload API documentation. This API allows you to upload and retrieve videos using a unique identifier.

## Table of Contents

1. [Introduction](#introduction)
2. [Endpoints](#endpoints)
    - [Upload Video](#upload-video)
    - [Get Video](#get-video)
3. [Authentication](#authentication)
4. [HTTP Status Codes](#http-status-codes)
5. [Error Handling](#error-handling)

## Introduction

The Video Upload API provides a simple way to upload and retrieve videos. You can upload a video and receive a unique identifier (video ID) in response. Later, you can use this ID to retrieve the uploaded video.

## Endpoints

### Upload Video

- **Endpoint**: `/upload`
- **Method**: POST
- **Description**: Upload a video file encoded as a Base64 string and receive a unique video ID.
- **Request Body**:
    ```json
    {
        "video_base64": "Base64-encoded video data"
    }
    ```
- **Response**:
    ```json
    {
        "video_id": "unique_video_id"
    }
    ```
- **Example Request**:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"video_base64": "YourBase64DataHere"}' http://yourserver/upload
    ```
- **Example Response**:
    ```json
    {
        "video_id": "a6f1d21e-4dd9-4f4f-afbb-5d9e64c3d8a1"
    }
    ```

### Get Video

- **Endpoint**: `/get_video/<video_id>`
- **Method**: GET
- **Description**: Retrieve the video associated with the given video ID.
- **Response**: Video file (prompting for download)
- **Example Request**:
    ```bash
    curl -OJ http://yourserver/get_video/a6f1d21e-4dd9-4f4f-afbb-5d9e64c3d8a1
    ```
- **Note**: Replace `<video_id>` with the actual video ID received after uploading.

## Authentication

This API does not require authentication for uploading and retrieving videos.

## HTTP Status Codes

- `200 OK`: Request successful.
- `400 Bad Request`: Invalid request or missing data.
- `404 Not Found`: The requested video ID does not exist.
- `500 Internal Server Error`: Server error.

## Error Handling

In case of errors, the API will return a JSON response with an "error" key containing an error message.
