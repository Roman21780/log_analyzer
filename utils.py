import json


def read_logs_from_files(file_paths):
    logs = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    if line.strip():
                        logs.append(json.loads(line))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error processing file {file_path}: {e}")
    return logs