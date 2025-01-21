# bold_decorator.py
from base_text import TextComponent

class BoldDecorator(TextComponent):
    """Decorator to add bold formatting."""
    def __init__(self, component: TextComponent):
        self.component = component

    def render(self) -> str:
        return f"<b>{self.component.render()}</b>"
