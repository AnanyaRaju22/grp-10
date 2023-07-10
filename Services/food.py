from models import Food, Restaurant
from rich.console import Console
from rich.table import Table

console = Console()


class FoodService:
    def add(self, name: str, restaurant: str, price: int, is_veg: bool = True, quantity: int = 0):
        try:
            restaurant_obj = Restaurant.get(Restaurant.name == restaurant)
        except Restaurant.DoesNotExist:
            print(f"Restaurant '{restaurant}' does not exist.")
            return

        try:
            food = Food.create(name=name, restaurant=restaurant_obj, price=price, is_veg=is_veg, quantity=quantity)
            print(f"Food '{food.name}' added successfully.")
        except Exception as e:
            print(f"Error adding food: {str(e)}")

    def add_prompt(self, name: str, price: int, is_veg: bool = True, quantity: int = 0):
        while True:
            restaurant = input("Enter the restaurant name: ")
            if Restaurant.select().where(Restaurant.name == restaurant).exists():
                self.add(name, restaurant, price, is_veg, quantity)
                break
            else:
                print(f"Restaurant '{restaurant}' does not exist. Please enter a valid restaurant name.")

    def remove(self, name: str):
        try:
            food = Food.get(name=name)
            food.delete_instance()
            print(f"Food '{name}' has been removed.")
        except Food.DoesNotExist:
            print(f"Food '{name}' does not exist.")



    def list(self):
        foods = Food.select()

        if foods.count() == 0:
            print("No food items found.")
            return

        table = Table("sl.No.", "Name", "Price", "Is Veg", "Food-id")
        for i, food in enumerate(foods):
            table.add_row(
                f"{i + 1}",
                food.name,
                str(food.price),
                "Yes" if food.is_veg else "No",
                str(food.id),
            )

        console.print("List of all food items:")
        console.print(table)
