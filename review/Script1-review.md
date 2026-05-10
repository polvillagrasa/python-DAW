# Code review — Login script without entry guard (`Exemples Programació Modular-20260502/Script1.py`)

_Review date: 9 de maig de 2026._

## Activity: Modular login (always runs on import)

### Assignment

- **Source read:** None found.
- **Summary (optional):** Asks username/password, validates against fixed credentials, prints success or failure, calls `main()` at module level.

### Acceptance criteria

(Inferred.)

- [x] Separates input (`demanar_dades`), validation (`validar_inici_sessio`), and orchestration (`main`).
- [x] Uses a boolean return for validation outcome.
- [ ] **Import safety:** `main()` runs on import — importing the module from `Script3.py` would have executed login twice if not for `Script3` only importing helpers; still risky for reuse/tests.
- [ ] **Security note:** hard-coded credentials are expected only for classroom demos — flag clearly.

### Analysis

- `validar_inici_sessio` can be simplified to `return usuari == "admin" and contrasenya == "1234"` (no `if`/`else`).
- Top-level `main()` call means any `import Script1` triggers interactive I/O — `Script2` fixes this with `if __name__ == "__main__"`.

### Improvement proposals

1. Match `Script2.py` structure: only invoke `main()` under `__name__ == "__main__"`.
2. Document that plaintext passwords are for learning only.
3. Use English identifiers if adopting the repository language policy.

### Coded example (Python + comments)

```python
"""Same flow with a safe entry point for imports and tests."""


def read_credentials() -> tuple[str, str]:
    user = input("Username: ")
    password = input("Password: ")
    return user, password


def credentials_ok(user: str, password: str) -> bool:
    return user == "admin" and password == "1234"


def main() -> None:
    print("=== Login (demo) ===")
    user, password = read_credentials()
    if credentials_ok(user, password):
        print(f"Welcome, {user}.")
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    main()
```
