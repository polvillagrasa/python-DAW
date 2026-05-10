# Code review — Login plus placeholder program (`Exemples Programació Modular-20260502/Script3.py`)

_Review date: 9 de maig de 2026._

## Activity: Import-based composition

### Assignment

- **Source read:** None found.
- **Summary (optional):** Reuses `Script2` helpers, prints slightly different messages, calls empty `programa_principal` after success.

### Acceptance criteria

(Inferred.)

- [x] Imports shared functions instead of duplicating them.
- [x] Uses `__main__` guard.
- [ ] **Completeness:** `programa_principal` is `pass` — fine as a stub if the next exercise fills it; otherwise mark as TODO for students.
- [ ] **Import coupling:** depends on module name `Script2` (no package); fragile if files are renamed.

### Analysis

- Good illustration of “one module owns the helpers, another owns a different workflow”.
- Success path prints the username with comma formatting — minor style difference vs `Script2` f-string; both OK. (Student `Script3.py` uses Catalan strings; the sketch below uses en-US user-facing copy.)

### Improvement proposals

1. Replace `pass` with a one-line placeholder such as logging `"TODO: main program"` so success path shows visible progress.
2. When the course introduces packages, move shared code to a neutral module name (`login.py`).

### Coded example (Python + comments)

```python
"""Sketch: imported auth + explicit next step hook."""

from Script2 import demanar_dades, validar_inici_sessio  # noqa: F401  (demo import)


def run_app() -> None:
    print("(Demo) Real application would start here.")


def main() -> None:
    print("=== Login (Script3) ===")
    user, password = demanar_dades()
    if validar_inici_sessio(user, password):
        print("Access granted! Welcome,", user)
        run_app()
    else:
        print("Access denied. Please try again.")


if __name__ == "__main__":
    main()
```
