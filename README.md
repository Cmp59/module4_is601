# Module 4 Calculator

A command-line calculator built with Python and object-oriented design.

## Setup

Create and activate a virtual environment, then install the project dependencies:

```powershell
python -m venv .env
.\.env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation scripts, run this once for the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Run the Calculator

```powershell
python main.py
```

The calculator supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`). Enter `history` at the first-number prompt to view completed calculations, or enter `q` at any prompt to quit. The `CalculationFactory` creates a calculation instance for the selected operator, and completed instances are kept in session history.

## Run Tests

Run the test suite with coverage:

```powershell
python -m pytest
```

The project requires 100% test coverage. To enforce that requirement locally, run:

```powershell
python -m pytest --cov-fail-under=100
```

## Project Structure

- `app/operation/operations.py`: `Operations` class and arithmetic methods
- `app/calculator/calculator.py`: Interactive calculator REPL
- `app/calculation/calculation.py`: Calculation instances and their `perform()` method
- `app/calculation/calculation_factory.py`: Creates calculation instances by operator
- `app/calculation/calculation_history.py`: Stores and displays session calculations
- `tests/test_operations.py`: Parameterized arithmetic tests
- `tests/test_calculations.py`: Calculation, factory, and history tests
- `tests/test_calculator.py`: REPL tests
- `.github/workflows/ci.yml`: GitHub Actions configuration