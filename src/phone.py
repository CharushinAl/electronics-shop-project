from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = int(number_of_sim)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise None

    @staticmethod
    def valid_number_of_sim(number_of_sim):
        try:
            number_of_sim = int(number_of_sim)
            if number_of_sim <= 0:
                raise ValueError("The number of physical SIM cards must be an integer greater than zero.")
            return number_of_sim
        except ValueError:
            raise ValueError("The number of physical SIM cards must be an integer greater than zero.")
