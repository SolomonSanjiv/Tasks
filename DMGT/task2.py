import pandas as pd
data = {
    "CustomerID": [1, 2, 3],
    "Name": ["John", "Jane", "Michael"],
    "PhoneNumbers": ["555-1234, 555-5678", "555-9876", "555-5555"]
}
def convert_to_1nf(data):
    rows = []
    for index, row in data.iterrows():
        phone_numbers = row["PhoneNumbers"].split(", ")
        for phone in phone_numbers:
            rows.append({"CustomerID": row["CustomerID"], "Name": row["Name"], "PhoneNumber": phone})
    return pd.DataFrame(rows)
df = pd.DataFrame(data)
df_1nf = convert_to_1nf(df)
def convert_to_2nf(data):
    customers = data[["CustomerID", "Name"]].drop_duplicates()
    phone_numbers = data[["CustomerID", "PhoneNumber"]]
    return customers, phone_numbers
customers_2nf, phone_numbers_2nf = convert_to_2nf(df_1nf)
def convert_to_3nf(customers):
    return customers
customers_3nf = convert_to_3nf(customers_2nf)
print("Original Data:")
print(df)
print("\nFirst Normal Form (1NF):")
print(df_1nf)
print("\nSecond Normal Form (2NF) - Customers Table:")
print(customers_2nf)
print("\nSecond Normal Form (2NF) - Phone Numbers Table:")
print(phone_numbers_2nf)
print("\nThird Normal Form (3NF):")
print(customers_3nf)
