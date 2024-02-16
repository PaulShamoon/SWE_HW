import random
import string

def generate_random_username():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

def generate_random_password():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

def generate_random_birthdate():
    return f"{random.randint(1, 12)}/{random.randint(1, 28)}/{random.randint(1950, 2000)}"

def generate_random_address():
    streets = ['Elm Street', 'Maple Street', 'Oak Street', 'Main Street']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
    states = ['NY', 'CA', 'IL', 'TX']
    return f"{random.randint(1, 999)} {random.choice(streets)}, {random.choice(cities)}, {random.choice(states)}"

def generate_random_social_security_number():
    return ''.join(random.choice(string.digits) for _ in range(9))

def generate_sample_data(num_users):
    sample_data = {}
    for i in range(num_users):
        user_id = f"user_{i+1}"
        user = {
            'username': generate_random_username(),
            'password': generate_random_password(),
            'birthdate': generate_random_birthdate(),
            'address': generate_random_address(),
            'social_security_number': generate_random_social_security_number(),
            'product_purchased': random.choice(['Product A', 'Product B', 'Product C']),
            'salesperson': ''.join(random.choice(string.ascii_uppercase) for _ in range(6))  # Assuming salesperson code is 6 characters
        }
        sample_data[user_id] = user
    return sample_data

def search_by_state(data, state):
    users_in_state = []
    for user_id, user_data in data.items():
        if user_data['address'].split(", ")[-1] == state:
            users_in_state.append((user_id, user_data))
    return users_in_state

def search_by_salesperson(data, salesperson):
    users_handled_by_salesperson = []
    for user_id, user_data in data.items():
        if user_data['salesperson'] == salesperson:
            users_handled_by_salesperson.append((user_id, user_data))
    return users_handled_by_salesperson

def print_search_results(results):
    if not results:
        print("No matching users found.")
    else:
        for user_id, user_data in results:
            print(f"User ID: {user_id}")
            print(user_data)
            print()

# Generate 10 sample user records with unique IDs
sample_data = generate_sample_data(10)

# Prompt the user for what they want to search
search_criteria = input("Enter 'state' to search for users in a certain state or 'salesperson' to search for users handled by a certain salesperson: ").lower()

if search_criteria == 'state':
    state = input("Enter the state to search for (e.g., TX): ")
    state_search_results = search_by_state(sample_data, state)
    print("Users in", state.upper() + ":")
    print_search_results(state_search_results)
elif search_criteria == 'salesperson':
    salesperson = input("Enter the salesperson code to search for (e.g., ABCDEF): ")
    salesperson_search_results = search_by_salesperson(sample_data, salesperson)
    print("Users handled by salesperson", salesperson.upper() + ":")
    print_search_results(salesperson_search_results)
else:
    print("Invalid search criteria. Please enter 'state' or 'salesperson'.")
