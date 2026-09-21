It matches the common file globbing syntax
- `?` matches any character, e.g. `R?ADME.md` matches `README.md`
- `*` matches any number of characters excluding `/`
- `**` matches any number of characters including `/`
- `[x-y]` matches any character between `x` and `y`, e.g. `[A-R]EADME.md`
  matches `README.md`
- `a` matches character `a`
- `\a` matches character `a`, unless the character is `c` (see below)

Additional markers:
- If `\c` is present at any point, then the glob is treated as case-insensitive,
e.g. `re\cadme.md` matches `README.md`

    - Note that the escape rule is applied first, i.e. `\\c` matches the string `\c`, and is not treated as a marker
