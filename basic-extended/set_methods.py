electronics_customers = {"Alex", "Maria", "John"}
clothing_customers = {"John", "Sophia", "Maria", "Mike"}

# all_customers = electronics_customers.union(clothing_customers)

# Also, you could use:
all_customers = electronics_customers | clothing_customers

print(all_customers) # {"Maria", "Alex", "Mike", "John", "Sophia"}


regular_customers = electronics_customers.intersection(clothing_customers)

# Also, you could use:
# regular_customers = electronics_customers & clothing_customers

print(regular_customers) # {"John", "Maria"}

