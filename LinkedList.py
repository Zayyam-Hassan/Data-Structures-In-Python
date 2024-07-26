class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertathead(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            temp_head = Node(data)
            temp_head.next = self.head
            self.head = temp_head

    def insertattail(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)

    def getnodeatindex(self,index):
        current_index = 0
        current_node = self.head
        while current_node and current_index + 1 != index:
            current_node = current_node.next
        return current_node

    def insertatindex(self, data, index):
        if index == 0:
            self.insertathead(data)
            return
        else:
            current_node = self.getnodeatindex(index)
            if current_node:
                temp_node = Node(data)
                temp_node.next = current_node.next
                current_node.next = temp_node
            else:
                print("Index Not Found !!!")

    def delete(self, val):
        if self.head is None:
            return
        current_node = self.head
        prev_node = None
        while current_node and current_node.data != val:
            prev_node = current_node
            current_node = current_node.next
        if prev_node is None:
            self.head = current_node.next
            current_node = None
        elif current_node:
            prev_node.next = current_node.next
            current_node = None
        else:
            print("Node with the Value Not Found")

    def deleteathead(self):
        if self.head is None:
            return
        current_node = self.head
        self.head = self.head.next
        current_node = None

    def deleteattail(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node = None

    def update(self, index, val):
        if self.head is None:
            return
        current_node = self.getnodeatindex(index+1)
        if current_node:
            current_node.data = val

    def search(self, val):
        if self.head is None:
            return
        current_node = self.head
        while current_node and current_node.data != val:
            current_node = current_node.next
        if current_node:
            return current_node
        else:
            print("Value Not Found")

    def elementcount(self):
        mycount = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            mycount += 1
        return mycount

    def printlinkedlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end='->')
            current_node = current_node.next
        print('None')

