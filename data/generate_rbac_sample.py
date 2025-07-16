import random
import json

# Configuration
NUM_USERS = 50
NUM_PERMISSIONS = 30
NUM_ROLES = 10
MAX_PERMISSIONS_PER_ROLE = 6
MAX_ROLES_PER_USER = 3

def generate_permissions():
    return [f"perm_{i+1}" for i in range(NUM_PERMISSIONS)]

def generate_users():
    return [f"user_{i+1}" for i in range(NUM_USERS)]

def generate_roles(permissions):
    roles = {}
    for i in range(NUM_ROLES):
        role_name = f"role_{i+1}"
        perm_subset = random.sample(permissions, random.randint(1, MAX_PERMISSIONS_PER_ROLE))
        roles[role_name] = perm_subset
    return roles

def assign_roles_to_users(users, roles):
    user_roles = {}
    for user in users:
        role_subset = random.sample(list(roles.keys()), random.randint(1, MAX_ROLES_PER_USER))
        user_roles[user] = role_subset
    return user_roles

def derive_user_permissions(user_roles, roles):
    user_permissions = {}
    for user, assigned_roles in user_roles.items():
        perms = set()
        for role in assigned_roles:
            perms.update(roles[role])
        user_permissions[user] = list(perms)
    return user_permissions

def main():
    users = generate_users()
    permissions = generate_permissions()
    roles = generate_roles(permissions)
    user_roles = assign_roles_to_users(users, roles)
    user_permissions = derive_user_permissions(user_roles, roles)

    # Save to JSON files
    with open("users.json", "w") as f:
        json.dump(users, f, indent=2)
    with open("permissions.json", "w") as f:
        json.dump(permissions, f, indent=2)
    with open("roles.json", "w") as f:
        json.dump(roles, f, indent=2)
    with open("user_roles.json", "w") as f:
        json.dump(user_roles, f, indent=2)
    with open("user_permissions.json", "w") as f:
        json.dump(user_permissions, f, indent=2)

    print("Sample RBAC data generated successfully.")

if __name__ == "__main__":
    main()
