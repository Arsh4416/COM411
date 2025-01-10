from process import DataProcessor
from tui import UserInterface
from visual import Visualizer
from exporter import DataExporter
from logger import Logger

class DisneylandReviewAnalyser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.processor = DataProcessor(file_path)
        self.ui = UserInterface()
        self.visualizer = Visualizer()
        self.exporter = DataExporter()
        self.logger = Logger("application.log")
        self.is_running = True

    def start(self):
        self.ui.display_title("Disneyland Review Analyser")
        self.logger.log("Program started.")

        # Load dataset
        rows = self.processor.load_data()
        if rows > 0:
            self.ui.display_message(f"Dataset loaded successfully. Total rows: {rows}.")
        else:
            self.ui.display_message("Failed to load dataset. Exiting.")
            self.logger.log("Dataset loading failed.")
            return

        # Main menu loop
        while self.is_running:
            choice = self.ui.display_main_menu()
            self.handle_menu_choice(choice)

    def handle_menu_choice(self, choice):
        if choice == '1':
            self.ui.confirm_choice("View Data")
            self.view_data()
        elif choice == '2':
            self.ui.confirm_choice("Visualize Data")
            self.visualize_data()
        elif choice == '3':
            self.ui.confirm_choice("Export Data")
            self.export_data()
        elif choice == '4':
            self.ui.confirm_choice("Exit")
            self.is_running = False
            self.logger.log("Program exited.")
        else:
            self.ui.invalid_choice()

    def view_data(self):
        sub_choice = self.ui.display_view_data_menu()
        if sub_choice == 'A':
            park_name = input("Enter the park name: ")
            reviews = self.processor.filter_reviews_by_park(park_name)
            self.ui.display_reviews(reviews)
        elif sub_choice == 'B':
            park_name = input("Enter the park name: ")
            location = input("Enter the reviewer location: ")
            count = self.processor.count_reviews_by_location(park_name, location)
            self.ui.display_message(f"Number of reviews: {count}")
        else:
            self.ui.invalid_choice()

    def visualize_data(self):
        sub_choice = self.ui.display_visualization_menu()
        if sub_choice == 'A':
            data = self.processor.aggregate_reviews_by_park()
            self.visualizer.plot_pie_chart(data, "Most Reviewed Parks")
        elif sub_choice == 'B':
            park_name = input("Enter the park name: ")
            data = self.processor.aggregate_reviews_by_location(park_name)
            self.visualizer.plot_bar_chart(data, "Park Reviews by Location", "Locations", "Reviews")
        else:
            self.ui.invalid_choice()

    def export_data(self):
        format_choice = self.ui.display_export_options()
        if format_choice == '1':
            self.exporter.export_to_txt(self.processor.aggregate_data(), "exported_data.txt")
            self.ui.display_message("Data exported to TXT.")
        elif format_choice == '2':
            self.exporter.export_to_csv(self.processor.aggregate_data(), "exported_data.csv")
            self.ui.display_message("Data exported to CSV.")
        elif format_choice == '3':
            self.exporter.export_to_json(self.processor.aggregate_data(), "exported_data.json")
            self.ui.display_message("Data exported to JSON.")
        else:
            self.ui.invalid_choice()

if __name__ == "__main__":
    analyser = DisneylandReviewAnalyser("Disneyland_reviews.csv")
    analyser.start()
