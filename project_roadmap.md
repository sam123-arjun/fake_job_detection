# 🛡️ Full-Stack Project Roadmap: Fake Job Detection System

This guide provides a step-by-step walkthrough of building and deploying a modern AI-powered web application.

---

## 1. Project Understanding
### What the project is
The **Fake Job Detection System** is a full-stack web application that uses Machine Learning (Bi-LSTM neural networks) to analyze job descriptions and determine if they are legitimate or fraudulent.

### Real-world use cases
*   **Job Portals**: Integrating an automated flagger for suspicious listings.
*   **Job Seekers**: A tool to verify a suspicious job offer before sharing personal information.
*   **Recruitment Agencies**: Cleaning up large datasets of scrapped job postings.

### Features of the system
1.  **AI Analysis**: Paste a job description to get a "Real" or "Fake" prediction.
2.  **User Authentication**: Secure sign-up and login to save your history.
3.  **Dashboard**: View a history of all previous checks with confidence scores.
4.  **Responsive Design**: A premium "Glassmorphism" UI that works on mobile and desktop.

---

## 2. System Design
### Architecture
`User Browser (React)` <--> `REST API (FastAPI)` <--> `Database (MongoDB)`
                                     |
                          `ML Model (TensorFlow)`

### Folder Structure
```text
fake-job-detection/
├── backend/            # FastAPI Source Code
│   ├── app/            # Main application logic
│   ├── ml/             # Saved .h5 model and tokenizer
│   └── requirements.txt
├── frontend/           # React Source Code
│   ├── src/
│   └── package.json
└── docker-compose.yml  # Orchestration
```

---

## 3. Setup Phase
### Tools Required
*   **Node.js & NPM**: For frontend.
*   **Python 3.10+**: For backend.
*   **Docker**: To run MongoDB easily.

### Installation
1.  **Clone the project**: `git clone <repo-url>`
2.  **Backend**: `cd backend && pip install -r requirements.txt`
3.  **Frontend**: `cd frontend && npm install`

---

## 4. Frontend Development
We use **React (Vite)** for speed and **TailwindCSS** for styling.
*   **AuthContext**: Manages user login state.
*   **Axios**: Connects the frontend to the backend API.

---

## 5. Backend Development
Built with **FastAPI**.
*   **Security**: Uses JWT tokens for secure logins.
*   **ML Service**: Loads the model once at startup for maximum speed.

---

## 6. Database Integration
We use **MongoDB** with the **Beanie ODM**.
*   **Users Collection**: Stores emails and hashed passwords.
*   **Predictions Collection**: Stores job descriptions and AI results.

---

## 7. Testing Phase
*   **Swagger**: Visit `http://localhost:8000/docs` to test APIs directly in the browser.
*   **Postman**: Used for testing the full user flow (Register -> Login -> Predict).

---

## 8. Deployment Phase
*   **Frontend**: Vercel.
*   **Backend**: Render.
*   **Database**: MongoDB Atlas.
*   **Env Variables**: Ensure `MONGODB_URL` and `SECRET_KEY` are set.

---

## 9. Bonus Section
*   **Optimization**: Use a smaller AI model (Quantization) for faster mobile loading.
*   **Mistake to avoid**: Never store passwords in plain text—always use `bcrypt` (which we do!).

---
*Created for your learning journey.*
