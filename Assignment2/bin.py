from avl import AVLTree
from node import Node

class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.objects = AVLTree()
        pass

    def add_object(self, object):
        node = Node(object.obj_id,object,object.size)
        self.objects.root = self.objects.insert(self.objects.root,node)
        self.capacity-=object.size


    def remove_object(self, object_id):
        node = self.objects.searchinTree(self.objects.root,object_id)
        a=node.other
        self.objects.root = self.objects.delete(self.objects.root,node)
        self.capacity+=a

        # Implement logic to remove an object by ID
        pass
