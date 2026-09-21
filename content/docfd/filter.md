## Filter language

The filter language is designed around narrowing the set of documents listed,
but does not impact the fine-grained search results otherwise.

An expression in the filter language is one of:
- `"search_exp"`, `'search_exp'` or `content:search_exp`
    - `search_exp` is the same search expression supported by content search field,
      but only determines whether the document is listed and does not impact the search results listed
- `path-date:"op date"`, e.g. `path-date:>2025-01-01`, `path-date:">= 2025-01-10"`
    - `op` is one of `=`, `>=`, `<=`, `>`, `<`
    - `date` is ISO8601 date, i.e. `yyyy-mm-dd`
- `path-fuzzy:search_exp`, e.g. `path-fuzzy:"meeting notes 2025"`, `path-fuzzy:changelog`
    - `search_exp` is the same search expression supported by content search field
- `path-glob:/**/*.md`
- `ext:txt`
- `expression OR expression` (`OR` is case-insensitive)
- `expression AND expression` (`AND` is case-insensitive)
- `NOT expression` (`NOT` is case-insensitive)
- `(expression)`

All arguments after the colon may be quoted via either single quotation marks (`'`) or double quotation mark (`"`).

Note that the handling of quoted strings is relaxed in one situation to allow for more immediate user feedback of the filtering.
If the expression using a quoted string is in the rightmost position, then the closing quotation mark is optional, e.g.

```
ext:md AND path-fuzzy:"meeting notes
```

is the same as

```
ext:md AND path-fuzzy:"meeting notes"
```

This allows for the results of filtering to be updated in the UI as one types even when the quoted string is, strictly speaking, incomplete.

## Date extraction from document path

Docfd recognizes the following patterns from a document path:
- `yyyy-mm-dd`
    - where`-` is a mandatory separator that is not a digit
- `yyyymmdd`
- `yyyy-mmm-dd`, `dd-mmm-yyyy`
    - where `-` is an optional separator that is neither a digit nor a letter
    - and `mmm` is an abbreviated month name (case-insensitive), e.g. `jan`, `Mar`, `SEP`
- `yyyy-mmmm-dd`, `dd-mmmm-yyyy`
    - where `-` is an optional separator that is neither a digit nor a letter
    - and `mmmm` is a full month name (case-insensitive), e.g. `january`, `March`, `SEPTEMBER`

which recognises the rightmost sequence of `yyyy` `mm` `dd` separated by any non-digit character.

Examples:

| Document path | Date extracted from path |
| --- | --- |
| `/home/user/2025-01-16.md` | `2025-01-16` |
| `/home/user/2025 Jan 16.md` | `2025-01-16` |
| `/home/user/16 Jan 2025.md` | `2025-01-16` |
| `/home/user/2025/01/02/test.txt` | `2025-01-02` |
| `/home/user/2025/01/02/2025-04-10.txt` | `2025-04-10` |
