"""Create calculation instances for supported operators."""

from ..operation import Operations
from .calculation import Calculation


class CalculationFactory:
    """Select and create calculations based on an operator symbol."""

    _OPERATIONS = {
        "+": Operations.addition,
        "-": Operations.subtraction,
        "*": Operations.multiplication,
        "/": Operations.division,
    }

    @classmethod
    def supports(cls, operator: str) -> bool:
        """Return whether the operator is supported."""
        return operator in cls._OPERATIONS

    @classmethod
    def create(
        cls, operator: str, first_number: float, second_number: float
    ) -> Calculation:
        """Create a calculation instance, raising for unknown operators."""
        try:
            operation = cls._OPERATIONS[operator]
        except KeyError as error:
            raise ValueError(f"Unsupported operation: {operator}") from error

        return Calculation(first_number, second_number, operator, operation)