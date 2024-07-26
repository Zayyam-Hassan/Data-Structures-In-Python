# main.py
from LinkedList import LinkedList
from BinarySearchTree import Tree
from Stack_Queue import Stack, Queue
from HashMap import HashMap
from Graph import Graph


def main():
    # Linked List operations
    Linked = LinkedList()
    Linked.insertathead(2)
    Linked.insertathead(3)
    Linked.insertatindex(5, -1)
    Linked.printlinkedlist()
    Linked.update(0, 6)
    Linked.printlinkedlist()
    Linked.deleteathead()
    Linked.printlinkedlist()

    # Binary Search Tree operations
    MyTree = Tree()
    MyTree.insert(5)
    MyTree.insert(4)
    MyTree.insert(2)
    MyTree.insert(3)
    MyTree.delete(2)
    print("Inorder traversal of BST:")
    MyTree.inorder_traversal()
    print()  # Newline for better readability

    # Stack operations
    MyStack = Stack()
    MyStack.push(4)
    MyStack.push(2)
    MyStack.push(3)
    print("Top element in Stack:", MyStack.peek())
    MyStack.pop()
    print("Top element in Stack after pop:", MyStack.peek())

    # Queue operations
    MyQueue = Queue()
    MyQueue.push(1)
    MyQueue.push(2)
    MyQueue.push(3)
    print("Front element in Queue:", MyQueue.get_front())
    MyQueue.pop()
    print("Front element in Queue after pop:", MyQueue.get_front())

    # Hash Map operations
    MyHashMap = HashMap()
    MyHashMap.insert('key1', 'value1')
    MyHashMap.insert('key2', 'value2')
    print("Value for 'key1':", MyHashMap.get('key1'))
    MyHashMap.delete('key1')
    print("Value for 'key1' after deletion:", MyHashMap.get('key1'))

    # Graph operations
    MyGraph = Graph()
    MyGraph.add_vertex('A')
    MyGraph.add_vertex('B')
    MyGraph.add_edge('A', 'B')
    print("Vertices in graph:", MyGraph.get_vertices())
    print("Edges in graph:", MyGraph.get_edges())
    MyGraph.remove_edge('A', 'B')
    print("Edges in graph after removing edge A-B:", MyGraph.get_edges())
    MyGraph.remove_vertex('A')
    print("Vertices in graph after removing vertex A:", MyGraph.get_vertices())


if __name__ == "__main__":
    main()
