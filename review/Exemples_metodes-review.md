# Code review — Functions, scope, and NumPy procedures (`Exemples_metodes.ipynb`)

_Review date: 9 de maig de 2026._

## Activity: Solved examples (definitions, mutability, modular procedures)

### Assignment

- **Source read:** None found — didactic notebook with intentional broken cells followed by fixes.
- **Summary (optional):** Teaches definition order, closure/`global`, parameter passing, in-place list changes vs returned copies, and refactors a matrix script into `demanarValors` / `imprimirTaula` / `invertirTaula`.

### Acceptance criteria

(Inferred.)

- [x] Contrasts failing call-before-define with correct order.
- [x] Shows `UnboundLocalError` vs `global` vs parameter+return patterns.
- [x] Demonstrates mutating a shared list vs returning a new list (`copy`).
- [x] Refactors monolithic NumPy code into reusable functions; shows in-place inversion vs non-mutating inversion variant.
- [ ] **Naming / policy:** function names like `demanarValors` mix Catalan; NumPy example uses `int(n/2)` for row half — for odd `n`, pairing with `round(n/2)` in the refactored version is slightly clearer (both are acceptable for tiny matrices).

### Analysis

- Early cells that fail on purpose are valuable if the instructor narrates why; otherwise learners may think the notebook is “broken”.
- **`invertirTaula` in-place:** swapping across both dimensions mutates the argument; the later cell with `.copy()` correctly separates concerns — good progression.
- **`imprimirTaula`:** border printing uses per-cell `"--"`; readable enough for class; could be deduplicated into one small helper if you want less duplication.
- Duplicate imports (`numpy`, `random`) appear when cells are re-run; harmless.

### Improvement proposals

1. Add a one-line markdown cell before each *intentional* error cell: “Expected failure: …”.
2. Prefer English identifiers in any hand-out meant to align with professional clean-code habits (`read_values`, `print_table`, `invert_table`).
3. Consider `//` for integer half-steps (`n // 2`) when looping swap indices to avoid `float` from `int(n/2)` in Python 3.

### Coded example (Python + comments)

```python
"""Same ideas as the notebook: explicit return instead of global mutation."""


def increment_all(values: list[int]) -> list[int]:
    """Return a new list; callers keep predictability (easier tests)."""
    incremented_values: list[int] = []
    for original_value in values:
        incremented_value = original_value + 1
        incremented_values.append(incremented_value)
    return incremented_values


def main() -> None:
    nums = [0, 1]
    updated = increment_all(nums)
    print(nums)      # unchanged
    print(updated)   # [1, 2]


if __name__ == "__main__":
    main()
```
