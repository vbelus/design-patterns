# color_decorator.py
from base_text import TextComponent

class ColorDecorator(TextComponent):
    """Decorator to add color formatting."""
    def __init__(self, component: TextComponent, color: str):
        self.component = component
        self.color = color

    def render(self) -> str:
        return f'<span style="color: {self.color};">{self.component.render()}</span>'
