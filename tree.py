class node:

    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data 
    
    def insert(self,data) -> None:
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()

# Use the insert method to add nodes
root = node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()