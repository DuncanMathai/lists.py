# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse" , 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)

# Delete poolhouse data
del(areas_2[10:12])
print(areas_2)

# Create an areas_copy list and make a change on the list without affecting the areas list
# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)