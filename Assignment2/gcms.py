from bin import Bin
from node import Node
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException


def comp_2(node_1, node_2):
    if(node_2.data < node_1.data):
        return -1
    elif(node_2.data == node_1.data):
        if(node_2.other > node_1.other):
            return -1
        elif(node_2.other == node_1.other):
            return 0
        else:
            return 1
    else:
        return 1

class GCMS:
    def __init__(self):
        self.bins_cap_blgr = AVLTree()
        self.bins_cap_ylrd = AVLTree(comp_2)
        self.bins_id = AVLTree()
        self.object_avl = AVLTree()

        # Maintain all the Bins and Objects in GCMS
        pass 


    def add_bin(self, bin_id, capacity):
        new_bin = Bin(bin_id, capacity)
        node_id = Node(data=new_bin.bin_id,object=new_bin,other=new_bin.capacity)
        node_cap1 = Node(data=new_bin.capacity,object=new_bin,other=new_bin.bin_id)
        node_cap2 = Node(data=new_bin.capacity,object=new_bin,other=new_bin.bin_id)
        self.bins_id.root = self.bins_id.insert(self.bins_id.root,node_id)
        self.bins_cap_blgr.root = self.bins_cap_blgr.insert(self.bins_cap_blgr.root,node_cap1)
        self.bins_cap_ylrd.root = self.bins_cap_ylrd.insert(self.bins_cap_ylrd.root,node_cap2)

        

    def add_object(self, object_id, size, color):
        new_obj = Object(object_id,size,color)
        if(new_obj.color==1):
            obj_bin = self.blueCargo(new_obj)
        elif(new_obj.color==2):
            obj_bin = self.yellowCargo(new_obj)
        elif(new_obj.color==3):
            obj_bin = self.redCargo(new_obj)
        else:
            obj_bin = self.greenCargo(new_obj)

        if(obj_bin):
            bin1 = Node(obj_bin.data,obj_bin.obj,obj_bin.other)
            bin2 = Node(obj_bin.data,obj_bin.obj,obj_bin.other)
            b = obj_bin.obj
            self.bins_cap_blgr.root = self.bins_cap_blgr.delete(self.bins_cap_blgr.root,bin1)
            self.bins_cap_ylrd.root = self.bins_cap_ylrd.delete(self.bins_cap_ylrd.root,bin2)
            b.add_object(new_obj)
            new_bin_node1 = Node(b.capacity,b,b.bin_id)
            new_bin_node2 = Node(b.capacity,b,b.bin_id)
            self.bins_cap_blgr.root = self.bins_cap_blgr.insert(self.bins_cap_blgr.root,new_bin_node1)
            self.bins_cap_ylrd.root = self.bins_cap_ylrd.insert(self.bins_cap_ylrd.root,new_bin_node2)
            obj_node = Node(data=new_obj.obj_id,object=new_obj,other=new_obj.size)
            self.object_avl.root = self.object_avl.insert(self.object_avl.root,obj_node)
            new_node = Node(b.capacity,b,b.bin_id)
            new_obj.container_bin = new_node
            # print('obj ki bin ka size: ',new_obj.container_bin.data)
        else:
            raise NoBinFoundException

    def delete_object(self, object_id):
        found_object = self.object_avl.searchinTree(self.object_avl.root,object_id)
        if(found_object is None):
            return None
        # print('object_id is ',object_id)
        node_to_delete = found_object
        found_obj = found_object.obj
        self.object_avl.root = self.object_avl.delete(self.object_avl.root,node_to_delete)
        parent_bin_node = found_obj.container_bin
        parent_bin = parent_bin_node.obj
        parent_bin_node1 = Node(parent_bin.capacity,parent_bin_node.obj,parent_bin_node.other)
        parent_bin_node2 = Node(parent_bin.capacity,parent_bin_node.obj,parent_bin_node.other)
        # print('i',object_id,parent_bin_node1.data,parent_bin_node1.other)
        # print(self.bin_info(parent_bin_node1.other))
        # print(self.bins_cap_blgr.traverse(self.bins_cap_blgr.root))
        # print('traversing before ',self.bins_cap_blgr.traverse(self.bins_cap_blgr.root))
        self.bins_cap_blgr.root = self.bins_cap_blgr.delete(self.bins_cap_blgr.root,parent_bin_node1)
        # print('traversing after removal ',self.bins_cap_blgr.traverse(self.bins_cap_blgr.root))
        self.bins_cap_ylrd.root = self.bins_cap_ylrd.delete(self.bins_cap_ylrd.root,parent_bin_node2)
        # print('old cap',parent_bin.capacity)
        parent_bin.remove_object(object_id)
        # print('new cap',parent_bin.capacity)
        bin_node1 = Node(parent_bin.capacity,parent_bin_node.obj,parent_bin_node.other)
        bin_node2 = Node(parent_bin.capacity,parent_bin_node.obj,parent_bin_node.other)
        self.bins_cap_blgr.root = self.bins_cap_blgr.insert(self.bins_cap_blgr.root,bin_node1)
        self.bins_cap_ylrd.root = self.bins_cap_ylrd.insert(self.bins_cap_ylrd.root,bin_node2)
        # print('traversing after addition ',self.bins_cap_blgr.traverse(self.bins_cap_blgr.root))


    def bin_info(self, bin_id):
        found_bin = self.bins_id.searchinTree(self.bins_id.root,bin_id)
        found_bin = found_bin.obj
        cap = found_bin.capacity
        element_tree = found_bin.objects
        element_list = element_tree.traverse(element_tree.root)
        return((cap,element_list))

    def object_info(self, object_id):
        found_object = self.object_avl.searchinTree(self.object_avl.root,object_id)
        if(found_object is None):
            return None
        found_obj = found_object.obj
        parent_bin_node = found_obj.container_bin
        # print('found connected obj:',parent_bin_node.data,parent_bin_node.other)
        parent_bin = parent_bin_node.obj
        # print('found : ',parent_bin.capacity)
        return parent_bin.bin_id
        

    def blueCargo(self, object):
        find_capacity = object.size
        obj_bin = self.bins_cap_blgr.compact_fit_minid(self.bins_cap_blgr.root,find_capacity)
        return obj_bin
    
    def yellowCargo(self, object):
        find_capacity = object.size
        obj_bin = self.bins_cap_ylrd.compact_fit_maxid(self.bins_cap_ylrd.root,find_capacity)
        return obj_bin
    
    def redCargo(self, object):
        find_capacity = object.size
        obj_bin = self.bins_cap_ylrd.largest_fit_minid(self.bins_cap_ylrd.root,find_capacity)
        return obj_bin
    
    def greenCargo(self, object):
        find_capacity = object.size
        obj_bin = self.bins_cap_blgr.largest_fit_maxid(self.bins_cap_blgr.root,find_capacity)
        return obj_bin

    
    