class Item:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
        if self.price==0:
            raise ValueError('Invalid value for price, got 0')
        if self.price<0:
            raise ValueError('Invalid value for price, got {}'.format(self.price))
    def __str__(self):
        return '{}@{}-{}'.format(self.name,self.price,self.category)
        
class Query:
    def __init__(self,field,operation,value):
        self.field=field
        self.operation=operation
        operations=['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if operation not in operations:
            raise ValueError('Invalid value for operation, got {}'.format(self.operation))
        self.value=value
    def __str__(self):
        return '{} {} {}'.format(self.field,self.operation,self.value)
        
class Store:
    def __init__(self):
        self.list_items=[]
        
    def count(self):
        return len(self.list_items)

    def add_item(self,item):
        self.list_items.append(item)
    
    def __str__(self):
        if len(self.list_items)>0:
           return '\n'.join(map(str,self.list_items))
        else:
            return 'No items'
        
    def filter(self,query):
        li=Store()

        if query.operation=='EQ':
            for i in self.list_items:
                if query.value==i.name:
                    li.add_item(i)
                elif query.value==i.price:
                    li.add_item(i)
                elif query.value==i.category:
                    li.add_item(i)
            return li
            
        '''for i in self.list_items:
            val=getattr(i,query.field)
            if query.operation=='EQ' and val==query.value: 
                li.add_item(i)
            if query.operation=='IN' and val in query.value: 
                li.add_item(i)
            if query.operation=='GT' and val>query.value: 
                li.add_item(i)
            if query.operation=='EQ' and val==query.value: 
                    li.add_item(i)'''    
                
                
                
                
        elif query.operation=='IN':
            for i in self.list_items:
                if i.name in query.value:
                    li.add_item(i)
                elif i.price in query.value:
                    li.add_item(i)
                elif i.category in query.value:
                    li.add_item(i)
            return li

        elif query.operation=='GT':
            for i in self.list_items:
                if query.value<i.price:
                    li.add_item(i)
            return li    
     
        elif query.operation=='GTE':
            for i in self.list_items:
                if query.value<=i.price:
                    li.add_item(i)
            return li   
            
        elif query.operation=='LT':
            for i in self.list_items:
                if query.value>i.price:
                    li.add_item(i)
            return li   
        elif query.operation=='LTE':
            for i in self.list_items:
                if query.value>=i.price:
                    li.add_item(i)
            return li  
            
        elif query.operation=="STARTS_WITH":
            for i in self.list_items:
                if i.name.startswith(query.value):
                    li.add_item(i)
                if i.category.startswith(query.value):
                    li.add_item(i)
            return li
        
        elif query.operation=="ENDS_WITH":
            for i in self.list_items:
                if i.name.endswith(query.value):
                    li.add_item(i)
                if i.category.endswith(query.value):
                    li.add_item(i)
            return li
        
        elif query.operation=='CONTAINS':
            for i in self.list_items:
                if query.field=='name':
                   if i.name.__contains__(query.value):
                       li.add_item(i)
                if query.field=='category':
                    if i.category.__contains__(query.value):
                        li.add_item(i)
            return li
    
    def exclude(self,query):
        exclude_items=Store()
        filter=self.filter(query)
        for i in self.list_items:
            if i not in filter.list_items:
                exclude_items.add_item(i)
        return exclude_items
        
    
        
            