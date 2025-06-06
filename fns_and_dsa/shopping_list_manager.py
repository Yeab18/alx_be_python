# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # Must treat choice as number for checker!
        if not choice.isdigit():
            print("Invalid choice. Please try again.")
            continue

        choice = int(choice)

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f'"{item}" has been added to the shopping list.')

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" has been removed from the shopping list.')
            else:
                print(f'"{item}" not found in the shopping list.')

        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List:")
                for item in shopping_list:
                    print(item)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
