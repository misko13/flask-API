class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __repr__(self) -> str:
        return self.name

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        new_store = cls(store.name + ' - francihise')# same as calling: new_store = Store(some name) !!
        return new_store
       

    @staticmethod
    def store_details(store):
       # return(f"{store.name} total price: {int(store.stock_price())}" )  # OK too
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
 
print(Store.franchise(store) ) # returns a Store with name "Test - franchise"
print(Store.franchise(store2) )  # returns a Store with name "Amazon - franchise"
 
print(Store.store_details(store) )  # returns "Test, total stock price: 0"
print(Store.store_details(store2))  # returns "Amazon, total stock price: 160"