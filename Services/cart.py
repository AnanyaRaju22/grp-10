from models import Cart, Food
from Exceptions import foodieexit
from rich.console import Console
from rich.table import Table

console = Console()


class CartService:
    def add_item(self, user, name: str, quantity: int):
        cart_item: Cart = self.get_cart_item(user=user, name=name)
        food = Food.get(name=name)
        cart_item.add(quantity=quantity)
        food.pick_item(name, quantity)

    def remove_item(self, user, name: str, quantity: int):
        cart_item: Cart = self.get_cart_item(user=user, name=name)
        cart_item.remove(quantity=quantity)
        food = Food.get(name=name)
        food.drop_item(name, quantity)

    @staticmethod
    def get_cart_item(user, name: str) -> Cart:
        food = Food.get(name=name)
        try:
            cart_item = Cart.get(item=food, user=user)
        except Cart.DoesNotExist:
            cart_item = Cart.create(item=food, user=user, quantity=0)
        return cart_item

    def display(self, user):
        cart = Cart.filter(user=user)
        count = cart.count()

        if count == 0:
            print("Your cart looks empty, add some items!")
            return

        table = Table("sl.No.", "Item", "Quantity", "Price", "Amount")
        for i, ci in enumerate(cart):
            table.add_row(
                f"{i + 1}",
                ci.item.name,
                str(ci.quantity),
                f"Rs. {ci.item.price}",
                f"Rs. {ci.quantity * ci.item.price}",
            )
        console.print(table)
        total_price = self.total_price(cart)
        print(f"Total items: {count} | price: Rs. {total_price}")

    def total_price(self, cart):
        price = 0
        for i in cart:
            price = price + (i.quantity * i.item.price)
        return price

    
    
    def clear(self, user):
        cart_items = Cart.select().where(Cart.user == user)
        for cart_item in cart_items:
            cart_item.delete_instance()
        print("Cart has been cleared.")
