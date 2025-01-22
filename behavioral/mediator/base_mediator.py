from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: "Colleague") -> None:
        pass

class Colleague(ABC):
    def __init__(self, mediator: Mediator, name: str):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def receive_message(self, message: str) -> None:
        pass
