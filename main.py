class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

## don't touch above this line

class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows
        
        
    def get_num_arrows(self):
        return self.__num_arrows
    
    def use_arrows(self, num):
        self.__num_arrows -= num
        if self.__num_arrows < 0:
            self.__num_arrows += num
            raise Exception("not enough arrows")    
        
class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)
        
    def triple_shot(self, target):
        self.use_arrows(3)
        return f"{target.get_name()} was shot by 3 crossbow bolts"
    
def main():

    human1 = Human("Derek")
    archer1 = Archer(human1.get_name(),4)
    crossbowman1 = Crossbowman("Tim", 5)
    print(f"Archer name inheritance from class Human: {human1.get_name()}")
    print(f"Archer's arrows number : {archer1.get_num_arrows()}")
    print(f"Crossbowman name inheritance from class Archer: {crossbowman1.get_name()}")
    print(f"Crossbowman's bolts number inheritance from class Archer: {crossbowman1.get_num_arrows()}")

main()
