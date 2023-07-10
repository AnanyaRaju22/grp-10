from models import Restaurant, Food
from rich.console import Console
from rich.table import Table

console = Console()


class RestaurantService:
    def add_restaurant(self, name: str, rating: float):
        while rating < 0 or rating > 5:
            print("Rating should be between 0 and 5.")
            rating = float(input("Please enter a valid rating: "))

        while True:
            try:
                restaurant = Restaurant.create(name=name, rating=rating)
                print(f"Restaurant '{restaurant.name}' added successfully.")
                break  # Exit the loop if the restaurant is created successfully
            except Exception as e:
                print(f"Error adding restaurant: {str(e)}")
                name = input("Please enter a different restaurant name: ")



    def remove_restaurant(self, name: str):
        try:
            restaurant = Restaurant.get(name=name)
            restaurant.delete_instance()
            print(f"Restaurant '{restaurant.name}' has been removed from the restaurant list.")
        except Restaurant.DoesNotExist:
            print(f"Restaurant '{name}' does not exist.")

    def display_restaurants(self):
        restaurants = Restaurant.select()

        table = Table("sl.No.", "Name", "Rating", "Restaurant-id")
        for i, restaurant in enumerate(restaurants):
            table.add_row(
                f"{i + 1}",
                restaurant.name,
                str(restaurant.rating),
                str(restaurant.id),
            )

        console.print(table)

    def list_foods(self, restaurant_name: str):
        while True:
            try:
                restaurant = Restaurant.get(name=restaurant_name)
                foods = Food.select().where(Food.restaurant == restaurant)

                if foods.count() == 0:
                    print(f"No food items found for restaurant '{restaurant_name}'.")
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

                console.print(f"Food items for restaurant '{restaurant_name}':")
                console.print(table)
                break
            except Restaurant.DoesNotExist:
                print(f"Restaurant '{restaurant_name}' does not exist.")
                restaurant_name = input("Enter the restaurant name again: ")
