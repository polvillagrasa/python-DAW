# Code review — `Car` class and interactive demo (`Exemple_Cotxe.ipynb`)

_Review date: 9 de maig de 2026._

## Activity: Classes, encapsulation, and I/O

### Assignment

- **Source read:** None found in repository beyond the notebook itself.
- **Summary (optional):** Defines `Cotxe` with attributes, getters/setters, fuel cost helper, `__str__`, then exercises privacy and builds cars from `input()`.

### Acceptance criteria

(Inferred from typical “classes and objects” learning goals.)

- [x] Models a car with color, doors, seats, convertible flag, consumption, owner.
- [x] Provides `calcular_despesa` from consumption and fuel price.
- [x] Demonstrates `__str__` for readable output.
- [ ] **Encapsulation:** `descapotable` naming collides conceptually with boolean field vs methods (see Analysis); `__propietari` bypass via `cotxe1.__propietari = "Pere"` in a cell shows name mangling is not true security — good demo if explained, confusing if presented as “private”.
- [ ] **Input safety:** `demanar_dades` uses bare `int(input(...))` — crashes on bad input.

### Analysis

- **Method / attribute clash:** the class sets `self.descapotable` in `__init__` and also defines two methods named `descapotable` (getter- and setter-shaped). Because the instance attribute exists, normal reads like `self.descapotable` in `__str__` resolve to the boolean, not the methods — the “getter/setter” pair is effectively dead and confusing for readers.
- **Private owner:** `get_propietari` / `set_propietari` are fine; the notebook line `cotxe1.__propietari="Pere"` creates a *new* mangled attribute on the instance without updating the real private field — `get_propietari()` still returns `"Joan"` until `set_propietari` runs. That is a good teaching moment if labeled explicitly.
- **`demanar_dades`:** missing `consum` in one demo cell (`Cotxe(..., propietari="Joan")` without `consum`) would error at instantiation — likely a copy/paste slip between cells.

### Improvement proposals

1. Rename boolean field to `is_convertible` (or keep Catalan for class-only work) and use `get_is_convertible` / `set_is_convertible` — never reuse the field name as a method name.
2. Wrap numeric inputs with validation or `try`/`except` in examples meant to be run by beginners.

### Coded example (Python + comments)

```python
"""Small pattern: plain attributes + fuel cost helper — clear names, no name clash."""


class Car:
    def __init__(
        self,
        color: str,
        door_count: int,
        seat_count: int,
        is_convertible: bool,
        consumption_l_per_100km: float,
        owner: str,
    ) -> None:
        self.color = color
        self.door_count = door_count
        self.seat_count = seat_count
        self.is_convertible = is_convertible
        self.consumption_l_per_100km = consumption_l_per_100km
        self.owner = owner

    def fuel_cost_per_100km(self, price_per_litre: float) -> float:
        return self.consumption_l_per_100km * price_per_litre

    def __str__(self) -> str:
        return (
            f"Car(color={self.color!r}, doors={self.door_count}, "
            f"seats={self.seat_count}, convertible={self.is_convertible}, "
            f"owner={self.owner!r})"
        )


def main() -> None:
    car = Car("Blue", 4, 5, False, 6.2, "Joan")
    print(car)
    print("Cost @ 1.50/L:", car.fuel_cost_per_100km(1.5))


if __name__ == "__main__":
    main()
```
