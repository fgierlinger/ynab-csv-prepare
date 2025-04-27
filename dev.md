# Ideas

## Refactor as python module

* Installation with `pipx install -e .`
* ynab-csv-prepare.py needs to be moved in a module with the same name.

## Payee Glob Match

Now i'd like to have a pattern definition file as json, that maps a defined value to multiple globs. If the glob matches a string, the defined value should be used instead of the string.

Show me the code and the json to do this.

Alright, that's a cool idea — you basically want a JSON file where you define categories (or "mapped values") with a list of glob patterns, and when a string matches a glob, you replace the string with the mapped value.

```python
import json
import fnmatch

# Load pattern definitions from JSON
with open('pattern_definitions.json', 'r') as f:
    pattern_definitions = json.load(f)

def map_string(input_string, pattern_definitions):
    for mapped_value, patterns in pattern_definitions.items():
        for pattern in patterns:
            if fnmatch.fnmatch(input_string, pattern):
                return mapped_value
    return input_string  # No match, return the original string

# Example strings to test
strings = [
    "picture.jpg",
    "document.pdf",
    "script.py",
    "archive.tar.gz",
    "unknownfile.xyz"
]

# Map each string
for s in strings:
    mapped = map_string(s, pattern_definitions)
    print(f"{s} => {mapped}")
```
