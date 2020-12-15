"""
Braxton Phillips
SDEV 220
Chapter 18 Exercises 18.1
Due Dec 5, 2020 
"""

#implementation of linked list
class Node():
   def __init__( self, data = None, next_ = None ):
       self.data = data
       self.next = next_

   def get_data( self ):
       return self.data

   def get_next_node( self ):
       return self.next

   def set_data( self, data ):
       self.data = data

   def set_next_node( self, next_ ):
       self.next = next_

#class for linkedlist
class LinkedList():
   def __init__(self, head = None):
       self.head = head

   def insert(self, data):
        new_node = Node(data)
        new_node.set_next_node( self.head )
        self.head = new_node

   def get_size(self): #get size of branch
        node_var = self.head;
        size = 0
        while node_var != None:
            node_var = node_var.get_next_node()
            size = size + 1
        return size

   def lastIndexOf(self, data): #reads last val of list
       node_var = self.head
       element_found = False
       last_seen_at = None
       index = 0
       while node_var != None:
            if node_var.get_data() == data:
                element_found = True
                last_seen_at = index
            node_var = node_var.get_next_node()
            index = index + 1
       if element_found :
            return last_seen_at; #returns spot in list
       else :
           return -1 #mofdify unseen vals

   def remove(self, data): #branch clearing 
        node_var = self.head
        previous = None
        element_found = False
        while (node_var != None) and \
          element_found is False:
            if node_var.get_data() == data:
                element_found = True
            else:
                previous = node_var;
                node_var = node_var.get_next_node()
        if node_var is None:
           return
        if previous is None:
            self.head = node_var.get_next_node()
        else:
            previous.set_next_node( node_var.get_next_node() )

    #creation of vals for list
   def set( self, index, data ):
       node_var = self.head
       at = 0
       while at < index:
           node_var = node_var.get_next_node()
           at = at + 1
       node_var.set_data( data )

   def print_List( self ): #function for printing list
       print('~'*10) #formatting
       node_var = self.head
       while node_var != None:
           print( node_var.get_data() )
           node_var = node_var.get_next_node()
       print('~'*10)#formatting
  
   def get_List( self ):
       node_var = self.head
       List = []
       while node_var != None:
           List.append( node_var.get_data() )
           node_var = node_var.get_next_node()
       return List

   def addAll( self, list2 ):
       list2 = list2.get_List()
       for element in list2:
           if self.lastIndexOf( element ) == -1:
               #if element is not there add it
               self.insert( element )

   def removeAll( self, list2 ):
       list2 = list2.get_List()
       for element in list2:
           index = self.lastIndexOf( element )
           if index != -1:
               self.remove( element )

   def retainAll( self, list2 ):
       list2 = list2.get_List()
       for element in list2:
           self.insert( element )

#declaration of test vals
def testVals():
   list1 = ["Tom", "George", "Peter", "Jean", "Jane"]
   list2 = ["Tom", "George", "Michael", "Michelle", "Daniel"]
  
   L1 = LinkedList()
   L2 = LinkedList()
   for l in list1:
       L1.insert( l )
   for l in list2:
       L2.insert( l )
  
   L1.addAll( L2 )
   L1.print_List()
  
   L1 = LinkedList()
   for l in list1:
       L1.insert( l )
   L1.removeAll( L2 )
   L1.print_List()

   L1 = LinkedList()
   for l in list1:
       L1.insert( l )
   L1.retainAll( L2 )
   L1.print_List()


testVals()