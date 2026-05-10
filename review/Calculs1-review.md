# Code review — Temperature and humidity averages (`Exemples Programació Modular-20260502/Calculs1.py`)

_Review date: 9 de maig de 2026._

## Activity: Script with repeated `try`/`except` on input

### Assignment

- **Source read:** None found; file lives next to modular programming examples dated in folder name.
- **Summary (optional):** Reads morning/afternoon temperature and humidity, defaults invalid entries to `0.0`, prints two averages.

### Acceptance criteria

(Inferred.)

- [x] Reads four numeric inputs with graceful handling of non-numeric text.
- [x] Prints mean temperature and mean humidity.
- [ ] **DRY / structure:** same `try`/`except` block is duplicated four times — `Calculs2.py` in the same folder already improves this.

### Analysis

- Defaulting invalid input to `0.0` silently skews averages — acceptable if the brief demands it, but pedagogically it is often better to re-prompt until valid.
- No `main()` guard; fine for a tiny script, less ideal once imported.

### Improvement proposals

1. Reuse the helper pattern from `Calculs2.py` (`read_float` + `average`) or merge the two files conceptually for students.
2. Consider re-prompting instead of forcing `0.0`, unless the assignment explicitly requires a default.
3. Add `if __name__ == "__main__":` when turning snippets into modules.

### Coded example (Python + comments)

```python
"""Single helper removes repetition and keeps averages trustworthy."""


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again.")


def average(first: float, second: float) -> float:
    return (first + second) / 2


def main() -> None:
    t1 = read_float("Morning temperature: ")
    t2 = read_float("Afternoon temperature: ")
    print("Temperature average:", average(t1, t2))

    h1 = read_float("Morning humidity: ")
    h2 = read_float("Afternoon humidity: ")
    print("Humidity average:", average(h1, h2))


if __name__ == "__main__":
    main()
```
