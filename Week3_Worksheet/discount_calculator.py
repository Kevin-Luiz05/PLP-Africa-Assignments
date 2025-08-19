# PLP Africa Week 3, Day 2 Practical Assignment
# Topic: Control Flows and Functions in Python
# Author: Kevin Kamau
# Date: 2025-08-19
# --------------------------------------------
# Function: calculate_discount(price, discount_percent)
# This function calculates the final price after applying
# a discount. If discount >= 20%, discount is applied,
# otherwise the original price is returned.

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount.

    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage

    Returns:
    float: Final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# --- Main Program ---
try:
    # Prompt user input
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call function
    final_price = calculate_discount(price, discount_percent)

    # Output
    if discount_percent >= 20:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")

except ValueError:
    print("⚠️ Please enter valid numeric values for price and discount.")
