'''
    Python file to implement the class CrewMate
'''

from heap import Heap

class CrewMate:
    '''
    Class to implement a crewmate
    '''

    def priority_comparison(self,tr1,tr2):
        if(tr1.priority < tr2.priority):
            return True
        elif(tr1.priority == tr2.priority):
            if(tr1.id < tr2.id):
                return True
            else:
                return False
        else:
            return False

    def arrival_comparison(self,tr1,tr2):
        if(tr1.arrival_time < tr2.arrival_time):
            return True
        else:
            return False
    
    def __init__(self):
        # self.id = id
        self.treasure_heap = Heap(self.arrival_comparison, [])
        self.curr_load = 0

        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        pass

    def insert_treasure(self,obj):
        if(self.curr_load < obj.arrival_time):
            self.curr_load = obj.arrival_time+obj.size
        else:
            self.curr_load+=obj.size
        self.treasure_heap.insert(obj)
    
    def process_treasures(self):
        new_heap = Heap(self.priority_comparison,[])
        first_tre = self.treasure_heap.heap_array[0]
        first_tre.initate_variable()
        new_heap.insert(first_tre)
        t1 = first_tre.arrival_time
        for tre in self.treasure_heap.heap_array[1:]:
            tre.initate_variable()
            t2 = tre.arrival_time
            while(t1!=t2):
                curr_tre = new_heap.top()
                if(curr_tre):
                    resp = curr_tre.do_processing(t1,t2)
                    if(resp == False):
                        t1 = t2
                    else:
                        curr_tre = new_heap.extract()
                        t1 = curr_tre.completion_time
                else:
                    t1 = t2
            new_heap.insert(tre)
        top_tre = new_heap.extract()
        while top_tre:
            top_tre.completion_time = t1 + top_tre.rem_size
            t1 = top_tre.completion_time
            top_tre = new_heap.extract()
        
        return self.treasure_heap.heap_array
            





        pass
    
    # Add more methods if required