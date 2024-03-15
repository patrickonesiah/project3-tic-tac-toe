class Players:
    # def __init__(self, player, symbol):
    #     self.player = player
    #     self.symbol = symbol

    def set_name(self, name):
        self._name = name

    def set_symbol(self, symbol):
        self._symbol = symbol

    def get_name(self):
        return self._name

    def get_symbol(self):
        return self._symbol

    name = property(get_name, set_name,)
    symbol = property(get_symbol, set_symbol,)




# def function1():
#   print("Hello from a function")


# player class



# in terms of tic tac toe


# what should be made to a class?

# players


