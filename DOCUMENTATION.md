# API Documentation

This document provides an overview and usage guidelines for the API.

## Base URL

The base URL for all API endpoints is `https://yms.pythonanywhere.com/api`.

## Endpoints

### Upload Video

- **URL:** `https://yms.pythonanywhere.com/api`
- **Method:** `POST`
- **Description:** Uploads, compresses, and converts a video blob.
- **Request Body:**
  - `video` (BLOB): The video file to be uploaded.

**Example Request:**

```http
POST http://your-api-domain.com/upload_video
Content-Type: multipart/form-data

(video file as binary data)
```

**Example Response (Success):**

```json
HTTP Status: 200 OK
{
  "message": "Video uploaded, compressed, converted, and saved successfully"
}
```

**Example Response (Error):**

```json
HTTP Status: 500 Internal Server Error
{
  "error": "Description of the error"
}
```

## Error Handling

- The API may return HTTP status codes along with error messages in JSON format.
- Common status codes include:
  - `200 OK`: Successful request.
  - `400 Bad Request`: Invalid request data or missing parameters.
  - `500 Internal Server Error`: Server encountered an issue while processing the request.

## Usage Guidelines

- Make sure to send a POST request with a `video` file in the request body to `/upload_video`.
- The API will handle video compression and conversion.
- Check the response for success or error messages.

## Dependencies

- This API relies on the following dependencies:
  - Flask: Web framework for handling HTTP requests.
  - ffmpeg: Multimedia framework for video manipulation.
  - moviepy: Library for video editing.

## Running the API

To run the API, execute the following command in your terminal:

```bash
python your_api_script.py
```

Ensure that you have the required dependencies installed and configured.

## Support and Contact

For any questions or issues related to this API, please contact [your contact information].

---

This is a basic template for API documentation. You should tailor it to your specific API's features, parameters, and requirements. Additionally, consider adding sections for authentication, rate limiting, and more advanced features as needed.
```

Replace placeholders such as `http://your-api-domain.com`, `your_api_script.py`, and `[your contact information]` with the actual details of your API. You can also expand this documentation to cover more advanced features and usage examples.
