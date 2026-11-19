class Library:
    def __init__(self):
        self.catalog = []

    def insert_title(self, title):
        self.catalog.append(title)
        print(title, "added successfully")

    def show_catalog(self):
        print("Available Books:")
        for title in self.catalog:
            print(title)

my_lib = Library()
my_lib.insert_title("Machine Learning Basics")
my_lib.insert_title("Algorithms in Python")
my_lib.insert_title("Operating Systems")
my_lib.show_catalog()
