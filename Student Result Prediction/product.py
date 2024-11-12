# Function to retrieve data based on ID
def retrieve_data(product_id, filename='products.txt'):
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into ID, Name, and Number
            parts = line.strip().split('=')
            current_id = parts[0]
            name = parts[1]
            number = parts[2]

            # Check if the entered ID matches the current product's ID
            if current_id == product_id:
                return name, number
    # Return None if ID is not found
    return None, None


# Input the product ID
product_id = input("Enter the product ID (first 3 digits): ")

# Retrieve data based on the entered ID
product_name, product_number = retrieve_data(product_id)

# Check if data is found
if product_name is not None:
    print(f"Name: {product_name}\nNumber: {product_number}")
else:
    print("Product not found.")
