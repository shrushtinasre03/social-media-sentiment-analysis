# API Documentation

## Base URL

http://localhost:5000

---

## POST /predict

### Description
Predicts the sentiment of the given social media text.

### Request

```json
{
  "text": "I really enjoyed this product!"
}
```

### Response

```json
{
  "sentiment": "Positive"
}
```

---

## GET /history

Returns previously analyzed sentiment results.

---

## GET /dataset

Displays information about the dataset used for analysis.

---

## GET /health

Checks whether the backend server is running.

---

## POST /feedback

Stores user feedback regarding prediction accuracy.
