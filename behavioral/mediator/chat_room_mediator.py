from base_mediator import Mediator, Colleague

class ChatRoomMediator(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user: Colleague):
        self.users.append(user)

    def send_message(self, message: str, sender: Colleague) -> None:
        for user in self.users:
            if user != sender:
                user.receive_message(f"{sender.name}: {message}")
