class Category:
    def __init__(self):
        self.category_name = input("Enter the category name: ")

    def show_category_name(self):
        print(f"Category name: {self.category_name}")

class Product(Category):
    def __init__(self):
        Category.__init__(self)
        self.product_name = input("Enter product name: ")
        self.price = int(input("Enter product price: "))
        self.quantity = int(input("Enter product quantity: "))

    def show_product_info(self):
        Category.show_category_name(self)
        print(f"Product name: {self.product_name}")
        print(f"Product price: {self.price}")
        print(f"Product quantity: {self.quantity}")

    def total_price(self):
        print(f"Total price : {self.price * self.quantity}")

p = Product()
print("\n")
p.show_product_info()
print("\n")
p.total_price()
