import hashlib
import os


def hash_large_file(file_path = "temp_large_file.bin", chunk_size=4096):
    # Create a dummy file
    if not os.path.exists(file_path):
        with open(file_path, "wb") as f:
            f.write(os.urandom(1024 * 1024))
        print(f"Created dummy file: {file_path}")

    # Hash dummy file
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hasher.update(chunk)
        file_hash = hasher.hexdigest()
        print(f"Hash of {file_path} (chunked): {file_hash}")

    # Remove dummy file
    if os.path.exists(file_path):
        os.remove(file_path)


hash_large_file()