# Code review — Abstract `Figura` and concrete shapes (`Exemple_Abstraccio_Figura.ipynb`)

_Review date: 9 de maig de 2026._

## Activity: ABC, abstract methods, and polymorphism

### Assignment

- **Source read:** None found beyond the notebook.
- **Summary (optional):** Declares `Figura` with `@abstractmethod` for perimeter and area; implements `Rectangle` and `Cercle` (`Cercle` uses `math.pi`); builds a heterogeneous list and dispatches polymorphically.

### Acceptance criteria

(Inferred.)

- [x] Uses `ABC` and `@abstractmethod` to forbid direct instantiation of `Figura`.
- [x] Concrete classes implement `calcular_perimetre` and `calcular_area`.
- [x] Demonstrates polymorphic loop over `figures`.
- [ ] **Learner cell:** `figura = Figura("blau")` will raise `TypeError` — correct for ABCs; should be labeled as an expected failure or moved after explaining instantiation rules.

### Analysis

- `Rectangle` / `Cercle` correctly call `super().__init__(color)`.
- **`__str__` on base:** returns Catalan sentence; fine for local course; conflicts with English-only string policy if applied strictly to this repo.
- **Magic numbers:** circle perimeter/area formulas are standard; rectangle uses side names `c1`, `c2` — `width`/`height` would read clearer in English teaching tracks.

### Improvement proposals

1. Add a markdown cell before the illegal instantiation: “Expected `TypeError`: abstract classes cannot be constructed.”
2. Use English identifiers in canonical solutions when aligning with the repository language policy.

### Coded example (Python + comments)

```python
"""Same pattern with English names — keeps ABC teaching goal obvious."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        """Each concrete shape must define how to measure its outline."""

    @abstractmethod
    def area(self):
        """Each concrete shape must define how to measure its surface."""


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2


def main():
    shapes = [Rectangle("blue", 2, 3), Circle("pink", 2)]
    for shape in shapes:
        print(shape.color, shape.perimeter(), shape.area())


if __name__ == "__main__":
    main()
```
