import os
import sys
from unittest.mock import MagicMock

# Add the backend path to sys.path
base_dir = r"c:\Users\Sameer\.gemini\antigravity\scratch\fake-job-detection\backend"
sys.path.append(base_dir)

# Mocking settings and app things
os.environ["PROJECT_NAME"] = "FakeJobDetection"
os.environ["API_V1_STR"] = "/api/v1"

# Mock tensorflow before importing ml_service if it's not available
try:
    import tensorflow
except ImportError:
    print("TensorFlow not found, mocking for logic testing...")
    mock_tf = MagicMock()
    sys.modules["tensorflow"] = mock_tf
    sys.modules["tensorflow.keras"] = mock_tf
    sys.modules["tensorflow.keras.models"] = mock_tf
    sys.modules["tensorflow.keras.preprocessing"] = mock_tf
    sys.modules["tensorflow.keras.preprocessing.sequence"] = mock_tf

try:
    from app.services import ml_service
    print("Successfully imported ml_service")
    
    # Run the model loading (should fail or log error but not crash)
    print("Calling load_ml_model()...")
    ml_service.load_ml_model()
    
    # Test a prediction call (should use heuristic)
    print("\nTesting Heuristic Fallback...")
    res, score, conf, reasons = ml_service.predict_job_post(
        "We are offering a simple copy-paste typing job. You can earn ₹5,000 per day without any experience. Work from mobile or laptop. Hurry up and apply fast. Payment guaranteed.",
        "Data Entry Operator",
        "No experience required"
    )
    print(f"Prediction Result: {res}")
    print(f"Confidence: {score:.4f} ({conf})")
    print(f"Reasons: {reasons}")
    
    if "Note: Neural Engine is currently syncing" in str(reasons):
        print("\nPASS: Heuristic fallback is working correctly.")
    else:
        print("\nFAIL: Heuristic fallback message missing.")

    # Test a 'Real' job
    print("\nTesting Real Job Detection...")
    res, score, conf, reasons = ml_service.predict_job_post(
        "Senior Software Engineer role at Google. Requires 5 years of experience in Java and React. Competitive salary and health insurance.",
        "Senior Software Engineer",
        "Bachelor's degree in CS, 5+ years experience"
    )
    print(f"Prediction Result: {res}")
    print(f"Confidence: {score:.4f} ({conf})")
    print(f"Reasons: {reasons}")

except Exception as e:
    print(f"UNEXPECTED ERROR in verification script: {e}")
    import traceback
    traceback.print_exc()
