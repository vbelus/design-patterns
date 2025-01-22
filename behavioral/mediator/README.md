# Chat Room with Mediator Design Pattern

This directory demonstrates the **Mediator Design Pattern** in Python, which centralizes communication between objects, reducing dependencies between them.

---

## **Directory Structure**

- **`base_mediator.py`**:  
  Defines the `Mediator` interface and the `Colleague` base class, providing a common structure for all mediators and users.

- **`chat_room_mediator.py`**:  
  Implements the `ChatRoomMediator`, a concrete mediator that coordinates message passing between users.

- **`user.py`**:  
  Implements the `User` class, representing participants in the chat room.

- **`example.py`**:  
  Demonstrates the usage of the mediator pattern with a simple chat room example.

---

## **The Mediator Pattern**

In this implementation:

1. **Centralized Communication**:  
   - The `ChatRoomMediator` handles all communication between users, ensuring they do not need to reference each other directly.

2. **Loose Coupling**:  
   - Users (`User`) are decoupled from one another, relying only on the mediator to interact.

3. **Dynamic Interactions**:  
   - New users can join the chat room dynamically without requiring changes to existing code.

---

### **Example Output**

Running `example.py` produces the following output:

