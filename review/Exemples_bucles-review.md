# Code review — Loop teaching examples (`Exemples_bucles.ipynb`)

_Review date: 9 de maig de 2026._

## Activity: Solved examples (loops and iteration)

### Assignment

- **Source read:** None found — searched repository root; notebook appears to be course material with embedded prompts, not a separate brief.
- **Summary (optional):** Demonstrates `for`/`range`, nested loops, string iteration, `while`, and `zip` patterns typical of an introductory Python module.

### Acceptance criteria

(Inferred from notebook intent; no formal AC document.)

- [x] Illustrates fixed-count `for` loops and `range` variants — cells show counting and greeting patterns.
- [x] Shows nested iteration (friends / purchases) with running totals and extrema.
- [x] Covers `while` with termination conditions (guessing game, letter input).
- [ ] **Robustness / UX:** several cells assume valid `int`/`float` input with no `try`/`except` — acceptable for a first pass, but exercises would need validation for production-style scripts.

### Analysis

- The nested “friends” example correctly tracks max/min spend and averages; dividing by `num_coses` assumes `num_coses > 0` (would raise `ZeroDivisionError` if the user enters `0`).
- **Cell 9 comment bug:** the comment says range `[0-3)` but the code uses `range(1, 4)` (values `1..3`); the comment should match the code to avoid confusing learners.
- **Letter-count `while`:** the first prompt says “`.` to finish” but the inner prompt says “`0` to finish” — inconsistent exit rules; the loop condition only checks for `.`, so the text about `0` is misleading.
- **Quiz cell:** `float(input(...))` is compared to an integer sum; fine for whole-number random draws, but `int(input(...))` would match the problem statement better. The f-string in `input` does not substitute `num`/`num2` (literal text inside quotes).

### Improvement proposals

1. Align user-facing prompts and comments with actual exit conditions (`.` vs `0`).
2. Guard `num_coses` (and similar) before division; show a small validation loop for teaching.
3. Fix misleading comments on `range` bounds.
4. For new or revised teaching code, use **English identifiers and messages** per project clean-code policy (current cells use Catalan strings, which is fine for local class use but should be flagged if the codebase standard is English).

### Coded example (Python + comments)

```python
"""Guarded average: same teaching goal, fewer edge-case surprises."""

def read_positive_int(prompt: str) -> int:
    """Keep asking until the user supplies a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a positive integer.")


def main() -> None:
    total_spent = 0.0
    num_items = read_positive_int("How many items? ")
    for _ in range(num_items):
        total_spent += float(input("Item price: "))
    print("Average:", total_spent / num_items)


if __name__ == "__main__":
    main()
```
