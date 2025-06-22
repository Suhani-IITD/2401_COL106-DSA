'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''

    def crew_compare(self,crew1,crew2):
        if(crew1.curr_load < crew2.curr_load):
            return True
        else:
            return False
    
    def __init__(self, m):
        self.empty_crew = []
        for i in range(m):
            self.empty_crew.append(CrewMate())
        self.crew_heap = Heap(self.crew_compare,[])


        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        pass
    
    def add_treasure(self, treasure):
        treasure_obj = Treasure(treasure.id,treasure.size,treasure.arrival_time)
        if(self.empty_crew):
            crew = self.empty_crew.pop(0)
        else:
            crew = self.crew_heap.extract()
        crew.insert_treasure(treasure_obj)
        self.crew_heap.insert(crew)
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
       
    
    def get_completion_time(self):
        ans_list = []
        for crew in self.crew_heap.heap_array:
            a = crew.process_treasures()
            ans_list.extend(a)
        ans_list.sort(key = lambda tre_obj:tre_obj.id)
        return ans_list



        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        pass
    
    # You can add more methods if required