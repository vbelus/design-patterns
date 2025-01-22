from tree_flyweight import TreeFlyweight


class FlyweightFactory:
    """
    Factory to manage and reuse TreeFlyweight instances.
    """
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, tree_type: str, texture: str, color: str) -> TreeFlyweight:
        """
        Retrieve a flyweight tree, creating it if it doesn't already exist.
        """
        key = (tree_type, texture, color)
        if key not in self._flyweights:
            self._flyweights[key] = TreeFlyweight(tree_type, texture, color)
        return self._flyweights[key]

    def flyweight_count(self) -> int:
        """
        Return the number of flyweights managed by the factory.
        """
        return len(self._flyweights)
