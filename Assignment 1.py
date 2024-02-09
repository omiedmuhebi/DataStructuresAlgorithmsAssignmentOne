
# Define a class to represent a single product with its attributes
class Product:
    # Initialize a Product instance with ID, name, price, and category
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    # Return a string representation of the Product instance
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: ${self.price}, Category: {self.category}"

# Define a class to manage a collection of Product instances
class ProductManager:
    # Initialize the ProductManager with a filepath for product data and load products
    def __init__(self, filepath):
        self.filepath = filepath  # File path to the product data file
        self.products = []  # List to store Product instances
        self.load_products()  # Load products from the file upon initialization

    # Load product data from the specified file and create Product instances
    def load_products(self):
        with open(self.filepath, 'r') as file:  # Open file for reading
            for line in file:  # Iterate over each line in the file
                id, name, price, category = line.strip().split(', ')  # Parse product data
                self.products.append(Product(id, name, float(price), category))  # Create and add Product instance to list

    # Write the current list of Product instances back to the file
    def save_products_to_file(self):
        with open(self.filepath, 'w') as file:  # Open file for writing
            for product in self.products:  # Iterate over Product instances
                # Create a string for each product and write it to the file
                line = f"{product.id}, {product.name}, {product.price}, {product.category}\n"
                file.write(line)

    # Add a new Product instance to the list and save the updated list to the file
    def insert_product(self, id, name, price, category):
        new_product = Product(id, name, float(price), category)  # Create a new Product instance
        self.products.append(new_product)  # Add it to the list
        self.save_products_to_file()  # Save the updated list to the file

    # Update an existing Product instance based on ID
    def update_product(self, id, newName=None, newPrice=None, newCategory=None):
        for product in self.products:  # Iterate over the list to find the product
            if product.id == id:  # Check if the current product is the one to update
                # Update product attributes if new values are provided
                product.name = newName or product.name
                product.price = float(newPrice) if newPrice else product.price
                product.category = newCategory or product.category
                self.save_products_to_file()  # Save the updated list to the file
                return

    # Remove a Product instance from the list based on ID and save the updated list
    def delete_product(self, id):
        self.products = [product for product in self.products if product.id != id]  # Filter out the product to delete
        self.save_products_to_file()  # Save the updated list to the file

    # Search for and print a Product instance based on ID or name
    def search_product(self, identifier):
        for product in self.products:  # Iterate over the list to find the product
            if product.id == identifier or product.name == identifier:  # Check if the product matches the search criteria
                print(product)  # Print the product
                return
        print("Product not found.")  # Print not found message if no product matches

    # Sort the list of Product instances based on a specified attribute using Quick Sort
    def quick_sort(self, low, high, attr="price"):
        if low < high:
            pi = self.partition(low, high, attr)
            self.quick_sort(low, pi - 1, attr)
            self.quick_sort(pi + 1, high, attr)

    # Helper function for quick_sort to partition the list
    def partition(self, low, high, attr):
        pivot = getattr(self.products[high], attr)
        i = low - 1
        for j in range(low, high):
            if getattr(self.products[j], attr) <= pivot:
                i += 1
                self.products[i], self.products[j] = self.products[j], self.products[i]
        self.products[i + 1], self.products[high] = self.products[high], self.products[i + 1]
        return i + 1

    # Print all Product instances in the list
    def display_products(self):
        for product in self.products:  # Iterate over the list
            print(product)  # Print each product

# Main function to run the program
def main():
    # Initialize ProductManager with the path to the data file
    manager = ProductManager('C:\\Users\\Owner\\Downloads\\product_data.txt')

    # Main loop for user input and actions
    while True:
        # Display the menu options to the user.
        print("\nAvailable actions:")
        print("1: Insert a new product")
        print("2: Update an existing product")
        print("3: Delete a product")
        print("4: Search for a product")
        print("5. Sort products by price")
        print("6. Exit and display products")
        # Prompt the user to enter their choice based on the menu.
        choice = input('Enter your choice (1-6): ')
        print('\n')

        # Check the user's choice and call the corresponding method.
        if choice == '1':
            # Collect new product information from the user.
            id = input("Enter product ID to add: ")
            name = input("Enter product name: ")
            price = input("Enter price of product: ")
            category = input("Enter category of product: ")
            # Insert the new product into the product list.
            manager.insert_product(id, name, price, category)
            print('Product added successfully')

        elif choice == '2':
            # Collect product ID and new details for the product to be updated.
            id = input("Enter product ID to update: ")
            newName = input("Enter new name (or leave blank to keep current): ")
            newPrice = input("Enter new price (or leave blank to keep current): ")
            newCategory = input("Enter new category (or leave blank to keep current): ")
            # Update the specified product with new details.
            manager.update_product(id, newName=newName, newPrice=newPrice, newCategory=newCategory)
            print("Product updated successfully")

        elif choice == '3':
            # Prompt the user for the ID of the product to delete.
            identifier = input('Enter the ID of the product to delete: ')
            # Delete the specified product from the list.
            manager.delete_product(identifier)
            print('Product deleted successfully')

        elif choice == '4':
            # Prompt the user for the name or ID of the product to search for.
            identifier = input('Enter the name or ID of the product to search: ')
            # Search for and display the specified product.
            manager.search_product(identifier)

        elif choice == '5':
            # Sort the products by price.
            manager.quick_sort(0, len(manager.products) - 1)
            # Display the sorted list of products.
            manager.display_products()

        elif choice == '6':
            # Save any changes made to the products back to the file.
            manager.save_products_to_file()
            print("Final list of products:")
            # Display the final list of products before exiting.
            manager.display_products()
            # Exit the loop, thus ending the program.
            break

# Check if the script is the main program and if so, execute main().
if __name__ == "__main__":
    main()
