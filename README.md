
#📑 Report: Weather Data Storage System

a. Weather Record ADT

The Weather Record Abstract Data Type (ADT) defines the basic structure for representing individual weather observations. It encapsulates the following attributes:

Date: A string (e.g., "15/09/2025") or a custom structure (day/month/year).

City: A string representing the city name (e.g., "London").

Temperature: A floating-point number representing the recorded temperature.


Methods

insert(data): Adds a new weather record to the system.

delete(data): Removes an existing weather record based on a date and city.

retrieve(city, year): Retrieves the temperature record(s) for a specified city and year.


This ADT ensures modularity, allowing storage and retrieval of weather data in a structured way without exposing internal storage details.


---

b. Strategy for Memory Representation

Weather data is stored in a 2D array where:

Rows = Years

Columns = Cities

Cell value = Temperature (or sentinel if missing)


Row-Major Order

Data is stored row by row (all cities for a year, then move to next year).

Traversal:

for year in years:
    for city in cities:
        access(year, city)

Advantage: Better cache locality because elements of a row are stored contiguously in memory.

Use Case: Efficient when analyzing year-wise trends across cities.


Column-Major Order

Data is stored column by column (all years for one city, then move to next city).

Traversal:

for city in cities:
    for year in years:
        access(year, city)

Advantage: Useful for operations that focus on city-wise comparisons over multiple years.

Use Case: Efficient for long-term city climate analysis.


Note: In Python, lists are row-major by default (like C), so row-wise access is more memory-efficient.


---

c. Approach to Handling Sparse Data

Real-world weather datasets often contain missing values due to incomplete observations. To manage this, two approaches are considered:

1. Sentinel Values

Store a placeholder (None or -9999) in the 2D array for missing data.

Simple but wastes space if the dataset is sparse.



2. Sparse Matrix Representation (Dictionary)

Store only non-empty values using a dictionary:

sparse_data[(year, city)] = temperature

Memory efficient since only existing records are stored.

Trade-off: Extra dictionary overhead, but still supports O(1) insertion/retrieval.




Choice:

Use 2D array if dataset is mostly full.

Use sparse representation if large portions of data are missing.



---

d. Time and Space Complexity Analysis

Operation	2D Array (Dense)	Sparse Representation (Dictionary)

Insert	O(1) (direct index)	O(1) (hash map insertion)
Delete	O(1) (set to sentinel)	O(1) (delete key)
Retrieve	O(1) (direct lookup)	O(1) (hash lookup)
Row Traversal	O(Y * C)	O(N) where N = number of records
Column Traversal	O(Y * C)	O(N)
Space Usage	O(Y * C) (even for missing data)	O(N) (efficient for sparse data)


Y = number of years.

C = number of cities.

N = number of non-empty entries.


Key Insights

Dense 2D array is fast for direct indexing but wastes memory if sparse.

Sparse matrix saves memory but still maintains efficient O(1) operations.

Row-major traversal is generally faster in Python due to memory layout.
