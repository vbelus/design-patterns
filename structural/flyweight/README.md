# Flyweight Design Pattern

The **Flyweight** pattern helps save memory by sharing common data between objects instead of storing the same data multiple times. It's perfect for situations where you need lots of similar objects, like trees in a forest!

---

## Why Use the Flyweight Pattern?

Imagine you're making a **forest** in a video game. Every tree has some shared properties, like:
- **Type** (e.g., Oak, Pine, Cherry Blossom)
- **Texture** (e.g., Rough, Smooth)
- **Color** (e.g., Green, Pink)

Now, if you create a separate tree object for every single tree, you'd end up using **a lot of memory**. But with the **Flyweight** pattern, you can **share tree objects** that have the same type, texture, and color. This way, instead of creating thousands of copies of the same tree, you just **reuse** one object and change only its **position**.

---

## Files in This Directory

- **`tree_flyweight.py`**: Contains the shared tree object with intrinsic properties.
- **`flyweight_factory.py`**: Manages the reuse of tree objects.
- **`forest.py`**: Manages the forest, where trees are placed using the Flyweight pattern.
- **`example.py`**: Runs the simulation and shows the Flyweight pattern in action.
