
# ==============================================
# Kiryana Store Manager - Beginner Python Project
# ==============================================

# Step 1: Store Information

STORE_INFO = ("Kiryana Store", "Main Bazaar Road, Lahore", "0300-1234567")  # Store ka name, address aur phone save kar rahe hain.

# Step 2: Store Prices

prices = {"rice": 280, "sugar": 150, "milk": 220, "tea": 950, "oil": 540}  # Dictionary mein grocery items ki prices save kar rahe hain.

# Step 3: Available Stock

stock = {"rice": 20, "sugar": 3, "milk": 10, "tea": 8, "oil": 15}  # Dictionary mein items ka available stock save kar rahe hain.

# Step 4: Welcome Message

print("=" * 40)  # Welcome message ke upar line print kar rahe hain.
print(f"Welcome to {STORE_INFO[0]}!")  # Store ka name print kar rahe hain.
print(f"Address: {STORE_INFO[1]}")  # Store ka address print kar rahe hain.
print(f"Phone: {STORE_INFO[2]}")  # Store ka phone number print kar rahe hain.
print("=" * 40)  # Welcome message ke neeche line print kar rahe hain.

# Step 5: Main Menu

while True:  # Menu ko baar baar show karne ke liye loop chala rahe hain.

    print("\n===== MAIN MENU =====")  # Menu ka heading print kar rahe hain.
    print("1. View Inventory")  # Inventory option show kar rahe hain.
    print("2. New Sale")  # New sale option show kar rahe hain.
    print("3. Exit")  # Exit option show kar rahe hain.

    choice = input("Enter your choice (1-3): ").strip()  # User se menu choice le rahe hain.

    # Step 6: View Inventory

    if choice == "1":  # Agar user 1 select kare.

        print("\n--- INVENTORY ---")  # Inventory heading print kar rahe hain.

        for item in prices:  # Prices dictionary ke har item par loop chala rahe hain.

            print(f"{item.capitalize()} - Rs. {prices[item]} - Stock: {stock[item]}")  # Item name, price aur stock print kar rahe hain.

            if stock[item] < 5:  # Check kar rahe hain ke stock 5 se kam hai.
                print("LOW STOCK")  # Low stock warning show kar rahe hain.

    # Step 7: New Sale

    elif choice == "2":  # Agar user 2 select kare.

        cart = []  # Customer ke items store karne ke liye empty list bana rahe hain.

        print("\n--- NEW SALE ---")  # New sale heading print kar rahe hain.

        while True:  # Customer se items lene ke liye loop chala rahe hain.

            item = input("Item (or done): ").strip().lower()  # Item ka name le rahe hain aur lowercase kar rahe hain.

            if item == "done":  # Check kar rahe hain ke customer shopping complete kar chuka hai.
                break  # Shopping loop stop kar rahe hain.

            if item not in prices:  # Check kar rahe hain ke item store mein available hai.
                print("Item not found.")  # Item na milne par message print kar rahe hain.
                continue  # Dobara item mangwane ke liye loop continue kar rahe hain.

            qty_input = input("Quantity: ").strip()  # Customer se quantity le rahe hain.

            if not qty_input.isdigit():  # Check kar rahe hain ke quantity number hai.
                print("Please enter a number.")  # Invalid quantity ka message print kar rahe hain.
                continue  # Dobara input lene ke liye loop continue kar rahe hain.

            qty = int(qty_input)  # Quantity ko integer mein convert kar rahe hain.

            if qty <= 0:  # Check kar rahe hain ke quantity zero ya negative nahi hai.
                print("Quantity must be greater than zero.")  # Error message print kar rahe hain.
                continue  # Dobara input lene ke liye loop continue kar rahe hain.

            if qty > stock[item]:  # Check kar rahe hain ke required stock available hai.
                print(f"Only {stock[item]} left in stock.")  # Available stock show kar rahe hain.
                continue  # Dobara item lene ke liye loop continue kar rahe hain.

            line_total = prices[item] * qty  # Item ki price ko quantity se multiply kar rahe hain.

            cart.append((item, qty, prices[item]))  # Item, quantity aur price ka tuple cart mein add kar rahe hain.

            stock[item] = stock[item] - qty  # Purchased quantity stock se minus kar rahe hain.

            print(f"Added {item} x {qty} = Rs. {line_total}")  # Purchase confirmation print kar rahe hain.

        # Step 8: Generate Bill

        if len(cart) == 0:  # Check kar rahe hain ke cart empty hai.
            print("Cart is empty. No sale made.")  # Empty cart ka message print kar rahe hain.

        else:  # Agar cart mein items hain.

            total = 0  # Total bill zero se start kar rahe hain.

            print("\n----- CUSTOMER BILL -----")  # Bill heading print kar rahe hain.

            for item, qty, price in cart:  # Cart se item, quantity aur price read kar rahe hain.

                line_total = price * qty  # Har item ka total calculate kar rahe hain.

                print(f"{item} x {qty} = Rs. {line_total}")  # Bill mein item aur price print kar rahe hain.

                total = total + line_total  # Item ka total bill mein add kar rahe hain.

            # Step 9: Calculate Discount

            discount = 0  # Discount zero set kar rahe hain.

            if total > 3000:  # Check kar rahe hain ke total 3000 se zyada hai.
                discount = total * 10 / 100  # Total ka 10 percent discount calculate kar rahe hain.

            final = total - discount  # Total mein se discount minus kar rahe hain.

            # Step 10: Print Final Bill

            print("--------------------------")  # Bill separator print kar rahe hain.
            print(f"Total: Rs. {total}")  # Total bill print kar rahe hain.
            print(f"Discount: Rs. {discount}")  # Discount print kar rahe hain.
            print(f"Pay: Rs. {final}")  # Final payment print kar rahe hain.

    # Step 11: Exit Program

    elif choice == "3":  # Agar user 3 select kare.

        print("Thank you, goodbye!")  # Goodbye message print kar rahe hain.
        break  # Main menu loop stop kar rahe hain.

    # Step 12: Invalid Choice

    else:  # Agar user invalid choice enter kare.

        print("Invalid choice.")  # Invalid choice message print kar rahe hain.
