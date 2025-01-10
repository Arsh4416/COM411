import csv
import json

class DataExporter:
    @staticmethod
    def export_to_txt(data, file_path):
        """Exports aggregated data to a TXT file."""
        try:
            with open(file_path, 'w') as file:
                for park, details in data.items():
                    file.write(f"{park}:\n")
                    for key, value in details.items():
                        file.write(f"  {key}: {value}\n")
                    file.write("\n")
            print(f"Data successfully exported to {file_path}.")
        except Exception as e:
            print(f"Error exporting to TXT: {e}")

    @staticmethod
    def export_to_csv(data, file_path):
        """Exports aggregated data to a CSV file."""
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Park", "Total Reviews", "Positive Reviews", "Average Rating", "Countries"])
                for park, details in data.items():
                    writer.writerow([
                        park,
                        details['total_reviews'],
                        details['positive_reviews'],
                        details['average_rating'],
                        details['countries']
                    ])
            print(f"Data successfully exported to {file_path}.")
        except Exception as e:
            print(f"Error exporting to CSV: {e}")

    @staticmethod
    def export_to_json(data, file_path):
        """Exports aggregated data to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data successfully exported to {file_path}.")
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
