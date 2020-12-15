"""
Braxton Phillips
SDEV 220
Chapter 19 Exercise 19.1
Due Dec 12, 2020
(Adding new methods in BinaryTree) Add the following new methods in BinaryTree.
"""
#from BinaryTree import BinaryTree

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root
        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current. element
                return True # Element is found
        return False

    # Displays the nodes in breadth-first traversal
    def breadthFirstTraversal(self): #given
        node = self
        node.root.level = 1
        queue = deque([node.root])
        output = []
        current_level = node.root.level
    
        while len(queue)>0:
    
            current_node = queue.popleft()
    
            if(current_node.level > current_level):
                output.append("\n")
                current_level += 1
    
            output.append(str(current_node))
    
            if current_node.left != None:
                current_node.left.level = current_level + 1 
                queue.append(current_node.left) 
    
            if current_node.right != None:
                current_node.right.level = current_level + 1 
                queue.append(current_node.right)
            
        return ''.join(output)
    #Returns the height of this binary tree, i.e., the number of the nodes in the longest path of the root to a leaf
    def height(self): #given
        return self.maxdepth(self.root)
    
    def maxdepth(self,node):
        if node is None: 
            return 0 ;  
        else : 
            lDepth = self.maxdepth(node.left) 
            rDepth = self.maxdepth(node.right) 
      
            if (lDepth > rDepth): 
                return lDepth+1
            else: 
                return rDepth+1


#from chapt
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None
    def __repr__(self):
        return(str(self.element))


#test case
b = BinaryTree()
b.insert(10)
b.insert(20)
b.insert(30)
b.insert(40)
b.insert(50)
print("breadthFirstTraversal by level: ")
print(b.breadthFirstTraversal())
print("height of the tree is: ",b.height())