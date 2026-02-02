import os

def find_corrupted_py_files(root_dir: str):
    corrupted = []

    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "rb") as f:
                    if b"\x00" in f.read():
                        corrupted.append(path)

    return corrupted


if __name__ == "__main__":
    ROOT_DIR = r"/src"
    bad_files = find_corrupted_py_files(ROOT_DIR)

    if bad_files:
        print("Corrupted files found:")
        for f in bad_files:
            print(" -", f)
    else:
        print("No corrupted .py files found.")
