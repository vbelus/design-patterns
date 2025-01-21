# base_text.py
from abc import ABC, abstractmethod

class TextComponent(ABC):
    """Abstract base class for text components."""
    @abstractmethod
    def render(self) -> str:
        """Render the text."""
        pass


class PlainText(TextComponent):
    """Concrete implementation of a basic text component."""
    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text