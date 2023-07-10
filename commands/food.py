import typer
from typing_extensions import Annotated
from Services.food import FoodService

food_service = FoodService()

app = typer.Typer()


@app.command()
def add(
    name: str = typer.Option(..., prompt=True, help="Enter the food name"),
    restaurant: str = typer.Option(..., prompt=True, help="Enter the restaurant name"),
    price: int = typer.Option(..., prompt=True, help="Enter the price"),
    is_veg: bool = typer.Option(True, prompt=True, help="Specify if the food is vegetarian (True/False)"),
    quantity: int = typer.Option(..., prompt=True, help="Enter the quantity")
):
    food_service.add(name, restaurant, price, is_veg, quantity)


@app.command()
def remove(
    name: Annotated[str, typer.Option(prompt=True)]
):
    food_service.remove(name)


@app.command(name="list")
def list_foods():
    food_service.list()


if __name__ == "__main__":
    app()

