import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_pie_chart(data, title):
        """Creates a pie chart for the given data."""
        labels, sizes = zip(*data.items())
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.show()

    @staticmethod
    def plot_bar_chart(data, title, x_label, y_label):
        """Creates a bar chart for the given data."""
        labels, values = zip(*data.items())
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_line_chart(data, title, x_label, y_label):
        """Creates a line chart for trends over time."""
        labels, values = zip(*sorted(data.items()))
        plt.figure(figsize=(10, 6))
        plt.plot(labels, values, marker='o')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_heatmap(data, title, x_label, y_label):
        """Creates a heatmap for review distributions."""
        import seaborn as sns
        import numpy as np

        x_labels = list(data.keys())
        y_labels = list(data[next(iter(data))].keys())
        heatmap_data = np.array([list(data[x].values()) for x in x_labels])

        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu", xticklabels=y_labels, yticklabels=x_labels)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.tight_layout()
        plt.show()
