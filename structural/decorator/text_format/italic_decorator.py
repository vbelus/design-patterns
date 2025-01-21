# italic_decorator.py
from base_text import TextComponent

class ItalicDecorator(TextComponent):
    """Decorator to add italic formatting."""
    def __init__(self, component: TextComponent):
        self.component = component

    def render(self) -> str:
        return f"<i>{self.component.render()}</i>"
