from typing_extensions import Annotated
import typer
from Services.cart import CartService
from Services.order import OrderService
from commands import users

app = typer.Typer()
cart = CartService()
order = OrderService(cart)
auth = users.auth


@app.command()
def place():
    auth.is_authenticated()
    order.place(auth.user)


@app.command()
def display():
    auth.is_authenticated()
    order.display(auth.user)


@app.command()
def history():
    auth.is_authenticated()
    order.history(auth.user)


@app.command()
def checkout(amout: int):
    auth.is_authenticated()
    order.checkout(auth.user, amout)
