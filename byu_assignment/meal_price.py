print("please enter the answer of the following question: \n")
child_meal = float(input("What is the price of a child's meal?: "))
adult_meal = float(input("What is the price of an adult's meal?: "))
milkshake = float(input("How much is a milkshake?: "))
soda = float(input("How much is a bottle of soda?: "))
child_num = int(input("How many children are there?: "))
adult_num = int(input("How many adults are there?: "))
tax_rate = float(input("What is the sales tax rate?: "))
tip_percentage = float(input("What is the tip percentage?: "))
subtotal = (child_meal + milkshake) * child_num + (adult_meal + soda) * adult_num
sales = subtotal * tax_rate / 100
tip = subtotal * tip_percentage / 100
total = sales + subtotal + tip
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Sales taxes: ${sales:.2f}")
print(f"Tip offered: ${tip:.2f}")
print(f"Total: ${total:.2f}")
payment = float(input("\nWhat is the payment amount?: "))
print(f"Change: ${payment-total:.2f}")
