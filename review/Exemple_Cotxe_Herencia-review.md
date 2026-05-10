# Code review — Inheritance and vehicle hierarchy (`Exemple_Cotxe_Herencia.ipynb`)

_Review date: 9 de maig de 2026._

## Activity: Base class, manager, and specialized `Cotxe`

### Assignment

- **Source read:** None found beyond the notebook.
- **Summary (optional):** Extends the earlier car model with `Vehicle_motor`, a `Gestor_Vehicles` helper, list-driven registration, then `Cotxe(Vehicle_motor)` with overridden `__str__`, and a loop that chooses car vs generic vehicle.

### Acceptance criteria

(Inferred.)

- [x] Shows inheritance (`Cotxe` calls `super().__init__` with wheel count fixed to 4).
- [x] Groups interactive creation in `Gestor_Vehicles` with two factory-style methods.
- [x] Polymorphic printing over a mixed `vehicles` list via `__str__`.
- [ ] **Consistent encapsulation:** `Cotxe` repeats the `descapotable` method/field naming issue from the base car notebook; `Vehicle_motor` uses a single-underscore `propietari` while earlier material used double-underscore — fine, but should be explained as a convention change.
- [ ] **Motor / speed state:** `Cotxe` passes `0` and `False` for speed/motor; `accelerar`/`frenar` exist on base but are not demonstrated — optional extension.

### Analysis

- **`Gestor_Vehicles` duplication:** `demanar_dades_vehicle` and `demanar_dades_cotxe` repeat prompts; a shared private helper for “owner + color + consumption” would reduce copy-paste as students advance.
- **`Cotxe.__str__`:** correctly adds doors/seats/convertible while reusing base fields; commented alternative calling `super().__str__()` is a nice teaching branch.
- **Notebook flow:** relies on running cells in order so `vehicles` exists before the final `for` loop — normal for Jupyter but worth stating in class.

### Improvement proposals

1. Align naming style (`VehicleMotor` in English for shared repos, or keep Catalan consistently across *all* identifiers for local-only material).
2. Extract shared input fragments to reduce duplicated `input` blocks.
3. Fix `descapotable` getter/setter naming clash the same way as in the non-inheritance notebook review.

### Coded example (Python + comments)

```python
"""Minimal inheritance sketch: shared engine behavior, specialized string form."""


class MotorVehicle:
    def __init__(self, color: str, wheel_count: int, consumption: float, owner: str) -> None:
        self.color = color
        self.wheel_count = wheel_count
        self.consumption = consumption
        self._owner = owner

    def fuel_cost_per_100km(self, price_per_litre: float) -> float:
        return self.consumption * price_per_litre


class Car(MotorVehicle):
    def __init__(
        self,
        color: str,
        consumption: float,
        owner: str,
        door_count: int,
        seat_count: int,
        is_convertible: bool,
    ) -> None:
        super().__init__(color, 4, consumption, owner)
        self.door_count = door_count
        self.seat_count = seat_count
        self.is_convertible = is_convertible

    def __str__(self) -> str:
        return (
            f"Car({self.color!r}, doors={self.door_count}, seats={self.seat_count}, "
            f"convertible={self.is_convertible}, owner={self._owner!r})"
        )


def main() -> None:
    fleet: list[MotorVehicle] = [
        MotorVehicle("Red", 2, 3.0, "Alex"),
        Car("Blue", 5.5, "Joan", 5, 5, True),
    ]
    for vehicle in fleet:
        print(vehicle)


if __name__ == "__main__":
    main()
```
