from factories.windows_factory import WindowsFactory
from factories.macos_factory import MacOSFactory

def main(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.render())  # Render the button
    print(checkbox.render())  # Render the checkbox

if __name__ == "__main__":
    # Client code dynamically selects a factory
    print("Using Windows Factory:")
    main(WindowsFactory())

    print("\nUsing macOS Factory:")
    main(MacOSFactory())
