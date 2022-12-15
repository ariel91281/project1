class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.first_node = Node(None)
        self.count = 0

    def push(self, next_val):
        next_node = Node(next_val)
        if self.count == 0:
            self.first_node = next_node
        else:
            current_node = self.first_node
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = next_node
        self.count += 1

    def pop(self):  # return last value and pop him  ,
        if self.count == 0:
            raise Exception("Error, list is empty")

        current_node = self.first_node
        return_val = ""

        if current_node.next is None:
            return_val = current_node.val
            self.first_node = Node(None)

        while current_node.next is not None:
            if current_node.next.next is None:
                return_val = current_node.next.val
                current_node.next = None
                break
            current_node = current_node.next

        self.count -= 1
        return return_val

    def head(self):  # return val of head
        if self.count == 0:
            raise Exception("Error, list is empty")
            # return None
        return self.first_node.val

    def len(self):  # return len of linked list   main:len(name) or name.len()
        return self.count

    def is_empty(self):  # return true false
        if self.count == 0:
            return True
        return False


llist = LinkedList()
llist.push(18)
llist.push(12)