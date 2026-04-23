# 🤖 Machine Learning Logic: How the AI Detects Scams

This guide explains the internal logic of the **Bi-LSTM** model used in this project.

---

## 1. The Preprocessing Logic (The Filter)
The AI is sensitive. If we give it messy text, it gives messy results.
*   **Cleaning**: We remove numbers, punctuation, and "Stopwords" (common words like 'the', 'is', 'at' that don't help detect fraud).
*   **Lowercasing**: To the AI, "JOB" and "job" are different. We lowercase everything to ensure the AI treats them as the same concept.

---

## 2. Tokenization & Sequencing (Words to Numbers)
Computers only understand math.
*   **The Tokenizer**: We use a pre-trained `tokenizer.pickle`. It contains a dictionary where every word has an ID (e.g., "Urgent" = 5, "Money" = 12).
*   **Sequencing**: We turn a sentence into a list of these IDs. 
    *   "Urgent money needed" -> `[5, 12, 8]`
*   **Padding**: The AI model expects every input to be the exact same length (e.g., 500 words). If a job post is only 50 words, we add 450 "zeros" to the end. This is called **Padding**.

---

## 3. The Bi-LSTM Architecture (The Brain)
We use a **Bidirectional Long Short-Term Memory (Bi-LSTM)** network.
*   **What is LSTM?**: It's a "Memory" network. It remembers important words from earlier in the text (like "No Experience Required") and connects them to later words (like "$5000/week").
*   **Why Bidirectional?**: It reads the text in two directions:
    1.  **Forward**: Understands the flow of the sentence.
    2.  **Backward**: Understands the context of a word based on what comes *after* it.
    *   **Logic**: Fake jobs often have "Normal" starts but "Suspicious" ends. Reading both ways catches these inconsistencies.

---

## 4. Inference Logic (The Verdict)
When we run `model.predict(data)`, we get a single number (a float).
*   **Sigmoid Activation**: Our model's last layer uses "Sigmoid," which squashes any value into a range between `0.0` and `1.0`.
*   **The Logic**: 
    *   Value near `1.0` -> High probability of being **Fake**.
    *   Value near `0.0` -> High probability of being **Real**.
*   **Confidence Calculation**:
    *   If result is `0.98`, we are **98% Confident** it is Fake.
    *   If result is `0.52`, we are only **52% Confident** (Low Confidence).

---

## 5. Model Persistence Logic
*   **Loading**: In `ml_service.py`, we use `load_model('model.h5')`.
*   **Global Variable**: We store the loaded model in a global variable.
*   **Reasoning**: Loading a 30MB neural network takes time (disk I/O). By keeping it in the server's RAM, we can process a job post in **milliseconds** instead of seconds.

---
*Developed by Antigravity AI - ML Engineering Mode*
