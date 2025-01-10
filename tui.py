class UserInterface:
    @staticmethod
    def display_title(title):
        """Displays the program title with dashes."""
        dashes = "-" * len(title)
        print(dashes)
        print(title)
        print(dashes)

    @staticmethod
    def display_main_menu():
        """Displays the main menu and returns the user's choice."""
        print("\nMain Menu:")
        print("1. View Data")
        print("2. Visualize Data")
        print("3. Export Data")
        print("4. Exit")
        return input("Please select an option (1-4): ").strip()

    @staticmethod
    def display_view_data_menu():
        """Displays the View Data submenu and returns the user's choice."""
        print("\nView Data Menu:")
        print("A. View Reviews by Park")
        print("B. Count Reviews by Park and Location")
        return input("Please select an option (A-B): ").strip().upper()

    @staticmethod
    def display_visualization_menu():
        """Displays the Visualize Data submenu and returns the user's choice."""
        print("\nVisualization Menu:")
        print("A. Pie Chart of Reviews by Park")
        print("B. Bar Chart of Reviews by Location")
        print("C. Line Chart of Review Trends Over Time")
        print("D. Heatmap of Review Distributions")
        return input("Please select an option (A-D): ").strip().upper()

    @staticmethod
    def display_export_options():
        """Displays the Export Data options and returns the user's choice."""
        print("\nExport Options:")
        print("1. Export to TXT")
        print("2. Export to CSV")
        print("3. Export to JSON")
        return input("Please select an option (1-3): ").strip()

    @staticmethod
    def confirm_choice(choice):
        """Confirms the user's menu choice."""
        print(f"You selected: {choice}")

    @staticmethod
    def invalid_choice():
        """Informs the user about an invalid choice."""
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_message(message):
        """Displays a generic message to the user."""
        print(message)

    @staticmethod
    def display_reviews(reviews):
        """Displays a list of reviews."""
        if not reviews:
            print("No reviews found.")
        else:
            for review in reviews:
                print(review)

    @staticmethod
    def display_summary(summary):
        """Displays a summary of aggregated data."""
        for key, value in summary.items():
            print(f"{key}: {value}")