class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("ID must be a positive integer.")
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

    def update_item(self, item_id, name=None, description=None, price=None):
        try:
            if item_id not in self.items:
                raise ValueError("Item not found.")
            
            item = self.items[item_id]
            if name:
                item.name = name
            if description:
                item.description = description
            if price is not None:
                if not isinstance(price, (int, float)) or price < 0:
                    raise ValueError("Price must be a non-negative number.")
                item.price = price
            print("Item updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        try:
            if item_id not in self.items:
                raise ValueError("Item not found.")
            del self.items[item_id]
            print("Item deleted successfully.")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            try:
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Name: ")
                description = input("Enter Description: ")
                price = float(input("Enter Price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == "2":
            manager.read_items()
        elif choice == "3":
            try:
                item_id = int(input("Enter Item ID to update: "))
                name = input("Enter new Name (leave blank to keep current): ") or None
                description = input("Enter new Description (leave blank to keep current): ") or None
                price_input = input("Enter new Price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == "4":
            try:
                item_id = int(input("Enter Item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid input. Please enter a valid Item ID.")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
