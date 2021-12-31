import QueueLL as q

class BST:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        '''insert a new node in a binary search tree'''
        if self.data == None:           #parent node is empty
            self.data = data

        elif data <= self.data:         #if data less than that in parent node
            if self.left_child is None: #insert in left child
                new_node = BST(data)
                self.left_child = new_node
            else:
                self.left_child.insert(data)
                 
        else:                            #if data greater than that in parent node
            if self.right_child is None: #insert in right child
                new_node = BST(data)
                self.right_child = new_node
            else:
                self.right_child.insert(data)

        return f"{data} has been successsfully inserted"

    def pre_order(self):
        print(self.data)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()   

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.data)
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order() 
        print(self.data) 

    def level_order(self):
        order = q.Queue()
        order.enqueue(self)             #self(TreeNode) gets enqueued inside Queue node
        while not(order.isEmpty()):
            node = order.dequeue().data #order.dequeue() returns Queue node
            print(str(node.data))       #node.data stores TreeNode; we print TreeNode.data
            if node.left_child:
                order.enqueue(node.left_child)
            if node.right_child:
                order.enqueue(node.right_child) 

    def search(self, data):
        if self.data == data:
            print('Node Value found')
            return
        elif data < self.data:
            if self.left_child:
                self.left_child.search(data)
                return
        else:
            if self.right_child:
                self.right_child.search(data)
                return
        print('Node Value not found')