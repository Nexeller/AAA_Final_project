import click
import random
import functools


class BasePizza:
    """Представляет общую пиццу с указанием размера, названия и ингредиентов."""

    def __init__(self, size='L'):
        if size.upper() not in ['L', 'XL']:
            raise ValueError("NO SUCH SIZE")
        self.size = size.upper()
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_description(self):
        return f"{self.__class__.__name__} ({self.size}) with {' '.join(self.ingredients)}"

    def dict(self):
        return {
            "type": self.__class__.__name__,
            "size": self.size,
            "ingredients": self.ingredients
        }


class Margherita(BasePizza):
    """Класс пиццы Маргарита, подкласс BasePizza."""

    def __init__(self, size='L'):
        super().__init__(size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('basil')


class Pepperoni(BasePizza):
    """Класс пиццы Пепперони, подкласс BasePizza."""

    def __init__(self, size='L'):
        super().__init__(size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('pepperoni')


class Hawaiian(BasePizza):
    """Класс пиццы Гавайская, подкласс BasePizza."""

    def __init__(self, size='L'):
        super().__init__(size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('ham')
        self.add_ingredient('pineapple')


def log_execution_time(func):
    """
    Декоратор, который выводит случайное время выполнения
    в дополнение к выводу функции
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)  # результат ф-ции до декорирования
        return f'{original_result} - {random.randint(1, 10)}с!'

    return wrapper


@click.group()
def cli():
    """Выбираем пиццу из нашего меню."""
    pass


@click.command()
def menu():
    """Выводит меню наших пицц."""
    for pizza_class in [Margherita, Pepperoni, Hawaiian]:
        pizza = pizza_class()
        click.echo(pizza.get_description())


@click.command()
@click.argument('type')
@click.option('--size', default='L', help='Size of the pizza (L, XL)')
@click.option('--delivery', is_flag=True, help='Include if you want delivery')
@log_execution_time
def order(type: str, size: str, delivery: bool):
    '''Готовит и доставляет пиццу'''

    if type.strip().lower() not in ('pepperoni', 'hawaiian', 'margherita'):
        print('We don\'t have this kind of pizza, call back later.')
    else:
        print(f'Prepared for {random.randint(1, 10)}с!')
        if delivery:
            print(f'Delivered in {random.randint(1, 10)}с!')


cli.add_command(menu)
cli.add_command(order)

if __name__ == '__main__':
    cli()
