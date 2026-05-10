# Code review — Refactored averages (`Exemples Programació Modular-20260502/Calculs2.py`)

_Review date: 9 de maig de 2026._

## Activity: Functions for float input and mean

### Assignment

- **Source read:** None found.
- **Summary (optional):** Same behaviour as `Calculs1.py` with `demanar_float` and `mitjana` to avoid copy-paste.

### Acceptance criteria

(Inferred.)

- [x] Centralises parsing and default-on-error behaviour.
- [x] Computes both averages using `mitjana`.
- [ ] **Language policy:** identifiers `demanar_float`, `mitjana` are Catalan — fine for a local hand-in; rename if aligning with English-only codebase rules.

### Analysis

- Clear step-up from `Calculs1.py`; students see how duplication maps to functions.
- Still uses silent `0.0` default — same trade-off as the previous file.

### Improvement proposals

1. Return `Optional[float]` and let the caller decide, or loop until valid, depending on the assignment wording.
2. Rename to English if the course adopts professional naming (`read_float`, `mean`).

### Coded example (Python + comments)

```python
"""Optional: return None on bad input so the caller can branch explicitly."""

from typing import Optional


def try_parse_float(text: str) -> Optional[float]:
    try:
        return float(text)
    except ValueError:
        return None


def read_float(prompt: str) -> float:
    while True:
        value = try_parse_float(input(prompt))
        if value is not None:
            return value
        print("Invalid value, try again.")


def mean(first: float, second: float) -> float:
    return (first + second) / 2


def main() -> None:
    print("Temperature average:", mean(read_float("Morning: "), read_float("Afternoon: ")))


if __name__ == "__main__":
    main()
```
