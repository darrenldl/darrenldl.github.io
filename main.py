import hashlib
import json
import os
import subprocess

CONTENT_DIR = "content"
OUT_DIR = "docs"
CACHE_PATH = ".markdown-hashes.json"


def load_hashes():
    try:
        with open(CACHE_PATH) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def blake2_hash(path):
    digest = hashlib.blake2b()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main():
    old_hashes = load_hashes()
    new_hashes = {}
    for root, dirs, files in os.walk('content'):
        for file in files:
            file_no_ext, ext = os.path.splitext(file)
            if ext == ".md":
                in_path = os.path.join(root, file)
                out_path = os.path.join(OUT_DIR, root.removeprefix(CONTENT_DIR).removeprefix("/"), f"{file_no_ext}.html")
                content_hash = blake2_hash(in_path)
                new_hashes[in_path] = content_hash
                if old_hashes.get(in_path) == content_hash and os.path.exists(out_path):
                    continue
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                print(f"{in_path}")
                print(f"    -> {out_path}")
                cmd = ["uv",
                       "run",
                       "pandoc",
                       in_path,
                       "--filter",
                       "./filter.py",
                       "--standalone",
                       "--template",
                       "template.html",
                       "-o",
                       out_path
                       ]
                subprocess.run(cmd, check=True)

    with open(CACHE_PATH, "w") as f:
        json.dump(new_hashes, f, indent=2, sort_keys=True)
        f.write("\n")

if __name__ == "__main__":
    main()
