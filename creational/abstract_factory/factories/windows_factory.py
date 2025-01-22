from components.button import WindowsButton
from components.checkbox import WindowsCheckbox

class WindowsFactory:
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()
