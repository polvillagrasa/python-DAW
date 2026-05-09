# Code review — registration, sign-in, and summary (`pol_exercices/app.py`)

_Data de la revisió: 9 de maig de 2026._

## Activity: Registration → session → summary (`app.py`)

### Assignment

- **Source read:** None found in the repository (searched: `README.md`, `**/enunciado.md`, `**/ENUNCIAT.md`, `**/AC.md`, `docs/`, and `pol_exercices/` next to `app.py`). No brief was attached in chat for this update.
- **Summary (inferred):** A linear script collects user registration fields, performs a username/password check for sign-in, then prints a short summary of some fields.

### Acceptance criteria

_Inferred, checkable behaviours from the script’s apparent intent._

- [x] Collect first name, last name, birth date, city, postal code, username, password, student flag, age, and adult flag via prompts.
- [x] Confirm registration completed, then prompt for sign-in with username and password.
- [x] Report whether sign-in matched the registered credentials.
- [ ] Include **all** collected fields in the final summary (student and adult flags are collected but not printed).
- [x] Program runs for happy-path numeric postal code input.

### Analysis

- **Context:** the script collects registration data, then credentials for sign-in, and prints a partial data summary.
- **What the code does:** a linear sequence of `input` calls, script-level variables, compares username/password to the sign-in attempt, prints messages and a summary.
- **Strengths:** easy to follow for a first exercise; the credential comparison clearly states intent.
- **Weak spots / risks:**
  - 🔴 `int(input(...))` for postal code: non-numeric or empty input raises **`ValueError`** (unvalidated input).
  - `estudiant` and `major_edat` are collected but **omitted from the summary**, which looks like forgotten requirements or an incomplete flow.
  - **Plaintext password** in memory and re-entered: fine for a classroom script, but real apps must not treat passwords this way (security awareness).
  - All logic at **module top level** hurts **testing** and **reuse** (one unstructured script).
  - Typos in `input` prompts (“introdeuix”, etc.) hurt polish and readability.
- **Basics:** variable names are mostly clear (`nom_usuari2` is weaker than e.g. `entered_username`); each phase could be a small function without jumping to heavy architecture.

### Improvement proposals

1. **Validate or handle postal code input** — robustness: avoid crashing the whole program on bad input (`try/except` or parse as string then validate before `int()`).
2. **Split into functions** (`collect_registration()`, `verify_sign_in()`, `print_summary()`) — readability and separation of concerns; teaches “one job per function” at this level.
3. **Align summary with prompts** — either print all collected fields or stop asking for unused ones (functional consistency).
4. **Rename second-login variables** to reflect “attempt” or “session” — naming / clean code.
5. **Fix prompt strings** — presentation quality even in exercises.
6. **Optional teaching note:** in production, passwords are hashed and never logged in plaintext — language-agnostic principle.

### Coded example (Python + comments)

Illustrative fragment (your teacher may still want a fully linear script); shows **functions**, **gentle postal validation**, and a **complete summary**.

```python
"""Example: phase-based structure and safer input.

Each function covers one step — single responsibility without advanced patterns;
the idea applies in any language.
"""


def read_postal_code() -> int:
    """Loop until valid input: keeps user mistakes from crashing the program."""
    while True:
        text = input("Postal code (5 digits): ").strip()
        if text.isdigit() and len(text) == 5:  # simple rule; adjust if needed
            return int(text)
        print("Invalid postal code. Try again.")


def collect_registration() -> dict[str, str]:
    """Return a dict so later steps receive one structured object."""
    return {
        "first_name": input("First name: ").strip(),
        "last_name": input("Last name: ").strip(),
        "birth_date": input("Birth date: ").strip(),
        "city": input("City: ").strip(),
        "postal_code": str(read_postal_code()),
        "username": input("Username: ").strip(),
        "password": input("Password: ").strip(),
        "is_student": input("Student? Yes/No: ").strip(),
        "age": input("Age: ").strip(),
        "is_adult": input("Legal adult? Yes/No: ").strip(),
    }


def verify_sign_in(expected_username: str, expected_password: str) -> bool:
    """Return bool instead of printing inside logic: separates decision from UI."""
    user = input("Username: ").strip()
    pwd = input("Password: ").strip()
    return user == expected_username and pwd == expected_password


def print_summary(data: dict[str, str], sign_in_ok: bool) -> None:
    """Single place for output formatting — easier to change later."""
    print("\n--- Summary ---")
    print(f"Full name: {data['first_name']} {data['last_name']}")
    print(
        f"Age: {data['age']} | Adult: {data['is_adult']} | Student: {data['is_student']}"
    )
    print(f"Session: {'ok' if sign_in_ok else 'failed'}")


def main() -> None:
    data = collect_registration()
    print("Registration completed.")

    print("\nSign in:")
    ok = verify_sign_in(data["username"], data["password"])
    print("Sign-in successful." if ok else "Sign-in failed.")

    print_summary(data, ok)


if __name__ == "__main__":
    main()
```
