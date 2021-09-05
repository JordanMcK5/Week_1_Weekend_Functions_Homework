# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_name):
    return pet_shop_name ["name"]

def get_total_cash(total_cash):
    return total_cash ["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_cash, new_cash_amount):
     pet_shop_cash["admin"]["total_cash"] += new_cash_amount

def add_or_remove_cash(pet_shop_cash, new_cash_amount_2):
     pet_shop_cash["admin"]["total_cash"] += new_cash_amount_2

def get_pets_sold(total_pets_sold):
    return total_pets_sold ["admin"]["pets_sold"]

def increase_pets_sold(total_pets_sold, new_pets_sold_amount):
     total_pets_sold["admin"]["pets_sold"] += new_pets_sold_amount

def get_stock_count(stock_in_shop):
    return len(stock_in_shop["pets"])

def test_increase_pets_sold(pets_sold, new_sold_amount):
     pets_sold["admin"]["pets_sold"] += new_sold_amount   

def get_pets_by_breed(pet_shop, pets_by_breed):
    return pets_by_breed ["pets"]["breed"]

def get_pets_by_breed( pet_shop, pets_by_breed):
    breeds_found = []
    for pets in pet_shop["pets"]:
        if pets["breed"] == pets_by_breed:
            breeds_found.append(pets)
    return breeds_found

def get_pets_by_breed( pet_shop, pets_by_breed):
    breeds_found = []
    for pets in pet_shop["pets"]:
        if pets["breed"] == pets_by_breed:
            breeds_found.append(pets)
    return breeds_found

def get_pets_by_breed( pet_shop, pets_by_breed):
    breeds_found = []
    for pets in pet_shop["pets"]:
        if pets["breed"] == pets_by_breed:
            breeds_found.append(pets)
    return breeds_found

def find_pet_by_name( pet_shop, pets_by_name):
    pet_names_found = []
    for pets_names in pet_shop["pets"]:
        if pets_names["name"] == pets_by_name:
            pet_names_found.append(pets_names)
    return pet_names_found

def find_pet_by_name( pet_shop, pets_by_name):
    pet_names_found = None
    for pets_names in pet_shop["pets"]:
        if pets_names["name"] == pets_by_name:
            pet_names_found = pets_names
    return pet_names_found

def remove_pet_by_name( pet_shop, pets_by_name):
    for pets in pet_shop["pets"]:
        if pets ["name"] == pets_by_name:
            pet_shop["pets"].remove(pets)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer_cash):
    return customer_cash ["cash"]

def remove_customer_cash( pet_shop_customer, customer_cash):
    pet_shop_customer["cash"] -= customer_cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, customer_pet):
    customer["pets"].append(customer_pet)

# EXTENSIONS

def customer_can_afford_pet(customer, pets):
    if customer["cash"] >= pets["price"]:
        return True
    else:
        return False
