# 🛡️ Backend Logic: Fake Job Detection System

This guide explains the internal engineering logic of **this specific project**.

---

## 1. Backend Fundamentals (This Project)
*   **Core Role**: The backend acts as an **AI Middleware**. Its main job is to receive raw text from a user, prepare it for a Machine Learning model, and save the resulting "verdict" safely.
*   **The "Worker"**: We use **FastAPI**. Unlike older systems, it is "Asynchronous," meaning it can handle many users checking jobs at the exact same time without waiting for the AI to finish one before starting the next.

---

## 2. Request–Response Lifecycle (Predict Flow)
1.  **Incoming Request**: The React frontend sends a `POST` to `/api/v1/predict/`.
2.  **Middleware Processing**: The `log_requests` middleware (in `main.py`) captures the start time to monitor how long the AI takes.
3.  **Dependency Injection**: The server runs `get_current_active_user` (in `deps.py`). This checks the user's "Badge" (JWT). If missing, the flow stops immediately.
4.  **Service Execution**: The request hits the `predict_job_post` service.
5.  **Response Delivery**: The server returns a JSON object and the `log_requests` middleware calculates the final processing time.

---

## 3. API Logic: The Predicting Endpoint
*   **Location**: `app/api/v1/endpoints/predict.py`
*   **Logic**: 
    *   It doesn't just run the AI; it first **validates** the input using a Pydantic schema (`PredictionCreate`).
    *   It calls the `ml_service` to get the score.
    *   **Crucial Step**: It creates a `Prediction` document in the database *before* sending the response back to the user, ensuring the user's history is always updated.

---

## 4. Database Logic: Beanie & MongoDB
*   **Connection**: Handled in `app/db/init_db.py`. It uses a "Singleton" pattern, meaning only one database connection is shared across the whole app.
*   **NoSQL Logic**: We store predictions as "Documents." This is faster than SQL for this project because we often save large blocks of job description text.
*   **Data Linking**: We use `Link[User]` in the `Prediction` model. This tells MongoDB: "Store the ID of the user who made this prediction so we can find it later."

---

## 5. Authentication & Security Logic
*   **Password Hashing**: We use `bcrypt` via `Passlib`. When you register, the backend *never* sees your real password; it only sees and stores a "hash."
*   **Token Generation**: We use `python-jose` to create JWTs.
    *   **Logic**: The backend takes your `User ID`, adds an expiration time (30 mins), and signs it with a `SECRET_KEY`. 
    *   **Verification**: Every time you access your Dashboard, the backend verifies the signature. If a hacker tries to change the User ID in the token, the signature won't match, and the backend rejects it.

---

## 6. Backend Architecture: The Service Layer
*   **Separation**: We keep ML logic in `app/services/ml_service.py` and API logic in `endpoints`.
*   **Why?**: If we want to upgrade from a Bi-LSTM model to a Transformer (like GPT), we only have to change one file (`ml_service.py`). The rest of the backend (routes, auth, database) stays exactly the same.

---

## 7. Real Example: "User Predicts a Job"
1.  **Frontend**: User pastes a job and hits "Detect."
2.  **Backend Auth**: `deps.py` extracts the `sub` (User ID) from the JWT in the header.
3.  **ML Processing**: 
    *   `ml_service.py` cleans the text (removes HTML/special characters).
    *   The `tokenizer` converts words to a matrix of numbers.
    *   `model.predict()` runs the matrix through the neural network.
4.  **DB Record**: A new `Prediction` object is saved with the user's ID.
5.  **Response**: Frontend receives `{"prediction_result": "Real", "confidence_score": 0.99}`.

---

## 8. Mental Model: Thinking like the Fake Job Detection Engineer
*   **Latency Awareness**: AI models are slow. We use `async` functions so the server doesn't "freeze" while the GPU/CPU is thinking.
*   **Model Persistence**: We load the 32MB `model.h5` file **once** into RAM at startup. If we loaded it for every request, the app would take 10 seconds to respond instead of 0.5 seconds.
*   **Confidence Levels**: We don't just say "Fake." We calculate a score (0 to 1). Our logic converts this to "LOW," "MEDIUM," or "HIGH" confidence to help the user understand the AI's "feeling."

---
*Developed by Antigravity AI - Project Logic Deep Dive*
