from components.button import MacOSButton
from components.checkbox import MacOSCheckbox

class MacOSFactory:
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()
