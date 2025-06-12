# Singly Linked List Implementation using OOP

class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages the linked list with methods to add, print, and delete nodes."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Prints all elements of the list."""
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Deletes the nth node in the list (1-based index)."""
        try:
            if not self.head:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index should be 1 or greater.")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node {n} with value {deleted_data}")
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node {n} with value {deleted_data}")

        except IndexError as e:
            print("Error:", e)


# Sample Test
if __name__ == "__main__":
    # Create a linked list
    ll = LinkedList()

    # Add some nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Original List:")
    ll.print_list()

    print("\nDeleting 3rd node:")
    ll.delete_nth_node(3)
    ll.print_list()

    print("\nAttempting to delete 10th node (out of range):")
    ll.delete_nth_node(10)

    print("\nDeleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nDeleting from empty list:")
    # Delete remaining nodes
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    # Now the list is empty
    ll.delete_nth_node(1)
