# Initialize variables to store the read data
problem_name = ""         # Store the name of the problem
knapsack_data_type = ""   # Store the data type of the knapsack problem
dimension = 0             # Store the dimension of the problem
num_items = 0             # Store the number of items
capacity = 0              # Store the capacity of the knapsack
min_speed = 0.0           # Store the minimum speed
max_speed = 0.0           # Store the maximum speed
renting_ratio = 0.0       # Store the renting ratio
edge_weight_type = ""      # Store the type of edge weight
node_coord_section = []    # Store the list of node coordinate information
items_section = []         # Store the list of item information

# Open the file
with open('a280-n279.txt', 'r') as file:
    # Read the file content line by line
    for line in file:
        # Remove trailing newline characters
        line = line.strip()

        # Parse the file content line by line
        if line.startswith("PROBLEM NAME:"):
            problem_name = line.split(":")[1].strip()
        elif line.startswith("KNAPSACK DATA TYPE:"):
            knapsack_data_type = line.split(":")[1].strip()
        elif line.startswith("DIMENSION:"):
            dimension = int(line.split(":")[1].strip())
        elif line.startswith("NUMBER OF ITEMS:"):
            num_items = int(line.split(":")[1].strip())
        elif line.startswith("CAPACITY OF KNAPSACK:"):
            capacity = int(line.split(":")[1].strip())
        elif line.startswith("MIN SPEED:"):
            min_speed = float(line.split(":")[1].strip())
        elif line.startswith("MAX SPEED:"):
            max_speed = float(line.split(":")[1].strip())
        elif line.startswith("RENTING RATIO:"):
            renting_ratio = float(line.split(":")[1].strip())
        elif line.startswith("EDGE_WEIGHT_TYPE:"):
            edge_weight_type = line.split(":")[1].strip()
        elif line.startswith("NODE_COORD_SECTION"):
            # Start reading node coordinate data
            break
        elif line:  # If the line is not empty
            # Process other possible information
            print("Other Information:", line)

    # Continue reading node coordinate data
    for line in file:
        line = line.strip()
        if line.startswith("ITEMS SECTION"):
            # Start reading item information
            break
        elif line:  # If the line is not empty
            # Parse node coordinate data
            index, x, y = map(int, line.split())
            node_coord_section.append((index, x, y))

    # Continue reading item information
    for line in file:
        line = line.strip()
        if line:  # If the line is not empty
            # Parse item information
            index, profit, weight, assigned_node_number = map(int, line.split())
            items_section.append((index, profit, weight, assigned_node_number))

# Print the read information
print("PROBLEM NAME:", problem_name)
print("KNAPSACK DATA TYPE:", knapsack_data_type)
print("DIMENSION:", dimension)
print("NUMBER OF ITEMS:", num_items)
print("CAPACITY OF KNAPSACK:", capacity)
print("MIN SPEED:", min_speed)
print("MAX SPEED:", max_speed)
print("RENTING RATIO:", renting_ratio)
print("EDGE_WEIGHT_TYPE:", edge_weight_type)
print("NODE_COORD_SECTION:", node_coord_section)
print("ITEMS SECTION:", items_section)
