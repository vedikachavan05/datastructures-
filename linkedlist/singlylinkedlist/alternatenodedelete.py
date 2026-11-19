def solution():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        # append function
        def append(self, new_node):
            if self.head == None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next  # appending new node
                temp.next = new_node

        # traverse and print function
        def print_list(self):
            temp = self.head
            while temp:
                print(temp.data, end=" ")  # printing list
                temp = temp.next
            print()


        def alternatenodedelete(self):
            prev=self.head
            temp=self.head.next
            while(prev and temp):
                prev.next=temp.next
                temp=None #delete the node
                prev=prev.next
                if prev:
                   temp=prev.next # to check if prev is pointing to end of list 

    
    list1 = LinkedList()
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)

    list1.append(n1)
    list1.append(n2)
    list1.append(n3)
    list1.append(n4)
    list1.append(n5)

    print("list after appending:")
    list1.print_list()

    print("list after deleting the alternate nodes")
    list1.alternatenodedelete()
    list1.print_list()
    
solution()