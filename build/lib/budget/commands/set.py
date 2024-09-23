# commands/set.py

# A global variable to store the base amount
base_amount = None

def set_base_amount(amount):
    global base_amount
    base_amount = amount
    print(f"Monthly base set to: ${base_amount:.2f}")

    