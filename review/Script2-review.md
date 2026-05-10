# Code review — Login script with `__main__` guard (`Exemples Programació Modular-20260502/Script2.py`)

_Review date: 9 de maig de 2026._

## Activity: Reusable login helpers

### Assignment

- **Source read:** None found.
- **Summary (optional):** Same logic as `Script1.py` but wraps execution in `if __name__ == "__main__":`, enabling clean imports.

### Acceptance criteria

(Inferred.)

- [x] Keeps `demanar_dades` / `validar_inici_sessio` / `main` separation.
- [x] Avoids side effects on import — appropriate for `Script3.py` importing from here.
- [ ] **Naming / language:** Catalan identifiers and messages — acceptable for class; adjust for English-only policy if required.

### Analysis

- This file is the correct pattern for small modules that double as runnable scripts.
- `Script3` uses `from Script2 import demanar_dades, validar_inici_sessio` — requires running from the same directory or proper `PYTHONPATH`; normal for early exercises.

### Improvement proposals

1. Optionally move shared auth helpers to `auth_utils.py` once students learn packages.
2. Replace hard-coded credentials with a `dict` or file only if the syllabus moves to “configuration” topics.

### Coded example (Python + comments)

```python
"""Imported helpers stay side-effect free; only __main__ talks to the user."""


def prompt_login() -> tuple[str, str]:
    """Read username and password from stdin."""
    return input("Username: "), input("Password: ")


def main() -> None:
    user, password = prompt_login()
    print("OK" if user == "admin" and password == "1234" else "Denied")


if __name__ == "__main__":
    main()
```
