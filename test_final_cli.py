import pytest
from click.testing import CliRunner
from final_project import cli, Margherita, Pepperoni, Hawaiian

runner = CliRunner()


def test_check_menu():
    result = runner.invoke(cli, ['menu'])
    assert result.exit_code == 0
    assert "Margherita" in result.output
    assert "Pepperoni" in result.output
    assert "Hawaiian" in result.output


def test_order_margherita():
    result = runner.invoke(cli, ['order', 'margherita'])
    assert result.exit_code == 0
    assert "Margherita" in result.output


def test_order_pepperoni_with_size():
    result = runner.invoke(cli, ['order', 'pepperoni', '--size', 'XL'])
    assert result.exit_code == 0
    assert "Pepperoni (XL)" in result.output


def test_invalid_size_order():
    result = runner.invoke(cli, ['order', 'margherita', '--size', 'M'])
    assert "NO SUCH SIZE" in result.output


def test_invalid_pizza_order():
    result = runner.invoke(cli, ['order', 'unknown'])
    assert "NO SUCH TYPE OF PIZZA" in result.output


def test_margherita_ingredients():
    pizza = Margherita('L')
    assert 'basil' in pizza.ingredients
    assert pizza.size == 'L'


def test_pepperoni_size_and_ingredients():
    pizza = Pepperoni('XL')
    assert pizza.size == 'XL'
    assert 'pepperoni' in pizza.ingredients


def test_hawaiian_pizza_dict():
    pizza = Hawaiian('L')
    pizza_info = pizza.dict()
    assert pizza_info['type'] == 'Hawaiian'
    assert 'pineapple' in pizza_info['ingredients']
