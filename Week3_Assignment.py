def calculate_discount(price,discount_percent):
    if discount_percent >= 0.20 :
        fPrice = price - (price * discount_percent)
        return fPrice
    else :
        return price
    
price = float(input("Enter the original price\n"))
discount_percent = float(input("Enter the discount percentage\n"))
final_price = calculate_discount(price,discount_percent)
print(f"The final price after discount is: {final_price}")