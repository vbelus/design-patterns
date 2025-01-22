from flyweight_factory import FlyweightFactory


class Forest:
    """
    Represents a forest with many trees. Uses flyweight objects for optimization.
    """
    def __init__(self):
        self._trees = []
        self._factory = FlyweightFactory()

    def plant_tree(self, tree_type: str, texture: str, color: str, x: int, y: int):
        """
        Plant a tree in the forest. Uses a flyweight to minimize memory usage.
        """
        tree = self._factory.get_flyweight(tree_type, texture, color)
        self._trees.append((tree, x, y))

    def display_forest(self) -> None:
        """
        Display all trees in the forest.
        """
        for tree, x, y in self._trees:
            print(tree.display(x, y))

    def flyweight_count(self) -> int:
        """
        Return the number of unique flyweight instances.
        """
        return self._factory.flyweight_count()
