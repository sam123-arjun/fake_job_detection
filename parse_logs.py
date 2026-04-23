import sys

try:
    with open('backend_logs.txt', 'r', encoding='utf-16le', errors='replace') as f:
        lines = f.readlines()
        
    with open('parsed_errors.txt', 'w', encoding='utf-8') as out:
        for i, line in enumerate(lines):
            l_lower = line.lower()
            if 'error' in l_lower or 'exception' in l_lower or 'traceback' in l_lower or '500 ' in l_lower or '422 ' in l_lower or 'critical' in l_lower:
                out.write(f"Line {i}: {line.strip()}\n")
except Exception as e:
    print(f"Failed to read file: {e}")
