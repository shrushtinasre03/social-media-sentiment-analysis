# AI Client-Server Architecture

## Project
Social Media Sentiment Analysis

## Objective
The project analyzes social media text and predicts the sentiment (Positive, Negative, or Neutral) using a machine learning model.

## Architecture Components

### 1. Client Layer
- User interacts with the web application.
- Enters social media text for analysis.
- Sends request to the server.

### 2. Server Layer
- Built using Python Flask.
- Receives the user request.
- Passes the text to the sentiment analysis model.
- Sends the prediction back to the client.

### 3. AI Model Layer
- Processes the input text.
- Performs sentiment analysis.
- Returns the predicted sentiment.

### 4. Dataset Layer
- Stores the social media dataset.
- Used for training and testing the model.
- Dataset source: Kaggle (Social Media Usage Dataset).

## Workflow

User → Frontend → Flask Server → AI Model → Dataset → Result → User
