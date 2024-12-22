print("OE:2")
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ₱{self.price}"

    def update_price(self, new_price):
        self.price = new_price

    def update_model(self, new_model):
        self.model = new_model

    def update_brand(self, new_brand):
        self.brand = new_brand


def display_phones(phone_list):
    if not phone_list:
        print("No phones available.")
    else:
        for i, phone in enumerate(phone_list, 1):
            print(f"{i}. {phone}")


def main():
    phone_list = []
    while True:
        print("\n--- Mobile Phone Menu ---")
        print("1. Add a new phone")
        print("2. Modify a phone")
        print("3. Delete a phone")
        print("4. Display all phones")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            brand = input("Enter phone brand: ")
            model = input("Enter phone model: ")
            price = float(input("Enter phone price in Pesos: ₱"))
            new_phone = Phone(brand, model, price)
            phone_list.append(new_phone)
            print("Phone added successfully.")

        elif choice == "2":
            display_phones(phone_list)
            if phone_list:
                phone_index = int(input("Enter the phone number to modify: ")) - 1
                if 0 <= phone_index < len(phone_list):
                    phone = phone_list[phone_index]
                    print("\nModify phone:")
                    print(f"1. Update price (₱{phone.price})")
                    print(f"2. Update model ({phone.model})")
                    print(f"3. Update brand ({phone.brand})")
                    mod_choice = input("Choose an option: ")

                    if mod_choice == "1":
                        new_price = float(input("Enter new price in Pesos: ₱"))
                        phone.update_price(new_price)
                    elif mod_choice == "2":
                        new_model = input("Enter new model: ")
                        phone.update_model(new_model)
                    elif mod_choice == "3":
                        new_brand = input("Enter new brand: ")
                        phone.update_brand(new_brand)
                    else:
                        print("Invalid option.")
                else:
                    print("Invalid phone number.")
            else:
                print("No phones to modify.")

        elif choice == "3":
            display_phones(phone_list)
            if phone_list:
                phone_index = int(input("Enter the phone number to delete: ")) - 1
                if 0 <= phone_index < len(phone_list):
                    del phone_list[phone_index]
                    print("Phone deleted successfully.")
                else:
                    print("Invalid phone number.")
            else:
                print("No phones to delete.")

        elif choice == "4":
            display_phones(phone_list)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
