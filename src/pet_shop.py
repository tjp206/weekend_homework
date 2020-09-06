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
    for pet in pet_shop['pets']:        # for lists
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

def customer_can_afford_pet(customers, new_pet):
    if customers['cash'] >= new_pet['price']:
        return True
    # elif customers['cash'] < new_pet['price']:
    #     return False
    # elif customers['cash'] == new_pet['price']:
    #     return True
    else: 
        return False

def sell_pet_to_customer(pet_shop, new_pet, customers):
    #Check customer can afford pet
    #If True add pet to customer
    #Then add to pet_shop sold count
    #Deduct cost of pet from customer
    #Add cost of pet to pet shop total cash
    if customer_can_afford_pet(customers, new_pet):
        add_pet_to_customer(customers, new_pet)
        increase_pets_sold(pet_shop, 1)
        remove_customer_cash(customers, new_pet['price'])
        add_or_remove_cash(pet_shop, new_pet['price'])
        # Everything runs until here - WHY TJ?! WHY?!?!
    # elif find_pet_by_name(pet_shop['pets']['name']):
    #     add_pet_to_customer(customers, new_pet)
    #     increase_pets_sold(pet_shop, 0)
    #     remove_customer_cash(customers, new_pet['price'])
    #     add_or_remove_cash(pet_shop, new_pet['price'])
    else:
        return False

