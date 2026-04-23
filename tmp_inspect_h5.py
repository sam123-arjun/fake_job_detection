import h5py
import os

base_dir = r"c:\Users\Sameer\.gemini\antigravity\scratch\fake-job-detection\backend"
model_path = os.path.join(base_dir, "ml", "model.h5")

if os.path.exists(model_path):
    print(f"Checking {model_path}")
    try:
        with h5py.File(model_path, 'r') as f:
            print("Attributes in root:")
            for k in f.attrs.keys():
                print(f" - {k}")
            if 'model_config' in f.attrs:
                config = f.attrs['model_config']
                if isinstance(config, bytes):
                    config = config.decode('utf-8')
                print(f"\nModel Config Snippet: {config[:200]}...")
                if '"batch_shape"' in config:
                    print("\nFOUND 'batch_shape' in config!")
                if '"batch_input_shape"' in config:
                    print("\nFOUND 'batch_input_shape' in config!")
            else:
                print("\n'model_config' NOT found in attributes!")
    except Exception as e:
        print(f"Error reading h5: {e}")
else:
    print(f"File not found: {model_path}")
