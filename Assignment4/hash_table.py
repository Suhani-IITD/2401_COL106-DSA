from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        self.params = params
        self.table_size = params[-1]
        self.z = params[0]
        self.collision_type = collision_type
        self.distinct_word_count = 0
        if(collision_type == "Chain"):
            #chaining
            self.hash_list = [[] for i in range(self.table_size)]
            
        elif(collision_type == "Linear"):
            self.hash_list = [None]*self.table_size
            pass
        else:
            self.hash_list = [None]*self.table_size
            self.z2 = params[1]
            self.c2 = params[2]
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
    
    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        z = self.z
        if(key[-1].islower()):
            p = (ord(key[-1])-97)
        else:
            p = (ord(key[-1])-39)

        for i in range(len(key)-2,-1,-1):
            p*=z
            if(key[i].islower()):
                p += (ord(key[i])-97)
            else:
                p+= (ord(key[i])-39)
        hash_val = p % self.table_size
        return hash_val
    
    def get_load(self):
        n = self.distinct_word_count
        t = self.table_size
        return n/t

    
    def __str__(self):
        pass

    def double_hash_funct(self,key):
        z = self.z2
        if(key[-1].islower()):
            p = (ord(key[-1])-97)
        else:
            p = (ord(key[-1])-39)

        for i in range(len(key)-2,-1,-1):
            p*=z
            if(key[i].islower()):
                p+= (ord(key[i])-97)
            else:
                p+= (ord(key[i])-39)
        p = p%self.c2
        return self.c2 - p        


    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):

    def __init__(self, collision_type, params):
        # self.distinct_word_count = 0
        # self.distinct_list = []
        super().__init__(collision_type,params)
        pass
    
    def insert(self, key):
        hash_code = super().get_slot(key)
        if(self.collision_type == "Chain"):
            if (self.hash_list[hash_code] == None):
                self.hash_list[hash_code].append(key)
                self.distinct_word_count+=1
            else:
                for i in self.hash_list[hash_code]:
                    if(i==key):
                        return
                else:
                    self.hash_list[hash_code].append(key)
                    
                    self.distinct_word_count+=1
            return
        
        elif(self.collision_type == "Linear"):
            i = 0
            while(i<self.table_size):
                if(self.hash_list[hash_code]==key):
                    return
                elif(self.hash_list[hash_code] == None):
                    self.hash_list[hash_code] = key
                    
                    self.distinct_word_count+=1
                    return
                else:
                    i+=1
                    hash_code = (hash_code+1)%self.table_size
            else:
                raise Exception("Table is full")
        else:
            hash_code2 = self.double_hash_funct(key)
            i = 0
            probe = 0
            fin_hash_code = (hash_code + (probe*hash_code2))%self.table_size
            while(i<self.table_size):
                if(self.hash_list[fin_hash_code]==key):
                    return
                elif(self.hash_list[fin_hash_code]==None):
                    self.hash_list[fin_hash_code]= key
                    
                    self.distinct_word_count+=1
                    return 
                else:
                    probe+=1
                    i+=1
                    fin_hash_code = (hash_code + (probe*hash_code2))%self.table_size
            else:
                raise Exception("Table is full")
        pass
    
    def find(self, key):
        hash_code = super().get_slot(key)
        if(self.collision_type == "Chain"):
            for i in self.hash_list[hash_code]:
                if(i==key):
                    return True
            else:
                return False
        elif(self.collision_type == "Linear"):
            i = 0
            while(i<self.table_size):
                if(self.hash_list[hash_code] == key):
                    return True
                else:
                    i+=1
                    hash_code = (hash_code+1)%self.table_size
            else:
                return False
        else:
            hash_code2 = self.double_hash_funct(key)
            i = 0
            probe = 0
            fin_hash_code = (hash_code + (probe*hash_code2))%self.table_size
            while(i<self.table_size):
                if(self.hash_list[fin_hash_code]==key):
                    return True
                else:
                    probe+=1
                    i+=1
                    fin_hash_code = (hash_code + (probe*hash_code2))%self.table_size
            else:
                return False

    
    def get_slot(self, key):
        return super().get_slot(key)
        pass
    
    def get_load(self):
        
        return super().get_load()
    
    def __str__(self):
        s = []
        if(self.collision_type == "Chain"):
            for i in range(len(self.hash_list)):
                if(self.hash_list[i]):
                    x = []
                    for j in range(len(self.hash_list[i])):
                        x.append(self.hash_list[i][j])
                    s.append(' ; '.join(x)) 
                else:
                    s.append('<EMPTY>')
            
        else:
            for i in range(len(self.hash_list)):
                if(self.hash_list[i]):
                    s.append(self.hash_list[i])
                else:
                    s.append("<EMPTY>")
        return ' | '.join(s)            
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type,params)
        pass
    
    def insert(self, x):
        # x = (key, value)
        hash_code = super().get_slot(x[0])
        if(self.collision_type == "Chain"):
            self.hash_list[hash_code].append(x)
            self.distinct_word_count+=1
        elif(self.collision_type == "Linear"):
            i = 0
            while(i<self.table_size):
                if(self.hash_list[hash_code] == None):
                    self.hash_list[hash_code] = x
                    self.distinct_word_count+=1
                    return
                elif(self.hash_list[hash_code][0]==[x[0]]):
                    self.hash_list[hash_code] = x
                else:
                    i+=1
                    hash_code = (hash_code+1)%self.table_size
            else:
                raise Exception("Table is full")
        else:
            hash_code2 = self.double_hash_funct(x[0])
            i = 0
            probe = 0
            fin_hash_code = (hash_code + (probe*hash_code2))%self.table_size
            while(i<self.table_size):
                if(self.hash_list[fin_hash_code]==None):
                    self.hash_list[fin_hash_code]= x
                    self.distinct_word_count+=1
                    return
                else:
                    probe+=1
                    i+=1
                    fin_hash_code = (hash_code + (probe*hash_code2))%self.table_size
            else:
                raise Exception("Table is full")
        pass
    
    def find(self, key):
        hash_code = super().get_slot(key)
        if(self.collision_type == "Chain"):
            for i in self.hash_list[hash_code]:
                if(i[0]==key):
                    return i[1]
        elif(self.collision_type == "Linear"):
            i = 0
            while(i<self.table_size):
                if(self.hash_list[hash_code][0] == key):
                    return self.hash_list[hash_code][1]
                else:
                    i+=1
                    hash_code = (hash_code+1)%self.table_size
            else:
                return None
        else:
            hash_code2 = self.double_hash_funct(key)
            i = 0
            probe = 0
            fin_hash_code = (hash_code + (probe*hash_code2))%self.table_size
            while(i<self.table_size):
                if(self.hash_list[fin_hash_code][0]==key):
                    return self.hash_list[fin_hash_code][1]
                else:
                    probe+=1
                    i+=1
                    fin_hash_code = (hash_code + (probe*hash_code2))%self.table_size
            else:
                return None

    
    def get_slot(self, key):
        return super().get_slot(key)
        pass
    
    def get_load(self):
        return super().get_load()
    
    def __str__(self):
        s = []
        for i in range(len(self.hash_list)):
            if(self.collision_type=='Chain'):
                if(self.hash_list[i]):
                    x=[]
                    for j in range(len(self.hash_list[i])):
                        x.append(str(self.hash_list[i][j]))
                    s.append(' ; '.join(x))
                else:
                    s.append('<EMPTY>')
            else:
                if(self.hash_list[i]):
                    s.append(str(self.hash_list[i]))
                else:
                    s.append('<EMPTY>')
        return ' | '.join(s)
                

        pass