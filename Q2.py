import time
from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transactionID = transaction_id
        self.customerName = customer_name
        self.productName = product_name
        self.amount = amount
        self.transactionDate = transaction_date

    def __str__(self):
        return f"{self.transactionID:<5} | {self.customerName:<10} | {self.productName:<10} | {self.amount:<8.2f} | {self.transactionDate}"


merge_call_count = 0


def merge_sort(arr, attr="transactionID"):
    global merge_call_count
    merge_call_count += 1

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], attr)
    right = merge_sort(arr[mid:], attr)
    return merge(left, right, attr)


def merge(left, right, attr):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if getattr(left[i], attr) <= getattr(right[j], attr):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def binary_search(arr, target_id, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid].transactionID == target_id:
        return mid
    elif arr[mid].transactionID > target_id:
        return binary_search(arr, target_id, low, mid - 1)
    else:
        return binary_search(arr, target_id, mid + 1, high)


def linear_search(arr, target_id):
    for i in range(len(arr)):
        if arr[i].transactionID == target_id:
            return i
    return -1


def main():
    transactions = [
        Transaction(105, "Ali", "Mouse", 45.00, "2026-04-01"),
        Transaction(101, "Siti", "Keyboard", 120.00, "2026-04-02"),
        Transaction(110, "John", "Monitor", 800.00, "2026-04-03"),
        Transaction(103, "Amin", "Laptop", 3500.00, "2026-04-04"),
        Transaction(108, "Lisa", "USB Cable", 15.00, "2026-04-05")
    ]

    # Initial sort so binary search works immediately
    sorted_transaction = merge_sort(transactions, "transactionID")
    current_sort_attr = "transactionID"

    while True:
        print("\n===== TRANSACTION SYSTEM MENU =====")
        print("1. Display all transactions")
        print("2. Sort transactions")
        print("3. Search by ID (Binary Search - Requires ID Sort)")
        print("4. Search by ID (Linear Search - Any order)")
        print("5. Add New Transaction")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print(f"\n{'ID':<5} | {'Customer':<10} | {'Product':<10} | {'Amount':<8} | {'Date'}")
            print("-" * 60)
            for t in sorted_transaction:
                print(t)

        elif choice == "2":
            print("\nSort by: (1) Transaction ID (2) Amount")
            sort_choice = input("Choice: ")
            current_sort_attr = "amount" if sort_choice == "2" else "transactionID"

            global merge_call_count
            merge_call_count = 0
            start = time.time()
            sorted_transaction = merge_sort(sorted_transaction, current_sort_attr)
            end = time.time()

            print(f"\nSorted successfully by {current_sort_attr}!")
            print(f"Time: {end - start:.6f}s | Recursive Calls: {merge_call_count}")

        elif choice == "3":
            # BUG FIX: Check if we are currently sorted by ID
            if current_sort_attr != "transactionID":
                print("! Warning: List was sorted by Amount. Re-sorting by ID for Binary Search...")
                sorted_transaction = merge_sort(sorted_transaction, "transactionID")
                current_sort_attr = "transactionID"

            try:
                target = int(input("Enter Transaction ID to Binary Search: "))
                start = time.time()
                result = binary_search(sorted_transaction, target, 0, len(sorted_transaction) - 1)

                if result != -1:
                    print(f"Found: {sorted_transaction[result]}")
                else:
                    print("Transaction ID not found.")
                print(f"Search Time: {time.time() - start:.6f}s")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "4":
            try:
                target = int(input("Enter Transaction ID to Linear Search: "))
                start = time.time()
                result = linear_search(sorted_transaction, target)
                print(f"Found: {sorted_transaction[result]}" if result != -1 else "Not Found")
                print(f"Search Time: {time.time() - start:.6f}s")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "5":
            try:
                tid = int(input("ID: "))
                name = input("Customer: ")
                prod = input("Product: ")
                amt = float(input("Amount: "))
                date = datetime.now().strftime("%Y-%m-%d")
                new_t = Transaction(tid, name, prod, amt, date)

                sorted_transaction.append(new_t)
                # Re-sort to maintain order after adding
                sorted_transaction = merge_sort(sorted_transaction, current_sort_attr)
                print("Transaction added and list re-sorted.")
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == "6":
            print("Exiting...")
            break


if __name__ == '__main__':
    main()