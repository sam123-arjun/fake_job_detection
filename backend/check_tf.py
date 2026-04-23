import sys
try:
    print("DEBUG: Importing tensorflow...")
    import tensorflow as tf
    print(f"SUCCESS: TensorFlow version: {tf.__version__}")
    print("DEBUG: Importing load_model...")
    from tensorflow.keras.models import load_model
    print("SUCCESS: load_model imported.")
except Exception as e:
    print(f"FAILED: Error during import: {e}")
    sys.exit(1)
