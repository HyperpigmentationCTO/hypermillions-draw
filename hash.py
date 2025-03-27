import hashlib
import sys
import argparse

def calculate_file_hash(filepath):
    with open(filepath, 'rb') as f:
        filehash = hashlib.sha256(f.read()).hexdigest()
        return filehash

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate SHA256 hash of a file')
    parser.add_argument('filepath', help='Path to the file to hash')

    args = parser.parse_args()

    try:
        hash_value = calculate_file_hash(args.filepath)
        print(hash_value)
    except FileNotFoundError:
        print(f"Error: File '{args.filepath}' not found")
        sys.exit(1)
