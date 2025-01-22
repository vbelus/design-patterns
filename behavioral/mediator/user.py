from base_mediator import Colleague

class User(Colleague):
    def receive_message(self, message: str) -> None:
        print(f"[{self.name} received]: {message}")

    def send_message(self, message: str) -> None:
        print(f"[{self.name} sending]: {message}")
        self.mediator.send_message(message, self)
