# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating the final price
final_price = calculate_discount(original_price, discount_percent)

# Printing the final price or the original price if no discount is applied
if final_price == original_price:
    print(f"No discount applied. The original price is: ${final_price:.2f}")
else:
    print(f"Final price after discount: ${final_price:.2f}")
