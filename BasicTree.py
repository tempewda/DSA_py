#Program to represent a basic tree and how its children are added

class TreeNode:
    def __init__(self, data, children = None):
        if children is None:
            children = []
        self.data = data
        self.children = children

    def __str__(self, level = None):
        if level is None:
            level = 0
        result = ' ' * level + str(self.data) + '\n'
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def addChild(self, child):
        self.children.append(child)

drinks = TreeNode('Drinks')
hot = TreeNode('Hot')
cold = TreeNode('Cold')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
cola = TreeNode('Cola')
mazaa = TreeNode('Mazaa')
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(mazaa)
drinks.addChild(hot)
drinks.addChild(cold)
print(drinks)
