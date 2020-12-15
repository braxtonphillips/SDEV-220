"""
Braxton Phillips
SDEV 220
Chapter 18 Exercises 18.3
Due Dec 5, 2020 
"""

class LinkedList(object):
        class Node(object): #node class reps vals at point in branch 

                def __init__(self, value, next_node):
                        self.value = value
                        self.next_node = next_node

        def __init__(self, initial=None):
                self.front = self.back = self.current = None

        def empty(self):
                if self.front is None:
                        return True
                else:
                        return False

        def __iter__(self):
                self.current = self.front
                return self

        def __next__(self):
                if self.current:
                        tmp = self.current.value
                        self.current = self.current.next_node
                        return tmp
                else:
                        raise StopIteration()

        def pushFront(self, value):
                new = self.Node(value, self.front)
                if self.empty():
                        self.front = self.back = new
                else:
                        self.front = new

        def popFront(self):
                tmp = self.front
                if tmp is None:
                        return None
                if self.front == self.back:
                        self.front = self.back = None
                else:
                        self.front = tmp.next_node
                return tmp.value

        def pushBack(self, value):
                new = self.Node(value, None)
                if not self.empty():
                        self.back.next_node = new
                        self.back = new
                else:
                        self.front = self.back = new

        def popBack(self):
                if self.empty():
                        return None
                tmp = self.back
                if self.front == self.back:
                        self.front = self.back = None
                else:
                        temp2 = self.front
                        while temp2.next_node is not self.back:  #traverse
                                temp2 = temp2.next_node
                        temp2.next_node = None
                        self.back = temp2
                return tmp.value

        def remove(self, value): #remoce ext vals
                self.current = self.back
                prev = None
                if self.front is None:
                        return None
                if self.front.value == value:
                        self.popFront()
                        return True
                if self.back.value == value:
                        self.popBack()
                        return True

                prev = self.front
                current = prev.next_node

                while current: #raeds nodes to see if vals need updated
                        if current.value == value:
                                prev.next_node = current.next_node
                                return True
                        else:
                                prev = current
                                current = current.next_node
                return False

        def find(self, value): #func finds and evals val
                current = self.front
                while current:
                        if current.value == value:
                                return True
                        current = current.next_node
                return False

        def lastIndexOf(self, value): #reads lst val of list
                result = -1
                index = 0
                current = self.front
                while current:
                        if current.value == value:
                                result = index
                        current = current.next_node
                        index += 1
                return result

        def set(self, index, value): #assignment of vals
                count = 0
                current = self.front
                while current:
                        if count == index:
                                current.value = value
                                return
                        current = current.next_node
                        count += 1

        def __str__(self): #formatting
                result = ''
                current = self.front
                while current: #updating vals
                        result += str(current.value) + ' '
                        current = current.next_node
                return result

linked_list = LinkedList()
linked_list.pushBack(1)
linked_list.pushBack(2)
linked_list.pushBack(3)
linked_list.pushBack(4)

print(linked_list)
linked_list.remove(2)
print(linked_list)
linked_list.pushBack(3)

print(linked_list.lastIndexOf(2))
print(linked_list.lastIndexOf(3))

linked_list.set(2, 12)
print(linked_list)
