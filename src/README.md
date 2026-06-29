# Source Code

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /predict | POST | Predicts the sentiment (Positive, Negative, Neutral) from user input. |
| /history | GET | Returns previous sentiment analysis results. |
| /dataset | GET | Displays information about the dataset used. |
| /health | GET | Checks if the server is running properly. |
| /feedback | POST | Stores user feedback about prediction accuracy. |

## Backend Technology
- Python
- Flask

## Response Format
The server returns responses in JSON format.
## Backend Workflow

1. User enters text in the frontend.
2. Frontend sends the text to the backend using a POST request.
3. Flask receives the request.
4. The sentiment analysis model processes the text.
5. The model predicts Positive, Negative, or Neutral sentiment.
6. Backend returns the prediction in JSON format.
7. Frontend displays the result to the user.
## Frontend Interface

The frontend provides a simple interface for users to interact with the sentiment analysis system.

### Features
- Text input box for entering social media content.
- Analyze button to submit the text.
- Display area showing the predicted sentiment.
- Loading indicator while processing the request.

### Technologies
- HTML
- CSS
- JavaScript
