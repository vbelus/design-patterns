class TreeFlyweight:
    """
    Flyweight class representing the intrinsic properties of a tree.
    """
    def __init__(self, tree_type: str, texture: str, color: str):
        self.tree_type = tree_type
        self.texture = texture
        self.color = color

    def display(self, x: int, y: int) -> str:
        """
        Display the tree at a specific position (extrinsic property).
        """
        return f"Tree ({self.tree_type}, {self.texture}, {self.color}) at position ({x}, {y})"
