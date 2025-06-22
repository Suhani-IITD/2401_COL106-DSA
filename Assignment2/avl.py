from node import Node

def comp_1(node_1, node_2):
    if(node_2.data < node_1.data):
        return -1
    elif(node_2.data == node_1.data):
        if(node_2.other < node_1.other):
            return -1
        elif(node_2.other == node_1.other):
            return 0
        else:
            return 1
    else:
        return 1


class AVLTree:
    def __init__(self, compare_function = comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def height_node(self,node):
        if(node is None):
            return 0
        else:
            return node.height
        
    def rrotate(self,n):
        p = n.left
        c = p.right
        p.right = n
        n.left = c
        n.height = 1 + max(self.height_node(n.left),self.height_node(n.right))
        p.height = 1 + max(self.height_node(p.left),self.height_node(p.right))
        return p
    
    def lrotate(self,n):
        p = n.right
        c = p.left
        p.left = n
        n.right = c
        n.height = 1 + max(self.height_node(n.left),self.height_node(n.right))
        p.height = 1 + max(self.height_node(p.left),self.height_node(p.right))
        return p


    def insert(self,root,node):
        if(root is None):
            return node
        step = self.comparator(root,node)
        if(step==-1):
            root.left = self.insert(root.left,node)
        else:
            root.right = self.insert(root.right,node)
        
        root.height = 1 + max(self.height_node(root.left),self.height_node(root.right))
        diff = self.height_node(root.right) - self.height_node(root.left)

        if(-1<=diff and diff<=1):
            return root
        elif(diff<-1):
            diff2 = self.comparator(root.left,node)
            if(diff2==-1):
                root = self.rrotate(root)
            else:
                root.left = self.lrotate(root.left)
                root = self.rrotate(root)
        elif(diff > 1):
            diff2 = self.comparator(root.right,node)
            if(diff2==1):
                root = self.lrotate(root)
            else:
                root.right = self.rrotate(root.right)
                root = self.lrotate(root)
        return root
    
    def compact_fit_minid(self,root,cap,curr_node = None):
        if(root is None):
            return curr_node
        if(root.data >= cap):
            if(curr_node and curr_node.data < root.data):
                curr_node = self.compact_fit_minid(root.left,cap,curr_node)
            else:
                curr_node = self.compact_fit_minid(root.left,cap,root)
        else:
            curr_node = self.compact_fit_minid(root.right,cap,curr_node)
        return curr_node
    
    def searchinTree(self,root,data):
        if(root is None):
            return None
        if(root.data == data):
            return root
        elif(root.data > data):
            return self.searchinTree(root.left,data)
        else:
            return self.searchinTree(root.right,data)
    
    def traverse(self,root):
        a = []
        if(root is None):
            return []
        if(root.left):
            a.extend(self.traverse(root.left))
        a.append(root.data)
        if(root.right):
            a.extend(self.traverse(root.right))
        return a
    
    
    def leftmost_node(self,root):
        while(root.left is not None):
            root = root.left
        return root  

    
    
    def delete(self,root,node):
        step = self.comparator(root,node)
        if(step == -1):
            root.left = self.delete(root.left,node)
        elif(step == 1):
            root.right = self.delete(root.right,node)
        else:
            if(root.left is None and root.right is None):
                root = None
            elif(root.left is None):
                root = root.right
            elif(root.right is None):
                root = root.left
            else:
                new_par = self.leftmost_node(root.right)
                root.data = new_par.data
                root.other = new_par.other
                root.obj = new_par.obj
                root.right = self.delete(root.right,new_par)
        
        if(root is None):
            return root
        else:
            root.height = 1 + max(self.height_node(root.right),self.height_node(root.left))
            diff = self.height_node(root.right) - self.height_node(root.left)
            if(-1<=diff and diff<=1):
                return root
            elif(diff<-1):
                diff2 = self.height_node(root.left.right) - self.height_node(root.left.left)
                if(diff2==-1 or diff2 == 0):
                    root = self.rrotate(root)
                elif(diff2==1):
                    root.left = self.lrotate(root.left)
                    root = self.rrotate(root)
            elif(diff > 1):
                diff2 = self.height_node(root.right.right) - self.height_node(root.right.left)
                if(diff2==1 or diff2==0):
                    root = self.lrotate(root)
                else:
                    root.right = self.rrotate(root.right)
                    root = self.lrotate(root)
        return root
        

    def compact_fit_maxid(self,root,cap,curr_node = None):
        if(root is None):
            return curr_node
        if(root.data >= cap):
            if(curr_node and curr_node.data < root.data):
                curr_node = self.compact_fit_maxid(root.left,cap,curr_node)
            else:
                curr_node = self.compact_fit_maxid(root.left,cap,root)
        else:
            curr_node = self.compact_fit_maxid(root.right,cap,curr_node)
        return curr_node
    
    def largest_fit_minid(self,root,cap,curr_node = None):
        if(root is None):
            return curr_node
        if(root.data >= cap):
            curr_node = self.largest_fit_minid(root.right,cap,root)
        else:
            curr_node = self.largest_fit_minid(root.right,cap,curr_node)
        return curr_node
    
    def largest_fit_maxid(self,root,cap,curr_node = None):
        if(root is None):
            return curr_node
        if(root.data >= cap):
            curr_node = self.largest_fit_maxid(root.right,cap,root)
        else:
            curr_node = self.largest_fit_maxid(root.right,cap,curr_node)
        return curr_node
    





        
        


    




        


        


    