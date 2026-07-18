# Social Media Sentiment Analysis

## Project Overview
This project analyzes social media data to identify trends, engagement patterns, and user behaviour using ML and NLP. It also includes a deployed REST API for analyzing the sentiment of text in real-time.

## Technologies Used
* python.
* pandas.
* matplotlib.
* numpy.

## Features
* Data collection.
* sentiment analysis.
* trend visualization.
* Engagement analytics.

---

## 🚀 API Documentation

**Base URL:** `https://shrushhh03.pythonanywhere.com`

### 1. Health Check
Checks if the API server is up and running.

* **URL:** `/health`
* **Method:** `GET`
* **Success Response:**
  * **Code:** 200 OK
  * **Content:** 
    ```json
    {
      "status": "Server is running"
    }
    ```

### 2. Predict Sentiment
Analyzes the input text and returns the predicted sentiment.

* **URL:** `/predict`
* **Method:** `POST`
* **Data Params:**
  ```json
  {
    "text": "I am so happy with this new update!"
  }
 Contributors
 - Shrushti Nasre
 - Riddhi pagariya
