from src.OntologyIncorporation.HotelOntology import *


def hotel_category_identification(data):
    room_category = []
    hotelService_category = []
    food_category = []
    price_category = []
    others_category = []
    irrelevant_hotel_category = []
    # location_category =['Location']
    try:
        for x in data:
            onto_class = hotel_onto.search_one(iri="*" + x + "*")
            if Room.__subclasscheck__(onto_class):
                room_category.append(x)

            elif HotelService.__subclasscheck__(onto_class) or x == "Hotel":
                hotelService_category.append(x)

            elif Food.__subclasscheck__(onto_class):
                food_category.append(x)

            elif Price.__subclasscheck__(onto_class):
                price_category.append(x)

            # elif Location.__subclasscheck__(onto_class):
            #     location_category.append(x)
            #     print(location_category)

            elif Rating.__subclasscheck__(onto_class) or Name.__subclasscheck__(onto_class) or Value.__subclasscheck__(onto_class):
                others_category.append(x)

            else:
                irrelevant_hotel_category.append(x)

        return room_category, hotelService_category, food_category, price_category, others_category, irrelevant_hotel_category


    except:
        print("Error in Hotel Category Identification!")
