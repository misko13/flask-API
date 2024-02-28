class Device:
    def __init__(self, name, connected_by) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self) -> str:
        return f'Device : {self.name!r}  ( {self.connected_by})'
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")

""" inherited class: extend the existing class  """
class Printer(Device): #new clas Printer INHERITS from Device class
    def __init__(self, name, connected_by, capacity) -> None:
        super().__init__(name, connected_by)  # inherits all --init-- from Device
        self.capacity= capacity
        self.remaining_pages = capacity

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.remaining_pages} pages rimaining)"
    
    def runprint(self, pages):
        if not self.connected:
            print("printer is offline")
            return
        print(f"Printer is printing {pages} pages.")
        self.remaining_pages -= pages

#prn1 = Device("Printer", "USB")
#print(prn1)
#prn1.disconnect()

prn1 = Printer("Printer", "USB", 1000)
print(prn1)
prn1.runprint(20)
print(prn1)
prn1.disconnect()
