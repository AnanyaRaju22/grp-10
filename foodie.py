import typer
from peewee import *
from models import create_tables
from commands import users, restaurant, food,cart,order

app = typer.Typer()

user_session = users.user_session
auth = users.auth

app.add_typer(users.app, name="users")
app.add_typer(restaurant.app, name="restaurant")
app.add_typer(food.app, name="food") 
app.add_typer(cart.app, name="cart")
app.add_typer(order.app, name="order")



if __name__ == "__main__":
    create_tables()
    with user_session:
        auth.load_session()
        app()
