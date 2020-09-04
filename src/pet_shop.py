# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    if (pet_shop['name']):
        return (pet_shop['name'])

def get_total_cash(pet_shop):
    if (pet_shop['admin']['total_cash']):
        return (pet_shop['admin']['total_cash'])
    
def add_or_remove_cash(pet_shop, amount):
    cash = get_total_cash(pet_shop)
    pet_shop['admin']['total_cash'] = cash + amount
    return pet_shop['admin']['total_cash']
    
def get_pets_sold(pet_shop):
    return (pet_shop['admin']['pets_sold'])

def increase_pets_sold(pet_shop, amount):
    pet_shop['admin']['pets_sold'] += amount
    
def get_stock_count(pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, breed_name):
    list_of_breeds = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed_name:
            list_of_breeds.append(pet_shop['pets'])
    return list_of_breeds
    
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop['pets']:        # for lists use for loop
        if pet['name'] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    new_pet = find_pet_by_name(pet_shop, pet_name)
    remove_pet = pet_shop['pets'].remove(new_pet)
    return remove_pet
        
def add_pet_to_stock(pet_shop, pet_name):
    pet_shop['pets'].append(pet_name)      # for dict 
    new_pets = get_stock_count(pet_shop)
    return new_pets

def get_customer_cash(customers):
    return customers['cash']

def remove_customer_cash(customers, amount):
    customers['cash'] -= amount

def get_customer_pet_count(customers):
    return len(customers['pets'])

def add_pet_to_customer(customers, new_pet):
    customers['pets'].append(new_pet)
    pet_counter = get_customer_pet_count(customers)
    return pet_counter


