# example.py
from base_text import PlainText
from italic_decorator import ItalicDecorator
from bold_decorator import BoldDecorator
from color_decorator import ColorDecorator

if __name__ == "__main__":
    # Start with plain text
    text = PlainText("Hello, World!")

    # Render the plain text
    print(text.render())

    # Apply decorators in classical style
    text = ItalicDecorator(text)  # Add italic
    text = BoldDecorator(text)    # Add bold
    text = ColorDecorator(text, "blue")  # Add blue color

    # Render the final formatted text
    print(text.render())  # Output: <span style="color: blue;"><b><i>Hello, World!</i></b></span>
