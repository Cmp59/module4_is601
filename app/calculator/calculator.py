"""Command-line calculator."""

from ..calculation import CalculationFactory, CalculationHistory


def calculator():
    """Run the calculator until the user chooses to quit."""
    history = CalculationHistory()
    print(
        "Calculator: enter q at any prompt to quit, or 'history' "
        "at the first-number prompt to view calculations."
    )

    while True:
        first_input = input("First number: ").strip()
        if first_input.lower() == "q":
            break
        if first_input.lower() == "history":
            print(history.format_entries())
            continue

        operator = input("Operation (+, -, *, /): ").strip()
        if operator.lower() == "q":
            break
        if not CalculationFactory.supports(operator):
            print("Please choose +, -, *, or /.")
            continue

        second_input = input("Second number: ").strip()
        if second_input.lower() == "q":
            break

        try:
            first_number = float(first_input)
            second_number = float(second_input)
            calculation = CalculationFactory.create(
                operator, first_number, second_number
            )
            result = calculation.perform()
        except ValueError as error:
            print(f"Error: {error}")
            continue

        history.add(calculation)
        print(f"Result: {result}")


if __name__ == "__main__":
    calculator()