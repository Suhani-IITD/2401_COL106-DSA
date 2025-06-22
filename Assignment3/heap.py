'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''

    def get_parent(self,index):
        return (index-1)//2
    
    def get_leftChild(self,index):
        return (2*index)+1
    
    def get_rightChild(self,index):
        return (2*index)+2
    
    def down_heap(self,indx_parent):
        parent = self.heap_array[indx_parent]
        l = len(self.heap_array)
        indx_lc = self.get_leftChild(indx_parent)
        if(indx_lc<l):
            lChild = self.heap_array[indx_lc]
            minChild  = lChild
            indx_minChild = indx_lc
            indx_rc = self.get_rightChild(indx_parent)
            if(indx_rc<l):
                rChild = self.heap_array[indx_rc]
                comp_result = self.comparator(lChild,rChild)
                if(not comp_result):
                    minChild = rChild
                    indx_minChild = indx_rc
            
            comp_result = self.comparator(parent,minChild)
            if(not comp_result):
                self.heap_array[indx_parent],self.heap_array[indx_minChild] = minChild,parent
                self.down_heap(indx_minChild)
        else:
            return
        
    def up_heap(self,indx_child):
        indx_parent = self.get_parent(indx_child)
        if(indx_parent<0):
            return
        parent = self.heap_array[indx_parent]
        child = self.heap_array[indx_child]
        comp_result = self.comparator(parent,child)
        if(not comp_result):
            self.heap_array[indx_parent],self.heap_array[indx_child] = self.heap_array[indx_child],self.heap_array[indx_parent]
            self.up_heap(indx_parent)
        else:
            return


        
    
    def __init__(self, comparison_function, init_array):
        self.comparator = comparison_function
        self.heap_array = init_array
        l = len(self.heap_array)
        if(l==0 or l==1):
            return
        
        p = self.get_parent(l-1)
        for i in range(p,-1,-1):
            self.down_heap(i)

        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        pass
        
    def insert(self, value):
        self.heap_array.append(value)
        self.up_heap(len(self.heap_array)-1)
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        pass
    
    def extract(self):
        if(self.heap_array == []):
            return None
        ele = self.heap_array[0]
        self.heap_array[0] = self.heap_array[-1]
        self.heap_array.pop(-1)
        if(self.heap_array!=[]):
           self.down_heap(0)
        return ele
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        pass
    
    def top(self):
        if(self.heap_array):
            return self.heap_array[0]
        else:
            return None
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        pass
    
    # You can add more functions if you want to