- First set of files is collected based on:
    - Extensions from `--exts`, `--add-exts`, `--single-line-exts`, `--single-line-add-exts`
        - `--exts` defaults to `txt,md,pdf,epub,odt,docx,fb2,ipynb,html,htm`
        - `--single-line-exts` defaults to `log,csv,tsv`
        - `--add-exts` and `--single-line-add-exts` both default to empty
          strings
    - `PATH`s provided as command line arguments, e.g. `dir0`, `dir1`, `file0`
      in `docfd dir0 dir1 file0`
        - `PATH`s default to `.` only when none of `--paths-from`, `--glob`,
          `--single-line-glob` are specified
    - Paths specified in `FILE` from `--paths-from FILE`

- Second set of files is collected based on `--single-line-glob`

- Third set of files is collected based on `--glob`

- Directories captured by globs are not recursively scanned, i.e.
  files must be directly picked up by glob to be considered for
  second and third set of files

- Files are categorized for single line search mode and default search mode
    - Default search mode is multiline search mode, unless `--single-line` is used

- A file falls into the single line search mode category if it satisfies any of
  the following:
    - File is in `PATH`s or in `FILE` from `--paths-from FILE` and the
      extension falls into `--single-line-exts` or `--single-line-add-exts`
    - File is captured by `--single-line-glob`
    - File is captured by `--glob`, and the extension falls into
      `--single-line-exts` or `--single-line-add-exts`
- Otherwise, the file falls into the default search mode category