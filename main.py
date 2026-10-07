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


def blake2_hash(*paths):
    digest = hashlib.blake2b()
    for path in paths:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                digest.update(chunk)
    return digest.hexdigest()


def front_matter_flag(path, name):
    with open(path) as f:
        if f.readline().strip() != "---":
            return False
        for line in f:
            if line.strip() in ("---", "..."):
                return False
            key, separator, value = line.partition(":")
            if separator and key.strip() == name:
                return value.strip().lower() == "true"
    return False


def main():
    old_hashes = load_hashes()
    new_hashes = {}
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            file_no_ext, ext = os.path.splitext(file)
            if ext == ".md":
                in_path = os.path.join(root, file)
                out_path = os.path.join(OUT_DIR, root.removeprefix(CONTENT_DIR).removeprefix("/"), f"{file_no_ext}.html")
                content_hash = blake2_hash(
                    in_path,
                    "template.html",
                    "filter.py",
                    __file__,
                )
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
                       ]
                if front_matter_flag(in_path, "toc"):
                    cmd.append("--toc")
                cmd.extend([
                    "--toc-depth=3",
                    "--standalone",
                    "--template",
                    "template.html",
                    "-o",
                    out_path,
                ])
                subprocess.run(cmd, check=True)

    for root, dirs, files in os.walk(OUT_DIR):
        for file in files:
            file_no_ext, ext = os.path.splitext(file)
            if ext == ".html":
                content_path = os.path.join(CONTENT_DIR, root.removeprefix(OUT_DIR).removeprefix("/"), f"{file_no_ext}.md")
                if not os.path.exists(content_path):
                    html_path = os.path.join(root, file)
                    print(f"Removing {html_path}")
                    os.remove(html_path)

    with open(CACHE_PATH, "w") as f:
        json.dump(new_hashes, f, indent=2, sort_keys=True)
        f.write("\n")

if __name__ == "__main__":
    main()
