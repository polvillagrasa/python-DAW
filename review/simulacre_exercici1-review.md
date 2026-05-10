# Code review — Package weights and statistics (`simulacre_exercici1.py`)

_Review date: 9 de maig de 2026._

## Activity: Multi-function “exam style” script

### Assignment

- **Source read:** None found; filename suggests a mock exam exercise.
- **Summary (optional):** Reads list size and weights, reports min/max/mean/count above mean, position of max, incidents over a threshold, duplicates and their positions.

### Acceptance criteria

(Inferred from `main()` flow — cannot verify without the original PDF/brief.)

- [ ] **Runnable correctness:** duplicate definition of `trobar_incidencies` — the first version (broken loop using undefined `n` and wrong bounds) is overwritten by the second, but the dead code is confusing and was likely a merge error.
- [ ] **Data model consistency:** `crear_llista` reads `int` values yet compares against `0.5` and `40.0` and prints “enter … between 0.5 and 40.0” — integers cannot satisfy `0.5 < value` in the way a float exercise would; likely should use `float(input(...))` or integer bounds.
- [x] **Intent visible:** functions for min, max, mean, above-average count, first max index, threshold positions, duplicates — structure matches a typical marks scheme.
- [ ] **Output quality:** `print(f"... {paquets_sobre_mitjana}paquets...")` missing a space before `paquets`.
- [ ] **Exception handling:** bare `except:` swallows `KeyboardInterrupt` and hides real errors — use `except ValueError:`.

### Analysis

- **Critical:** the stray first `trobar_incidencies` (lines using `while n < 5 or n > 40`) should be deleted; it references `n` before assignment and contradicts the later correct `trobar_incidencies(llindar, pesos)`.
- **`trobar_duplicats`:** appends a value once per pair `(i, j)`; duplicate values appearing three times can yield repeated entries in `duplicats` — may or may not match the marking scheme.
- **`trobar_posicio_maxim`:** returns first index only; OK if the brief asks for one position.
- **Indentation:** file mixes tabs — PEP 8 prefers four spaces for interoperability.

### Improvement proposals

1. Remove the erroneous first `trobar_incidencies` definition entirely; keep a single function with a clear name like `positions_above_threshold`.
2. Align numeric type and bounds (`float` vs `int`, inclusive/exclusive limits) with the exam wording.
3. Replace bare `except` with `except ValueError` and re-prompt with a clear message.
4. Fix the missing space in the print for readability.
5. Rename functions to English if following repository clean-code language rules.

### Coded example (Python + comments)

```python
"""Pattern: one validated read helper + clear bounds — avoids bare except."""


def read_int_in_range(prompt: str, low: int, high: int) -> int:
    """Loop until the user supplies an int within [low, high]."""
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
        except ValueError:
            pass
        print(f"Enter an integer between {low} and {high}.")


def positions_above_threshold(values: list[float], threshold: float) -> list[int]:
    """Return 0-based indices strictly above the threshold."""
    return [index for index, value in enumerate(values) if value > threshold]


def main() -> None:
    count = read_int_in_range("How many weights (10-25)? ", 10, 25)
    weights: list[float] = []
    for _ in range(count):
        weights.append(float(input("Weight: ")))
    threshold = read_int_in_range("Threshold (5-40)? ", 5, 40)
    print("Incidents:", positions_above_threshold(weights, float(threshold)))


if __name__ == "__main__":
    main()
```
