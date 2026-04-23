import h5py
import os
import pickle

# Mock load_model to avoid tensorflow requirement
def mock_load_model(path, compile=True):
    print(f"MOCK: load_model called with {path}, compile={compile}")
    return "MOCK_MODEL"

# Import our patch logic but wrapped to use mock
def test_patch_logic():
    base_dir = r"c:\Users\Sameer\.gemini\antigravity\scratch\fake-job-detection\backend"
    model_path = os.path.join(base_dir, "ml", "model.h5")
    
    print(f"Testing patch on {model_path}")
    
    try:
        if os.path.exists(model_path):
            with h5py.File(model_path, 'a') as f:
                if 'model_config' in f.attrs:
                    config_data = f.attrs['model_config']
                    if isinstance(config_data, bytes):
                        config_str = config_data.decode('utf-8')
                    else:
                        config_str = str(config_data)

                    print(f"DEBUG: Config length: {len(config_str)}")
                    if '"batch_shape"' in config_str:
                        print("DEBUG: Found 'batch_shape', applying patch...")
                        new_config = config_str.replace('"batch_shape"', '"batch_input_shape"')
                        f.attrs['model_config'] = new_config.encode('utf-8')
                        print("SUCCESS: Patch applied.")
                    else:
                        print("DEBUG: 'batch_shape' not found (maybe already patched).")
                else:
                    print("DEBUG: 'model_config' not found in attributes.")
        
        # Test if it can be loaded with the mock
        mock_load_model(model_path, compile=False)
        print("Test sequence finished successfully.")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_patch_logic()
