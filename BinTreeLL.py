import QueueLL as q

class TreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
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

    def search(self, item):
        order = q.Queue()
        order.enqueue(self)
        while not(order.isEmpty()):
            node = order.dequeue().data
            if node.data == item:
                return f'{item} found'
            if node.left_child:
                order.enqueue(node.left_child)
            if node.right_child:
                order.enqueue(node.right_child)
        return 'Not found'

    def insert(self, item):
        '''create an item(string) node and insert it in tree'''
        item_node = TreeNode(item)
        order = q.Queue()
        order.enqueue(self)
        while not(order.isEmpty()):
            node = order.dequeue().data
            if not(node.left_child):
                node.left_child = item_node
                return f'{item} inserted!!!'
            else:
                order.enqueue(node.left_child)
            if not(node.right_child):
                node.right_child = item_node
                return f'{item} inserted!!!'
            else:
                order.enqueue(node.right_child)
        
    def get_deepest_node(self):
        '''return the deepest node in TreeNode (self)'''
        order = q.Queue()
        order.enqueue(self)
        while not(order.isEmpty()):
            node = order.dequeue().data
            if node.left_child:
                order.enqueue(node.left_child)
            if node.right_child:
                order.enqueue(node.right_child)
        return node
    
    def delete_deepest_node(self):
        deepest_node = self.get_deepest_node()
        order = q.Queue()
        order.enqueue(self)
        while not(order.isEmpty()):
            node = order.dequeue().data
            if node is deepest_node:
                node = None
                return
            if node.right_child:
                if node.right_child is deepest_node:
                    node.right_child = None
                else:
                    order.enqueue(node.right_child)
            if node.left_child:
                if node.left_child is deepest_node:
                    node.left_child = None
                else:
                    order.enqueue(node.left_child)

    def delete_node(self, node_data):
        '''delete node_data(string) from a binary tree(self)'''
        deepest_node_data = self.get_deepest_node().data  #get data of deepest node
        order = q.Queue()
        order.enqueue(self)
        while not(order.isEmpty()):
            node = order.dequeue().data
            if node.data == node_data:         #if current node's data matches with data of node to be deleted
                node.data = deepest_node_data  #replace current node's data with that of deepest node
                self.delete_deepest_node()     #delete deepest node
                return f'{node_data} successfully deleted'
            if node.left_child:
                order.enqueue(node.left_child)
                if node.right_child:     #right child will be present iff left child exists
                    order.enqueue(node.right_child)
        return f'{node_data} could not be deleted'

    def delete_tree(self):
        '''Delete the entire tree'''
        self.data = None    #root node = None
        if self.left_child: 
            self.left_child = None  #left child of root node = None
        if self.right_child:
            self.right_child = None #right child of root node = None
        return 'Tree Successfully deleted'
        
drinks = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
drinks.left_child = hot
drinks.right_child = cold
tea = TreeNode("Tea")
coffee = TreeNode("coffee")
hot.left_child = tea
hot.right_child = coffee
cola = TreeNode("Cola")
fanta = TreeNode("Fanta")
cold.left_child = cola
cold.right_child = fanta

drinks.level_order()
drinks.insert('Milk Tea')
drinks.insert('Green Tea')
drinks.in_order()
print(drinks.get_deepest_node().data)