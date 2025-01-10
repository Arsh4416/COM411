class Authentication:
    def __init__(self):
        self.users = {
            "admin": "password123",
            "user1": "user1pass",
            "user2": "user2pass"
        }

    def authenticate_user(self, username, password):
        """Authenticates a user based on username and password."""
        if username in self.users and self.users[username] == password:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Invalid username or password.")
            return False

    def add_user(self, username, password):
        """Adds a new user to the system."""
        if username in self.users:
            print("User already exists.")
        else:
            self.users[username] = password
            print("User added successfully.")

    def remove_user(self, username):
        """Removes an existing user from the system."""
        if username in self.users:
            del self.users[username]
            print("User removed successfully.")
        else:
            print("User does not exist.")
