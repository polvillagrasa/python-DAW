# Code review — List and matrix teaching examples (`Exemples_llistes.ipynb`)

_Review date: 9 de maig de 2026._

## Activity: Solved examples (lists, 2D structures, slicing)

### Assignment

- **Source read:** None found — notebook is self-contained teaching material.
- **Summary (optional):** Walks through list creation, mutation, iteration pitfalls, indexing, shallow views vs copies, and a small “monthly sales” matrix scenario.

### Acceptance criteria

(Inferred.)

- [x] Demonstrates 1D and 2D lists, `append`, `pop`, `insert`, `remove`, `len`, slicing.
- [x] Contrasts mutating a list in-place by index vs failing to mutate via `for value in lst` reassignment (cell intentionally shows unchanged list).
- [x] Explains shallow slice effects vs `.copy()` with a minimal before/after print.
- [x] Introduces helper functions `crear_matriu` / `imprimir_matriu` and uses them with `vendes_mensuals`.
- [ ] **Bounds safety:** grade notebook (`notes[alumne]`) trusts the user index without range check — can `IndexError` or overwrite wrong slot.

### Analysis

- The slice-vs-copy cells are pedagogically strong: they show why `l2 = l[0:2]` aliases the first elements.
- **Grades loop:** `notes = [0]*12` then `notes[alumne] = nota` — if `alumne` is outside `0..11`, the program crashes; negative indices are legal in Python but probably not intended.
- **Sales cells:** converting month/category with `-1` is consistent with 1-based UI; comments in code help trace expected demo values.
- Naming mixes Catalan (`llista`, `fila`) with English (`random`); acceptable for class notes, but conflicts with an English-only identifier policy for shared repos.

### Improvement proposals

1. Clamp or validate `alumne` to `0 <= alumne < len(notes)` before assignment; show an error message otherwise.
2. Replace bare `int(input(...))` with `try`/`except` where the notebook is meant as a runnable script template.
3. If the repository adopts English identifiers, rename helpers to `create_matrix` / `print_matrix` in any *new* canonical solutions (keep Catalan in slides if required by the course).

### Coded example (Python + comments)

```python
"""Safe index write: keeps the teaching idea, avoids silent wrong slots."""

from typing import List


def set_grade(grades: List[float], student_index: int, value: float) -> bool:
    """Return True if stored; False if index is out of range."""
    if 0 <= student_index < len(grades):
        grades[student_index] = value
        return True
    return False


def demo() -> None:
    grades = [0.0] * 12
    student_index = int(input("Student index (0-11, -1 to quit): "))
    while student_index != -1:
        mark = float(input("Grade: "))
        if not set_grade(grades, student_index, mark):
            print("Index out of range.")
        student_index = int(input("Student index (0-11, -1 to quit): "))


if __name__ == "__main__":
    demo()
```
