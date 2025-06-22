from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        new_size = get_next_size()
        old_hash = self.hash_list
        self.table_size = new_size
        self.distinct_word_count = 0
        if(self.collision_type=='Chain'):
            self.hash_list = [[] for i in range(self.table_size)]
        else:
            self.hash_list = [None]*self.table_size

        for i in old_hash:
            if(i):
                if(self.collision_type=='Chain'):
                    for j in i:
                        self.insert(j)
                else:
                    self.insert(i)
        




        # IMPLEMENT THIS FUNCTION
        pass
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size = get_next_size()
        old_hash = self.hash_list
        self.table_size = new_size
        self.distinct_word_count = 0
        if(self.collision_type=='Chain'):
            self.hash_list = [[] for i in range(self.table_size)]
        else:
            self.hash_list = [None]*self.table_size

        for i in old_hash:
            if(i):
                if(self.collision_type=='Chain'):
                    for j in i:
                        self.insert(j)
                else:
                    self.insert(i)
        
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()