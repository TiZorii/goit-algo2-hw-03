# Homework on "Graphs and Trees"

To begin, install dependencies using the following command:

```
pip install -r requirements.txt.
```


## Task 1. Applying the Maximum Flow Algorithm for Logistics

Develop a program to model a flow network for logistics, transporting goods from warehouses to stores using the maximum flow algorithm. Analyze the obtained results and compare them with theoretical knowledge.

### Technical Requirements

1. Implement the Edmonds-Karp algorithm for maximum flow.
2. The graph structure should follow the given model with 20 vertices and specified capacities.

## How to Run

```
python task_1.py

--- результатами потоків між терміналами та магазинами ---

| Термінал            | Магазин            | Фактичний Потік (одиниць) |
| Термінал 1          | Магазин 1          | 15                        |
| Термінал 1          | Магазин 2          | 10                        |
| Термінал 1          | Магазин 3          | 20                        |
| Термінал 1          | Магазин 4          | 15                        |
| Термінал 1          | Магазин 5          | 10                        |
| Термінал 1          | Магазин 6          | 20                        |
| Термінал 1          | Магазин 7          | 15                        |
| Термінал 1          | Магазин 8          | 15                        |
| Термінал 1          | Магазин 9          | 10                        |
| Термінал 1          | Магазин 10         | 0                         |
| Термінал 1          | Магазин 11         | 0                         |
| Термінал 1          | Магазин 12         | 0                         |
| Термінал 1          | Магазин 13         | 0                         |
| Термінал 1          | Магазин 14         | 0                         |
| Термінал 2          | Магазин 1          | 0                         |
| Термінал 2          | Магазин 2          | 0                         |
| Термінал 2          | Магазин 3          | 0                         |
| Термінал 2          | Магазин 4          | 10                        |
| Термінал 2          | Магазин 5          | 10                        |
| Термінал 2          | Магазин 6          | 10                        |
| Термінал 2          | Магазин 7          | 15                        |
| Термінал 2          | Магазин 8          | 15                        |
| Термінал 2          | Магазин 9          | 10                        |
| Термінал 2          | Магазин 10         | 20                        |
| Термінал 2          | Магазин 11         | 10                        |
| Термінал 2          | Магазин 12         | 15                        |
| Термінал 2          | Магазин 13         | 5                         |
| Термінал 2          | Магазин 14         | 10                        |
```
## Questions and Answers

1. **Which terminals provide the highest flow of goods to stores?**  
   Terminal 1 provides the highest flow of goods to stores.

2. **Which routes have the lowest capacity, and how does this affect the overall flow?**  
   The lowest capacity is observed on the route from Terminal 2 to Store 13, with an actual flow of 5 units.

3. **Which stores received the least goods, and can their supply be increased by enhancing certain route capacities?**  
   Store 13 received only 5 units of goods, the lowest in the flow. Increasing the capacity of the route from Warehouse 4 to Store 13 could improve supply.

4. **Are there bottlenecks that can be removed to improve the efficiency of the logistics network?**  
   The main bottleneck is the route from Warehouse 4 to Store 13.

## Task 2. Comparing the Efficiency of OOBTree and Dictionary for Range Queries

Develop a program to store a large dataset of products in two data structures—OOBTree and dict—and conduct a comparative analysis of their performance for range queries.

### Task Description

1. Use the provided file generated_items_data.csv to load product information. Each product includes a unique identifier ID, name Name, category Category, and price Price.

2. Implement two structures for storing products.  
   - First: OOBTree from the BTrees library, where the key is ID and the value is a dictionary with product attributes.  
   - Second: dict (standard dictionary), where the key is also ID and the value is a similar dictionary with product attributes.

3. Implement functions for adding products to both structures: add_item_to_tree and add_item_to_dict.

4. Implement functions for performing range queries to find all products within a specified price range: range_query_tree and range_query_dict.

5. Measure the total execution time of range queries for each structure using timeit.

6. Execute the range query 100 times for each structure to calculate the average execution time.

7. Display the total execution time of range queries for each structure, including the time required to perform 100 queries for OOBTree and dict.

### Technical Requirements

1. Use only OOBTree and the standard dict for comparison.
2. Implement separate functions for adding a product to the structure: add_item_to_tree, add_item_to_dict.
3. Implement separate functions for range queries: range_query_tree, range_query_dict.
4. Use the timeit library for precise performance measurement.
5. Time measurement should be performed for 100 range queries for each structure.

## How to Run

```
python task_2.py

Total range_query time for OOBTree: 0.006717 seconds
Total range_query time for Dict: 0.888999 seconds
```
