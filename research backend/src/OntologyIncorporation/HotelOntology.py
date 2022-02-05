from src.OntologyIncorporation.OntologyConfig import *

with hotel_onto:
    class Hotels(Thing):
        pass

    class Hotel(Hotels):
        pass

    class Room(Hotel):
        pass

    class HotelService(Hotel):
        pass

    class Rating(Hotel):
        pass

    class Location(Hotel):
        pass

    class Price(Hotel):
        pass

    class Name(Hotel):
        pass

    class Food(Hotel):
        pass

    class Value(Hotel):
        pass

    class Accommodation(Room):
        pass

    class RoomService(Room):
        pass

    class Bed(Room):
        pass

    class Capacity(Room):
        pass

    class RoomType(Room):
        pass

    class Size(Room):
        pass

    class AirCondition(Room):
        pass

    class Minibar(Room):
        pass

    class Heater(Room):
        pass

    class Quality(HotelService):
        pass

    class Transport(HotelService):
        pass

    class Parking(HotelService):
        pass

    class WiFi(HotelService):
        pass

    class Staff(HotelService):
        pass

    class Booking(HotelService):
        pass

    class Gym(HotelService):
        pass

    class Reception(HotelService):
        pass

    class Sauna(HotelService):
        pass

    class Pool(HotelService):
        pass

    class Payment(Price):
        pass

    class Deposit(Price):
        pass

    class Offer(Price):
        pass

    class Cost(Price):
        pass

    class Discount(Price):
        pass

    class Clean(Location):
        pass

    class Airport(Location):
        pass

    class CityCenter(Location):
        pass

    class Sight(Location):
        pass

    class Surrounding(Location):
        pass

    class Beach(Location):
        pass

    class Railway(Location):
        pass

    class Dinner(Food):
        pass

    class Snack(Food):
        pass

    class Breakfast(Food):
        pass

    class Appetizer(Food):
        pass

    class Dessert(Food):
        pass

    class Water(Food):
        pass

    class Brunch(Food):
        pass

    class SoftDrinks(Food):
        pass

    class Lunch(Food):
        pass

    class HotDrinks(Food):
        pass

    class FamilyRoom(RoomType):
        pass

    class SingleRoom(RoomType):
        pass

    class DoubleRoom(RoomType):
        pass

    class Suite(RoomType):
        pass

    class Internet(HotelService):
        pass

    class Wine(HotDrinks):
        pass

    class Alcohol(HotDrinks):
        pass

    class Beer(HotDrinks):
        pass

    class Brandy(HotDrinks):
        pass

    class Whiskey(HotDrinks):
        pass

    class WiFi(Internet):
        pass
