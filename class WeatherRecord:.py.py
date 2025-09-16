class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date          
        self.city = city          
        self.temperature = temperature  

    def __repr__(self):
        return f"WeatherRecord(Date={self.date}, City={self.city}, Temp={self.temperature})"


class WeatherDataStorage:
    def __init__(self, years, cities):
        self.years = years
        self.cities = cities
        # Initialize 2D array with None (sentinel for missing data)
        self.data = [[None for _ in cities] for _ in years]

    def insert(self, year, city, temperature):
        y_index = self.years.index(year)
        c_index = self.cities.index(city)
        self.data[y_index][c_index] = temperature

    def delete(self, year, city):
        y_index = self.years.index(year)
        c_index = self.cities.index(city)
        self.data[y_index][c_index] = None

    def retrieve(self, city, year):
        y_index = self.years.index(year)
        c_index = self.cities.index(city)
        return self.data[y_index][c_index]

    def rowMajorAccess(self):
        for y, year in enumerate(self.years):
            for c, city in enumerate(self.cities):
                print(f"Year: {year}, City: {city}, Temp: {self.data[y][c]}")

    def columnMajorAccess(self):
        for c, city in enumerate(self.cities):
            for y, year in enumerate(self.years):
                print(f"Year: {year}, City: {city}, Temp: {self.data[y][c]}")

    def handleSparseData(self):
        sparse_repr = {}
        for y, year in enumerate(self.years):
            for c, city in enumerate(self.cities):
                if self.data[y][c] is not None:
                    sparse_repr[(year, city)] = self.data[y][c]
        return sparse_repr

    def analyzeComplexity(self):
        print("Insert: O(1)")
        print("Delete: O(1)")
        print("Retrieve: O(1)")
        print("Row/Column Traversal: O(Y * C)")
        print("Space (2D array): O(Y * C)")
        print("Space (Sparse): O(N), where N = non-empty entries")


# -------------------- Example Usage --------------------
years = [2023, 2024, 2025]
cities = ["New York", "London", "Tokyo"]

storage = WeatherDataStorage(years, cities)

# Insert some data
storage.insert(2023, "New York", 15.5)
storage.insert(2024, "London", 12.3)
storage.insert(2025, "Tokyo", 20.8)

print("Retrieve Example:", storage.retrieve("London", 2024))  # Output: 12.3

# Row-major access
print("\nRow-Major Access:")
storage.rowMajorAccess()

# Column-major access
print("\nColumn-Major Access:")
storage.columnMajorAccess()

# Sparse data representation
print("\nSparse Representation:", storage.handleSparseData())

# Complexity analysis
print("\nComplexity Analysis:")
storage.analyzeComplexity()