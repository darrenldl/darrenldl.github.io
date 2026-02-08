import os
import subprocess

CONTENT_DIR = "content"
OUT_DIR = "site"

def main():
    for root, dirs, files in os.walk('content'):
        for file in files:
            file_no_ext, ext = os.path.splitext(file)
            if ext == ".md":
                in_path = os.path.join(root, file)
                out_path = os.path.join(OUT_DIR, root.removeprefix(CONTENT_DIR).removeprefix("/"), f"{file_no_ext}.html")
                print(f"{in_path}")
                print(f"    -> {out_path}")
                cmd = ["uv",
                       "run",
                       "pandoc",
                       in_path,
                       "--filter",
                       "./filter.py",
                       "--standalone",
                       "-o",
                       out_path
                       ]
                subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
