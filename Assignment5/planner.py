from flight import Flight


class Planner:
    class Heap:
        

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
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.flights = flights
        self.flight_adj_list = []
        self.n = 0
        for i in flights:
            if(i.start_city>self.n):
                self.n = i.start_city
            if(i.end_city > self.n):
                self.n = i.end_city
        for i in range(self.n+1):
            self.flight_adj_list.append([])
        for i in flights:
            i.init_vis()
            self.flight_adj_list[i.start_city].append(i)
        pass
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        
        for i in self.flights:
            i.visited = False
            i.prev = None
            i.lvl = 0
        q = []
        ans = []
        found = False
        for i in self.flight_adj_list[start_city]:
            if(i.departure_time>=t1 and i.arrival_time<=t2 and i.visited!=True):
                if(i.end_city == end_city):
                    ans.append(i)
                    i.lvl+=1
                    found = True
                    i.visited = True
                elif(not found):
                    q.append(i)
                    i.lvl+=1
                    i.visited = True
        
        if(not found):
            while q!=[]:
                cur_flight = q.pop(0)
                ct = cur_flight.arrival_time + 20
                for i in self.flight_adj_list[cur_flight.end_city]:
                    if(i.departure_time>=ct and i.arrival_time<=t2 and i.visited!=True):
                        if(i.end_city == end_city):
                            i.prev = cur_flight
                            i.lvl = cur_flight.lvl+1
                            if(found):
                                if(i.lvl<=min_step):
                                    ans.append(i)
                            else:
                                found = True
                                ans.append(i)
                                min_step = i.lvl
                            i.visited = True
                        elif(found==False):
                            i.prev = cur_flight
                            i.lvl = cur_flight.lvl+1
                            q.append(i)
                            i.visited = True
                        
        
        res = []
        
        if(found):
            et = t2
            min_step = ans[0].lvl
            for i in ans:
                if(i.lvl<min_step):
                    res=i
                    et = i.arrival_time
                    min_step = i.lvl
                elif(i.lvl == min_step):
                    if(i.arrival_time <= et):
                        res=i
                        et = i.arrival_time
                        min_step = i.lvl


        r = []
        
        if(found):
            while res:
                r.append(res)
                res = res.prev
            return r[::-1]
        else:
            return []
        

    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        for i in self.flights:
            i.visited = False
            i.prev = None
        def comp(fl1,fl2):
            if(fl1[1] < fl2[1]):
                return True
            else:
                return False
        priority_heap = self.Heap(comp,[])
        found = False
        
        for i in self.flight_adj_list[start_city]:
            if(i.departure_time>=t1 and i.arrival_time<=t2):
                priority_heap.insert((i,i.fare))
                i.visited = True

        while priority_heap.heap_array!=[]:
            flt,cost = priority_heap.extract()
            if(flt.end_city==end_city):
                found = True
                ans = flt
                break
                
            for i in self.flight_adj_list[flt.end_city]:
                if(i.visited!=True):
                    if(i.departure_time>=(flt.arrival_time + 20) and i.arrival_time<=t2):
                        i.prev = flt
                        total_cost = cost + i.fare
                        priority_heap.insert((i,total_cost))
                        i.visited = True

        r = []
        if(found):
            while ans:
                r.append(ans)
                ans = ans.prev
        return r[::-1]


        pass
    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """

        for i in self.flights:
            i.visited = False
            i.prev = None
            i.lvl = 0

        def comp1(fl1,fl2):
            if(fl1[1] < fl2[1]):
                return True
            elif(fl1[1]==fl2[1] and fl1[2] < fl2[2]):
                return True
            else:
                return False
            
        priority_heap = self.Heap(comp1,[])
        arr = []
        found = False
        for i in range(self.n+1):
            arr.append(float('inf'))
        arr[start_city] = 0

        for i in self.flight_adj_list[start_city]:
            if(i.departure_time>=t1 and i.arrival_time <= t2):
                arr[i.end_city] = i.fare
                i.lvl+=1
                priority_heap.insert((i,i.lvl,i.fare))
                i.visited = True
        

        while priority_heap.heap_array!=[]:
            flt,lvl,cost = priority_heap.extract()
            if(flt.end_city==end_city):
                found = True
                ans = flt
                break
            for i in self.flight_adj_list[flt.end_city]:
                if(i.visited!=True):
                    i.prev = flt
                    if(i.departure_time>=(flt.arrival_time + 20) and i.arrival_time<=t2):
                        i.lvl = lvl+1
                        priority_heap.insert((i,i.lvl,cost+i.fare)) 
                        i.visited = True
        r = []
        if(found):
            while ans:
                r.append(ans)
                ans = ans.prev
        return r[::-1]
        
        pass