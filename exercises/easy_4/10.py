'''
Problem
Return True or False based on whether an inventory item is available

Rules:
    - Explicit:
        - An item is available, if SUM of ALL its "quantity" is greater than 0
        - An item gains/loses "quantity" from moving "in"/"out"

Examples

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True

Data Structures

- Create a list based on all transactions for an inventory_item
- Going through list elements, add or minus the "quantity' figure, based
on "movement" status

Algorithm

1. Given "inventory_item", "transaction_lst" as inputs
2. Initialize "item_qty" to 0
3. Create a list of relevant items using "transactions_for" function
- name this "item_transactions"
4. Iterating through each dict in "item_transactions": add to "item_qty"
    A. If "movement" is "in": add the relevant "quantity"
    B. If "movement" is "out": subtract the relevant "quantity"
5. Return result of checking if "item_qty" is greater than 0

Code
'''

def transactions_for(inventory_item, all_transactions): 
    return [transaction for transaction in all_transactions
            if transaction["id"] == inventory_item]

def is_item_available(inventory_item, transactions_lst):
    relevant_transactions = transactions_for(inventory_item, transactions_lst)
    item_qty = 0

    for transaction in relevant_transactions:
        if transaction["movement"] == 'in':
            item_qty += transaction['quantity']
        else:
            item_qty -= transaction['quantity']

    return item_qty > 0

        

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True

