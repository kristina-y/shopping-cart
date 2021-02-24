# shopping_cart.py



 

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Organic Bananas", "department": "produce", "aisle": "fruit", "price": .79, "price_per": "pound"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
# modified products to add Organic Bananas


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# empty list of items that will be filled with user inputs
grocery_list = []

# capturing using inputs
while True:
    
    user_input = input("Please input a product identifier, or type 'DONE' of there are no more: ")

    if user_input == "DONE":
        
        #End while loop if user typed "DONE"
        break

    else:

        # verify the user input
        try:
            identifier = int(user_input)
            if (identifier in range(1,len(products)+1)):
                # user_input is valid! Adding to list
                grocery_list.append(identifier)
            else:
                print("The product identifier should be an integer between 1 and 21. Please try again.")
        
        except ValueError:
            # User input is invalid
            print("The product identifier should be an integer between 1 and 21. Please try again.")
        # The try... except... method of validating input was adapted from pynative.com

def lookup_product(product_identifier):
    # Takes in the product identifier and returns the name and price, using the products list
    product_info = products[product_identifier]
    product_name = product_info["name"]
    product_price = product_info["price"]
    product_name_and_price = {"name": product_name, "price": product_price}
    return product_name_and_price


# Print Receipt Header:
print("---------------------------")
print("KRISTINA'S GROCERY STORE")
print("---------------------------")
print("Web: KRISTINA-GROCERY.COM")
print("Phone: (202) 123-4567")
print("---------------------------")
print("Shopping Cart Items:")


# Loop through grocery_list, printing out the name and price of each product
total_price = 0
for i in grocery_list:
    results = lookup_product(i - 1)
    total_price = total_price + results["price"]
    print("... ", results["name"], to_usd(results["price"]))
print("---------------------------")
print("SUBTOTAL: ", to_usd(total_price))

taxes = total_price * 0.06

print("SALES TAX IN DC:", to_usd(taxes))
print("TOTAL:", to_usd(total_price + taxes))

# print(products)