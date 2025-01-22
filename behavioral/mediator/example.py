from chat_room_mediator import ChatRoomMediator
from user import User

def main():
    chat_room = ChatRoomMediator()

    user1 = User(chat_room, "Alice")
    user2 = User(chat_room, "Bob")
    user3 = User(chat_room, "Charlie")

    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)

    user1.send_message("Hello everyone!")
    user2.send_message("Hi Alice!")
    user3.send_message("Good morning!")

if __name__ == "__main__":
    main()
