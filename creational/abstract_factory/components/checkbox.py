class Checkbox:
    def render(self):
        raise NotImplementedError("Subclasses must implement the `render` method.")

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering a Windows-style checkbox."

class MacOSCheckbox(Checkbox):
    def render(self):
        return "Rendering a macOS-style checkbox."
