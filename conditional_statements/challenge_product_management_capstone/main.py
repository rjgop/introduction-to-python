product_type = "Perishable"
days_until_expiration = 3 
stock_level = 55

if product_type == "Perishable":
    if days_until_expiration <= 3 and stock_level > 50:
        print(f"30% discount applied.")
    elif days_until_expiration >= 4 and days_until_expiration <= 6 and stock_level > 50:
        print(f"20% discount applied")
    elif days_until_expiration > 6 and stock_level <= 50:
        print(f"10% discount applied.")
else:
    print(f"No discount available for non-perishable items.")