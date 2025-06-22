'''
    Python file to implement the Treasure class
'''

class Treasure:
    '''
    Class to implement a treasure
    '''
    
    def __init__(self, id, size, arrival_time):
        '''
        Arguments:
            id : int : The id of the treasure (unique positive integer for each treasure)
            size : int : The size of the treasure (positive integer)
            arrival_time : int : The arrival time of the treasure (non-negative integer)
        Returns:
            None
        Description:
            Initializes the treasure
        '''
        
        # DO NOT EDIT THE __init__ method
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None

    def initate_variable(self):
        self.rem_size = self.size
        self.priority = (self.arrival_time + self.rem_size)

    def do_processing(self,t1,t2):
        interval = t2-t1
        if(self.rem_size > interval):
            self.rem_size-=interval
            self.priority = (self.arrival_time + self.rem_size)
            return False
        elif(self.rem_size == interval):
            self.completion_time = t2
            self.rem_size = 0
            self.priority = (self.arrival_time + self.rem_size)
            return True
        else:
            self.completion_time = t1 + self.rem_size
            self.rem_size = 0
            self.priority = (self.arrival_time + self.rem_size)
            return True


    
    # You can add more methods if required