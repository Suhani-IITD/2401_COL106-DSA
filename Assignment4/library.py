import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.book_titles,self.texts = self.mergeSort(book_titles,texts)
        for i in range(len(self.book_titles)):
            self.texts[i],a = self.mergeSort(self.texts[i])
            
            
        
    
    def distinct_words(self, book_title):
        index = self.search(self.book_titles,0,len(self.book_titles),book_title)
        return self.texts[index]

    
    def count_distinct_words(self, book_title):
        index = self.search(self.book_titles,0,len(self.book_titles),book_title)
        return len(self.texts[index])

    
    def search_keyword(self, keyword):
        ans = []
        for i in range(len(self.book_titles)):
            if(self.search(self.texts[i],0,len(self.texts[i]),keyword)!=-1):
                ans.append(self.book_titles[i])
        return ans

    
    def print_books(self):
        for i in range(len(self.book_titles)):
            print(self.book_titles[i],end=': ')
            for j in self.texts[i][:-1]:
                print(j,end=' | ')
            print(self.texts[i][-1])
        

    def search(self,arr,l,r,key):
        if(len(arr[l:r])==1 and arr[0]!=key):
            return -1
        mid = (l+r)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]>key):
            return self.search(arr,l,mid,key)
        else:
            return self.search(arr,mid,r,key)

    def merge(self,lb,rb,lt,rt):
        i,j = 0,0
        book = []
        txt = []
        l,r = len(lb),len(rb)
        while(i<l and j<r):
            if(lb[i]<rb[j]):
                book.append(lb[i])
                if(lt):
                    txt.append(lt[i])
                i+=1
            elif(lb[i]>rb[j]):
                book.append(rb[j])
                if(rt):
                    txt.append(rt[j])
                j+=1
            else:
                book.append(lb[i])
                if(lt):
                    txt.append(lt[i])
                i+=1
                j+=1
        book.extend(lb[i:])
        book.extend(rb[j:])
        if(lt and rt):
            txt.extend(lt[i:])
            txt.extend(rt[j:])
       
        
        return book,txt

    def mergeSort(self,book_titles,texts=[]):
        if(len(book_titles)==1):
            return book_titles,texts
        mid = (len(book_titles))//2
        lb,lt = self.mergeSort(book_titles[:mid],texts[:mid])
        rb,rt = self.mergeSort(book_titles[mid:],texts[mid:]) 
        return self.merge(lb,rb,lt,rt)
 

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        self.params = params
        if(name == "Jobs"):
            self.collision_type = "Chain"
        elif(name == "Gates"):
            self.collision_type = "Linear"
        else:
            self.collision_type = "Double"
        
        self.hash_arr = ht.HashMap(self.collision_type,params)
        
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        pass
    
    def add_book(self, book_title, text):
        hs = ht.HashSet(self.collision_type,self.params)
        for i in text:
            hs.insert(i)
        self.hash_arr.insert((book_title,hs))
        
        
    
    def distinct_words(self, book_title):
        hs = self.hash_arr.find(book_title)
        ans = []
        for i in hs.hash_list:
            if(i):
                if(self.collision_type=="Chain"):
                    for j in i:
                        ans.append(j)
                else:
                    ans.append(i)
        return ans
    
    def count_distinct_words(self, book_title):
        return self.hash_arr.find(book_title).distinct_word_count
        
    
    def search_keyword(self, keyword):
        a = []
        if(self.collision_type=="Chain"):
            for i in self.hash_arr.hash_list:
                for j in i:
                    if(j[1].find(keyword)):
                        a.append(j[0])
                    
        else:
            for i in self.hash_arr.hash_list:
                if(i and i[1].find(keyword)):
                    a.append(i[0])
        return a


    
    def print_books(self):
        for i in self.hash_arr.hash_list : 
            if(self.collision_type=='Chain'):
                if(i):
                    for j in i:
                        print(j[0]+': '+j[1].__str__())
                        
            else:
                if(i):
                    print(i[0]+': '+i[1].__str__())
        pass