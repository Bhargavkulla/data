import csv

users = [
    {"name": "juhi", "age": 22, "city": "blr"},
    {"name": "abc", "age": 22, "city": "bihar"}
]

try:
    with open("users.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "age", "city"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)
    print("Successfully wrote to 'users.csv'")

except IOError as e:
    print(f"Error writing to CSV file: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
