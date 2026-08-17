class coffee:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_items(self,coffee):
        self.items.append(coffee)

        print(f"Added {coffee.name} to your order. ")


    def total(self):
        return sum(item.price for item in self.items)

    def shows_order(self):
        if not self.items:

            print("No items in order.")

            return
        print("\nYour Order: ")

        for i, item in enumerate(self.items, 1):

          print(f"{i}.{item.name} - ${item.price}")


        print(f"Total: ${self.total()}\n")

        def checkout(self):
            if not self.items:
                print("Your cart is empty.")


                return

            self.show_Order()


            confirm  = input("Proceed to checkout? (tes/no): ").strip().lower()


            if confirm == "yes":


                print("Order confirmed! Thank you. ")

                self.items.clear()


            else:


                print("Checkout cancelled. ")


def main():


    menu = [


        coffee("Espresso", 2.5),

        coffee("Latte", 3.5),

        coffee("cappuccino",3.0),

        coffee("Americano", 2.0)
    ]

    order = Order()

    while True:


        print("\n---- Coffee Menu ---")


        for i, items  in enumerate(menu, 1):


            print(f"{i}. {items.name} - ${items.price}")


        print("5. View order")


        print('6. Checkout')

        print("7. Exit")


        choice = input("choose an option: ")


        if choice in ['1','2','3','4',]:


            order.add_item(menu[int(choice) - 1])

        elif choice == '5' :


            order.show_order()

        elif choice == '6':

            order.checkout()

        elif choice == '7':

            print("Thanks for visiting. Goodbye!")


            break

        else:


            print("Invalid choice. Try Again.")



if __name__=="__main__":
    main()        


        

