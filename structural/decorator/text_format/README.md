# Text Formatting with Classical Decorators

This directory showcases the classical **Decorator Design Pattern** in Python, used to dynamically add behavior to objects at runtime. Instead of using Python's `@` decorator syntax, we explicitly implement decorators as classes that adhere to the same interface as the object they decorate.

The example here focuses on formatting text with styles like **italic**, **bold**, and **color** using a modular and extensible design.

---

## **Directory Structure**

- **`base_text.py`**:  
  Defines the `TextComponent` interface, which all components and decorators implement. Includes the `PlainText` class, representing the base text without any formatting.

- **`italic_decorator.py`**:  
  Adds italic formatting (`<i>` tags) to the text.

- **`bold_decorator.py`**:  
  Adds bold formatting (`<b>` tags) to the text.

- **`color_decorator.py`**:  
  Adds color formatting using a `<span style="color: ...">` tag. The color is passed as a parameter to the decorator.

- **`example.py`**:  
  Demonstrates how to compose multiple decorators to format text dynamically.

---

## **The Classical Decorator Pattern**

In this implementation:
1. **Common Interface**:  
   - All components (`PlainText`) and decorators (`ItalicDecorator`, `BoldDecorator`, `ColorDecorator`) implement the `TextComponent` interface, ensuring they can be used interchangeably.

2. **No `@` Syntax**:  
   - Unlike Python's built-in decorator syntax (`@`), decorators here are explicitly applied by wrapping the object:
     ```python
     text = ItalicDecorator(text)
     text = BoldDecorator(text)
     text = ColorDecorator(text, "blue")
     ```

3. **Dynamic Composition**:  
   - Decorators are applied dynamically, allowing for flexible and reusable combinations without altering the original `PlainText` class.