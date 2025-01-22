from forest import Forest


if __name__ == "__main__":
    # Create the forest
    forest = Forest()

    # Plant trees in the forest
    forest.plant_tree("Oak", "Rough", "Green", 1, 1)
    forest.plant_tree("Pine", "Smooth", "Dark Green", 2, 3)
    forest.plant_tree("Oak", "Rough", "Green", 5, 7)
    forest.plant_tree("Pine", "Smooth", "Dark Green", 10, 6)
    forest.plant_tree("Cherry Blossom", "Soft", "Pink", 8, 2)

    # Display the forest
    print("Forest Overview:")
    forest.display_forest()

    # Display the number of unique flyweight objects
    print("Number of unique tree types (flyweights): ")
    print(forest.flyweight_count())
