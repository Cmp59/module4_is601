import pytest

from app.calculation import Calculation, CalculationFactory


@pytest.mark.parametrize(
    "operator, first_number, second_number, expected_result",
    [
        ("+", 2, 3, 5),
        ("-", 5, 3, 2),
        ("*", 2, 3, 6),
        ("/", 6, 3, 2),
    ],
)
def test_factory_creates_calculation_instances(
    operator, first_number, second_number, expected_result
):
    calculation = CalculationFactory.create(
        operator, first_number, second_number
    )

    assert isinstance(calculation, Calculation)
    assert calculation.perform() == expected_result


@pytest.mark.parametrize("operator", ["+", "-", "*", "/"])
def test_factory_supports_basic_operators(operator):
    assert CalculationFactory.supports(operator)


def test_factory_rejects_unsupported_operator():
    with pytest.raises(ValueError, match="Unsupported operation: %"):
        CalculationFactory.create("%", 2, 3)


def test_factory_reports_unsupported_operator():
    assert not CalculationFactory.supports("%")