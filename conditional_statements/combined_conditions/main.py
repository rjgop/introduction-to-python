discounted = False
lowStock = True
movingProduct = (discounted) or (lowStock)
promotion = not(discounted) and not(lowStock)
print(f"Is the item eligible for promotion? {promotion}")
