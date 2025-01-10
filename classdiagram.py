from graphviz import Digraph

# Create the class diagram
diagram = Digraph(comment='Class Diagram')

# Add nodes for the classes
diagram.node('A', 'DisneylandReviewAnalyser', shape='ellipse')
diagram.node('B', 'DataProcessor', shape='ellipse')
diagram.node('C', 'UserInterface', shape='ellipse')
diagram.node('D', 'Visualizer', shape='ellipse')
diagram.node('E', 'DataExporter', shape='ellipse')
diagram.node('F', 'Logger', shape='ellipse')
diagram.node('G', 'Authentication', shape='ellipse')

# Add edges for relationships
diagram.edge('A', 'B', label='uses')
diagram.edge('A', 'C', label='uses')
diagram.edge('A', 'D', label='uses')
diagram.edge('A', 'E', label='uses')
diagram.edge('A', 'F', label='uses')
diagram.edge('A', 'G', label='uses')

# Save and render the diagram
diagram.render('class_diagram_OOP', format='png', cleanup=True)
