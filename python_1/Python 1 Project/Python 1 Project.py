
SHOP_NAME = "Max's Pizza Shack"
TAX_RATE = 0.08
is_shop_open = True


pizza_menu = ["Cheese", "Pepperoni", "Veggie", "Supreme"]


def make_cheese():
    print("Baking a classic Cheese pizza!")
    print("Adding lots of mozzarella cheese.")

def make_pepperoni():
    print("Baking a Pepperoni pizza!")
    print("Adding spicy pepperoni slices.")

def make_veggie():
    print("Baking a Veggie pizza!")
    print("Adding peppers, onions, and mushrooms.")


print("Welcome to our pizza shop!")
user_order = input("What kind of pizza do you want? (Cheese, Pepperoni, or Veggie): ")


if user_order == pizza_menu[0]:
    make_cheese()
elif user_order == pizza_menu[1]:
    make_pepperoni()
elif user_order == pizza_menu[2]:
    make_veggie()
else:
    print("Sorry, we do not have that pizza today.")


current_box = 1
total_boxes = 5

print("\nTime to box up the pizzas!")
while current_box < total_boxes:
    print("Packing box number:")
    print(current_box)
    current_box = current_box + 1

print("All done packing!")
