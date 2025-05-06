'''
Problem
Write a function taking an ID, and list of transactions.
Return a list with only THOSE transactions

    Input:
        - 1st argument: ID integer
        - 2nd argument: a list of transactions (a dictionary)

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

Data Structures
Accessing dictionaries




Algorithm

1. given "transactions", "ID" as inputs to function
2. Initialize "result" to an empty list
3. Iterating through each "transaction" in "transactions" parameter:
    - if the ID matches value in "transaction" --> "ID"
        - append to "result
4. return "result
C

# '''
# def transactions_for(id, transactions_dict):
#     result = []
#     for idx in range(len(transactions_dict)):
#         if transactions_dict[idx]["id"] == id:
#             result.append(transactions_dict[idx])
    
#     return result

# def transactions_for(id, transactions_dict):
#     return [transactions_dict[idx] for idx in range(len(transactions_dict))
#             if transactions_dict[idx]["id"] == id
#     ]

def transactions_for(inventory_item, all_transactions):
    return [transaction for transaction in all_transactions
            if transaction["id"] == inventory_item]


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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True