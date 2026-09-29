"""A calculation instance that can be performed."""

from typing import Callable


class Calculation:
    """Store the operands and operation for one calculation."""

    def __init__(
        self,
        first_number: float,
        second_number: float,
        operator_symbol: str,
        operation: Callable[[float, float], float],
    ):
        self.first_number = first_number
        self.second_number = second_number
        self.operator_symbol = operator_symbol
        self.operation = operation

    def perform(self) -> float:
        """Run the stored operation and return its result."""
        return self.operation(self.first_number, self.second_number)

    def __str__(self) -> str:
        """Format the calculation and its result for display."""
        result = self.perform()
        return (
            f"{self.first_number} {self.operator_symbol} "
            f"{self.second_number} = {result}"
        )