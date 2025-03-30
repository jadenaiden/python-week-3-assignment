price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

def calculate_discount(price, discount_percent):
    discount_amount = price * discount_percent / 100
       

    if discount_percent >= 20:
        final_price = price - discount_amount
        return final_price
    else:
        return price



final_price = calculate_discount(price, discount_percent)
print("Final price:",' $',final_price)