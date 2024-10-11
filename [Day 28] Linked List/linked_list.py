class Node:
    def __init__(self,new_data):
        self.data = new_data #Data
        self.next = None #Next Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def delete(self,key):
        pointer_node = self.head

        if pointer_node and pointer_node.data == key:
            self.head = pointer_node.next
            pointer_node = None
            return
        
        prev = None

        while pointer_node and pointer_node.data != key:
            prev = pointer_node
            pointer_node = pointer_node.next

        if pointer_node is None:
            return
        
        prev.next = pointer_node.next
        pointer_node = None

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

def main():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(3)
    ll.insert(2)
    ll.printLL()
    ll.delete(2)
    ll.printLL()


if __name__ == "__main__":
    main()