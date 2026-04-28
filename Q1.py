import time

class Products:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    """Using modulus to store value"""
    def hash_function(self, key):
        return key % self.size

    def insert(self, key, product):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            index = (index + 1) % self.size #linear probing

            if index == start:
                print("Hash Table is Full")
                return

        self.table[index] = (key, product)

    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size

            if index == start:
                break

        return None

    def display(self):
        for i, item in enumerate(self.table):
            if item is not None:
                key, product = item
                print(f"Index {i}: {product.name} (ID:{key})")
            else:
                print(f"Index {i}: Empty")


def array_search(arr, key):
    for product in arr:
        if product.product_id == key:
            return product
    return None


def performance_test(ht, arr):
    start = time.time()
    for _ in range(1000):
        ht.search(102)
    end = time.time()
    print("Hash Table Search Time:", end - start)

    start = time.time()
    for _ in range(1000):
        array_search(arr, 102)
    end = time.time()
    print("Array Search Time:", end - start)


def main():
    ht = HashTable(10)
    arr = []

    p1 = Products(101, "Panadol", "Tablet", 5.5, 100)
    p2 = Products(102, "Cough Syrup", "Syrup", 8.0, 50)
    p3 = Products(103, "Vitamin C", "Supplement", 12.0, 30)

    ht.insert(p1.product_id, p1)
    ht.insert(p2.product_id, p2)
    ht.insert(p3.product_id, p3)

    arr.append(p1)
    arr.append(p2)
    arr.append(p3)

    while True:
        print("\n=== Pharmacy Inventory System ===")
        print("1. Display Products")
        print("2. Insert Product")
        print("3. Search Product")
        print("4. Performance Test")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == '1':
            ht.display()

        elif choice == '2':
            pid = int(input("Enter product ID: "))
            name = input("Enter product Name: ")
            cate = input("Enter category Name: ")
            price = float(input("Enter Product Price: "))
            quan = int(input("Enter Quantity: "))

            p = Products(pid, name, cate, price, quan)

            ht.insert(pid, p)
            arr.append(p)

        elif choice == '3':
            pid = int(input("Enter Product ID: "))
            result = ht.search(pid)

            if result:
                print(f"Found: {result.name}, Price: {result.price}, Quantity: {result.quantity}")
            else:
                print("Product Not Found")

        elif choice == '4':
            performance_test(ht, arr)

        elif choice == '5':
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()