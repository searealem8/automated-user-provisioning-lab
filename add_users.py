import csv

def create_users_from_csv(csv_file):
    try:
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
        for row in reader:
                full_name = row['Full Name']
                email = row['Email']
                department = row['Department']
                username = full_name.lower().replace(" ", ".")
                print(f"Creating user: {full_name}")
                print(f"Username: {username}")
                print(f"Email: {email}")
                print(f"Department: {department}")
                print("-" * 30)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")

# Simulate running script
if __name__ == "__main__":
    create_users_from_csv("users.csv")
