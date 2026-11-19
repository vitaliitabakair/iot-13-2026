from enum import Enum, auto


class ClothingType(Enum):
    SHIRT = auto()
    JEANS = auto()
    JACKET = auto()
    SWEATER = auto()
    SHOES = auto()


class Clothing:
    def __init__(self, name, description, location, colour, size, item_type: ClothingType):
        self.name = name
        self.description = description
        self.location = location
        self.colour = colour
        self.size = size
        self.item_type = item_type

    def __del__(self):
        print(f"Object Clothing '{self.name}' is being destroyed")

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_location(self) -> str:
        return self.location

    def get_colour(self) -> str:
        return self.colour

    def get_size(self) -> str:
        return self.size

    def get_item_type(self) -> ClothingType:
        return self.item_type

    def set_name(self, name: str):
        self.name = name

    def set_description(self, description: str):
        self.description = description

    def set_location(self, location: str):
        self.location = location

    def set_colour(self, colour: str):
        self.colour = colour

    def set_size(self, size: str):
        self.size = size

    def set_item_type(self, item_type: ClothingType):
        if not isinstance(item_type, ClothingType):
            raise TypeError("item_type must be a ClothingType")
        self.item_type = item_type

    def get_info(self) -> str:
        return (
            f"Name: {self.name}, "
            f"Description: {self.description}, "
            f"Type: {self.item_type.name}, "
            f"Size: {self.size}, "
            f"Colour: {self.colour}, "
            f"Location: {self.location}"
        )

    def is_suitable_for_weather(self, is_cold: bool) -> bool:
        warm_clothes = (
            ClothingType.JACKET,
            ClothingType.SWEATER
        )
        if is_cold:
            return self.item_type in warm_clothes
        return self.item_type not in warm_clothes

    def __str__(self) -> str:
        return self.get_info()


class Wardrobe:
    def __init__(self):
        self.items: list[Clothing] = []

    def __del__(self):
        print("Object Wardrobe is being destroyed")

    def add_item(self, item: Clothing):
        if not isinstance(item, Clothing):
            raise TypeError("Only Clothing objects can be added")
        self.items.append(item)

    def remove_item(self, item: Clothing):
        if item in self.items:
            self.items.remove(item)

    def sort_by_size(self):
        self.items.sort(key=lambda item: int(item.size))

    def display(self):
        if not self.items:
            print("The wardrobe is empty")
            return
        for item in self.items:
            print(item)


def goOut(clothing_list: list[Clothing]) -> tuple[int, bool]:
    unique_types = {item.item_type for item in clothing_list}
    count = len(unique_types)
    ready = count > 3
    return count, ready


if __name__ == "__main__":
    wardrobe = Wardrobe()
    c1 = Clothing("Blue Shirt", "Cotton casual shirt", "Shelf 1", "Blue", "42", ClothingType.SHIRT)
    c2 = Clothing("Denim Jeans", "Blue classic jeans", "Shelf 2", "Blue", "52", ClothingType.JEANS)
    c3 = Clothing("Winter Jacket", "Warm ski jacket", "Corridor", "Black", "48", ClothingType.JACKET)
    c4 = Clothing("Sneakers", "Running shoes", "Floor", "White", "40", ClothingType.SHOES)

    # для всього одягу який є в шафі вивести description і colour
    wardrobe.add_item(c1)
    wardrobe.add_item(c2)
    wardrobe.add_item(c3)
    wardrobe.add_item(c4)

    for item in wardrobe.items:
        print(f"colour {item.get_colour()}, description {item.get_description()}")

    print("=== Wardrobe Items ===")
    wardrobe.display()

    print("\n=== Access Methods ===")
    print("Old colour:", c1.colour)
    c1.set_colour("Red")
    print("New colour:", c1.colour)

    print("\n=== Sorted by Size ===")
    wardrobe.sort_by_size()
    wardrobe.display()

    count, ready = goOut(wardrobe.items)
    print("\n=== Going Outside ===")
    print("Number of unique clothing types:", count)
    print("Ready to go out:", "Yes" if ready else "No")

    print("\n=== Weather Check ===")
    print(
        f"Is {c3.name} suitable for cold weather?",
        c3.is_suitable_for_weather(True)
    )

    print("\n=== Removing an Item ===")
    wardrobe.remove_item(c4)
    wardrobe.display()
    
