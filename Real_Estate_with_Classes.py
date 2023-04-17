class House:
    def __init__(self, num_rooms, year_built, city, type="S"):
        self.num_rooms = num_rooms
        self._year_built = year_built
        self.city = city
        self._type = type

    @property
    def year_built(self):
        return self._year_built

    @year_built.setter
    def year_built(self, value):
        if value <= 0 or value >= 2023:
            ValueError("The year has to be between 0 and 2023 inclusive.")
        self._year_built = value

    def __str__(self):
        if self._type == "S":
            house_type = "Single"
        else:
            house_type = "Multi"
        return f"{house_type}-Family house with {self.num_rooms} rooms located in {self.city} was built in {self._year_built}."

    @property
    def age(self):
        return 2023 - self._year_built

    def __gt__(self, other):
        if isinstance(other, int):
            return self._year_built > other
        elif isinstance(other, str):
            return self.city > other
        elif isinstance(other, House):
            return self.num_rooms > other.num_rooms


class Duplex(House):
    def __init__(self, num_rooms, year_built, city):
        super().__init__(num_rooms, year_built, city, type="M")
        self.num_units = 2

    def __add__(self, other):
        if isinstance(other, tuple):
            num_rooms = self.num_rooms + other[0]
            year_built = max(self._year_built, other[1])
            city = self.city
            return (num_rooms, year_built, city)

    def __iadd__(self, other):
        if isinstance(other, tuple):
            self.num_rooms += other[0]
            self._year_built = max(self._year_built, other[1])
        return self


house1 = House(4, 2020, "Boston", "M")
house2 = Duplex(6, 2022, "Chelsea")


print(f"\n{house1}\n")
print(f"\n{house2}\n")