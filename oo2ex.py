class Store:
    def __init__(self, name):
        self.name=name
        self.items=[]
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        self.items.append({"name":name, "price":price})
        
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        tot =0
        for itm in self.items:
            tot+= itm['price'] #itm is Dictionary inise a list
        
        return tot
    
    def stock_price2(self): #compact method 
        return sum(  [ itm['price'] for itm in self.items ]   )
       
    
store = Store('mystore')
store.add_item('tool1', 123)
store.add_item('tool2', 222)
store.add_item('tool3', 333)

print(store.stock_price())
print(store.stock_price2())
