class Button:
    def render(self):
        raise NotImplementedError("Subclasses must implement the `render` method.")

class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows-style button."

class MacOSButton(Button):
    def render(self):
        return "Rendering a macOS-style button."
