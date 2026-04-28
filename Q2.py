import time
from datetime import datetime
class Transaction:
    def __init__(self,transaction_id,customer_name,product_name,amount,transaction_date):
        self.transactionID = transaction_id
        self.customerName = customer_name
        self.productName = product_name
        self.amount = amount
        self.transactionDate = transaction_date

    def __str__(self):
        return f"{self.transactionID} | {self.customerName} | {self.productName} | {self.amount} | {self.transactionDate}"

merge_call_count = 0
def merge_sort(arr):
    global merge_call_count
    merge_call_count += 1

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid]) #recursive left
    right = merge_sort(arr[mid:]) #recursive right
    return merge(left,right)

def merge(left,right):
    sorted_list = []
    i = 0
    j = 0

    #comparing then merge
    while i < len(left) and j < len(right):
        if left[i].transactionID <= right[j].transactionID:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1

    #appending remaining items
    sorted_list.extend(left[i:])
    sorted_list.extend((right[j:]))
    return sorted_list

def binary_search(arr,target_id,low,high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid].transactionID == target_id:
        return mid
    elif arr[mid].transactionID > target_id:
        return binary_search(arr, target_id, low, mid - 1)
    else:
        return binary_search(arr, target_id, mid + 1, high)

def linear_search(arr,target_id):
    for i in range(len(arr)):
        if arr[i].transactionID == target_id:
            return i
    return -1

def display_transaction(arr):
    for i in arr:
        print(i)

#test
transactions = [
    Transaction(105, "Ali", "Mouse", 45.00, "2026-04-01"),
    Transaction(101, "Siti", "Keyboard", 120.00, "2026-04-02"),
    Transaction(110, "John", "Monitor", 800.00, "2026-04-03"),
    Transaction(103, "Amin", "Laptop", 3500.00, "2026-04-04"),
    Transaction(108, "Lisa", "USB Cable", 15.00, "2026-04-05"),
    Transaction(102, "Daniel", "Phone", 2000.00, "2026-04-06"),
    Transaction(107, "Sarah", "Headset", 150.00, "2026-04-07"),
    Transaction(104, "Kumar", "Tablet", 900.00, "2026-04-08"),
    Transaction(109, "Mei", "Charger", 60.00, "2026-04-09"),
    Transaction(106, "Farah", "SSD", 400.00, "2026-04-10")
]

sorted_transaction = transactions[:] #copy original list

def main():
    global sorted_transaction
    # Example test cases
    print("\nTest Existing ID (101):")
    print(binary_search(sorted_transaction, 101, 0, len(sorted_transaction) - 1))

    print("\nTest Non-Existing ID (999):")
    print(binary_search(sorted_transaction, 999, 0, len(sorted_transaction) - 1))
    while True:
        print("\n===== TRANSACTION SYSTEM MENU =====")
        print("1. Display all transactions")
        print("2. Sort transactions (Merge Sort)")
        print("3. Search transaction (Binary Search)")
        print("4. Search transaction (Linear Search)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n--- TRANSACTIONS ---")
            display_transaction(sorted_transaction)

        elif choice == "2":
            print("\nBefore Sorting:")
            display_transaction(sorted_transaction)

            start = time.time()
            global merge_call_count
            merge_call_count = 0
            sorted_transaction = merge_sort(sorted_transaction)
            end = time.time()

            print("\nAfter Sorting (by Transaction ID):")
            display_transaction(sorted_transaction)

            print(f"\nMerge Sort Time: {end - start:.6f} seconds")
            print(f"Recursive Calls: {merge_call_count}")

        elif choice == "3":
            if sorted_transaction != sorted(transactions, key=lambda x: x.transactionID):
                print("\n Please sort data first using Merge Sort.")
                continue

            target = int(input("Enter Transaction ID to search: "))

            start = time.time()
            result = binary_search(sorted_transaction, target, 0, len(sorted_transaction) - 1)
            end = time.time()

            if result != -1:
                print("\n Transaction Found:")
                print(sorted_transaction[result])
            else:
                print("\n Transaction NOT found")

            print(f"Binary Search Time: {end - start:.6f} seconds")

        elif choice == "4":
            target = int(input("Enter Transaction ID to search: "))

            start = time.time()
            result = linear_search(sorted_transaction, target)
            end = time.time()

            if result != -1:
                print("\n Transaction Found:")
                print(sorted_transaction[result])
            else:
                print("\n Transaction NOT found")

            print(f"Linear Search Time: {end - start:.6f} seconds")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")



if __name__ == '__main__':
    main()



















































