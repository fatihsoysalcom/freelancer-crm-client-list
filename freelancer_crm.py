import json

class FreelancerCRM:
    def __init__(self, data_file='clients.json'):
        self.data_file = data_file
        self.clients = self.load_clients()

    def load_clients(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_clients(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.clients, f, indent=4, ensure_ascii=False)

    def add_client(self, name, email, phone=None, notes=''):
        client_id = len(self.clients) + 1
        new_client = {
            'id': client_id,
            'name': name,
            'email': email,
            'phone': phone,
            'notes': notes
        }
        self.clients.append(new_client)
        self.save_clients()
        print(f"Client '{name}' added successfully.")

    def list_clients(self):
        if not self.clients:
            print("No clients found.")
            return
        print("\n--- Client List ---")
        for client in self.clients:
            print(f"ID: {client['id']}, Name: {client['name']}, Email: {client['email']}")
            if client['phone']:
                print(f"    Phone: {client['phone']}")
            if client['notes']:
                print(f"    Notes: {client['notes']}")
        print("-------------------")

    def find_client_by_name(self, name):
        found = [c for c in self.clients if name.lower() in c['name'].lower()]
        if not found:
            print(f"No clients found matching '{name}'.")
            return None
        return found

    def update_client_notes(self, client_id, new_notes):
        for client in self.clients:
            if client['id'] == client_id:
                client['notes'] = new_notes
                self.save_clients()
                print(f"Notes for client ID {client_id} updated.")
                return
        print(f"Client with ID {client_id} not found.")

# --- Example Usage ---
if __name__ == "__main__":
    crm = FreelancerCRM()

    # Add some initial clients if the file is empty
    if not crm.clients:
        crm.add_client("Alice Smith", "alice.smith@example.com", "+1234567890", "Project X started last month.")
        crm.add_client("Bob Johnson", "bob.j@company.com")
        crm.add_client("Charlie Brown", "charlie@mail.net", notes="Interested in new services.")

    # Demonstrate functionalities
    crm.list_clients()

    # Find a client
    search_results = crm.find_client_by_name("Alice")
    if search_results:
        print(f"\nFound: {search_results[0]['name']} ({search_results[0]['email']})")

    # Update notes for a client (assuming Alice has ID 1)
    crm.update_client_notes(1, "Followed up on invoice. Project X is on track.")

    # List clients again to see the update
    crm.list_clients()
