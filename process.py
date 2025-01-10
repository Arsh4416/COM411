import csv

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load_data(self):
        """Loads the dataset into memory."""
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
            return len(self.data)
        except FileNotFoundError:
            print("Error: File not found.")
            return 0

    def filter_reviews_by_park(self, park_name):
        """Filters reviews for a specific park."""
        return [row for row in self.data if row['Branch'] == park_name]

    def count_reviews_by_location(self, park_name, location):
        """Counts the number of reviews for a park by location."""
        return sum(1 for row in self.data if row['Branch'] == park_name and row['Reviewer_Location'] == location)

    def aggregate_reviews_by_park(self):
        """Aggregates the number of reviews by park."""
        park_reviews = {}
        for row in self.data:
            park = row['Branch']
            if park not in park_reviews:
                park_reviews[park] = 0
            park_reviews[park] += 1
        return park_reviews

    def aggregate_reviews_by_location(self, park_name):
        """Aggregates the number of reviews for a specific park by location."""
        location_reviews = {}
        for row in self.data:
            if row['Branch'] == park_name:
                location = row['Reviewer_Location']
                if location not in location_reviews:
                    location_reviews[location] = 0
                location_reviews[location] += 1
        return location_reviews

    def aggregate_data(self):
        """Aggregates data for exporting."""
        park_data = {}
        for row in self.data:
            park = row['Branch']
            if park not in park_data:
                park_data[park] = {
                    'total_reviews': 0,
                    'positive_reviews': 0,
                    'total_rating': 0,
                    'countries': set()
                }
            park_data[park]['total_reviews'] += 1
            park_data[park]['total_rating'] += int(row['Rating'])
            if int(row['Rating']) > 3:
                park_data[park]['positive_reviews'] += 1
            park_data[park]['countries'].add(row['Reviewer_Location'])
        for park in park_data:
            park_data[park]['average_rating'] = park_data[park]['total_rating'] / park_data[park]['total_reviews']
            park_data[park]['countries'] = len(park_data[park]['countries'])
        return park_data
