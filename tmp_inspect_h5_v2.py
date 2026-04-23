import h5py
import os
import json

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
                
                print("\nSearching for 'batch' in config...")
                search_term = "batch"
                idx = config.find(search_term)
                while idx != -1:
                    print(f"Found '{search_term}' at {idx}: {config[idx:idx+30]}...")
                    idx = config.find(search_term, idx + 1)
                
                # Try to parse as JSON to see if it's valid
                try:
                    data = json.loads(config)
                    print("\nSuccessfully parsed model_config as JSON")
                except Exception as je:
                    print(f"\nFailed to parse model_config as JSON: {je}")
            else:
                # Check for other places where config might be
                print("\n'model_config' not found. Checking if it's in a different attribute or group...")
                for key in f.keys():
                    print(f"Group/Dataset: {key}")
    except Exception as e:
        print(f"Error reading h5: {e}")
else:
    print(f"File not found: {model_path}")
