# Number 1
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
# Number 2
preferred_size = ["Small", "Large", "Medium"]
# Number 3
preferred_size.append("Medium")
print(preferred_size)
# Number 4
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
# Number 5
customer_data[2][2] = False
# Number 6
customer_data[1].remove(False)
# Number 7
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
