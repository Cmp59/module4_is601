"""A calculation instance that can be performed."""

from typing import Callable


class Calculation:
    """Store the operands and operation for one calculation."""

    def __init__(
        self,
        first_number: float,
        second_number: float,
        operation: Callable[[float, float], float],
    ):
        self.first_number = first_number
        self.second_number = second_number
        self.operation = operation

    def perform(self) -> float:
        """Run the stored operation and return its result."""
        return self.operation(self.first_number, self.second_number)