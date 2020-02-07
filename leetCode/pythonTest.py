class CargoShip:  
    def __init__(self, capacity):
        self.cargo = []
        self.capacity = capacity
        
    def unload(self, port):
        """
        :param port: (String)
        :returns: [(String, Int)]
        """
        for items in self.cargo:
            if port == items[0]:
                self.cargo.remove(items)
                break
        return self
    
    def can_depart(self):
        """
        :returns: (Bool)
        """
        sum = 0
        for items in self.cargo:
            sum += items[1]
        if (sum <= self.capacity ):
            return True
        else:
            return False
    
    def load(self, new_cargo):
        """
        :param new_cargo: [(String, Int)]
        """
        for value in new_cargo:
            self.cargo.append(value)
        return self
    

ship = CargoShip(19)
ship.load([("New York", 1), ("London", 20)])
print(ship.cargo)
print(ship.unload("New York")) #should print [("New York", 1)]
print(ship.cargo) #should print [("London", 20)]
print(ship.can_depart()) #should print False