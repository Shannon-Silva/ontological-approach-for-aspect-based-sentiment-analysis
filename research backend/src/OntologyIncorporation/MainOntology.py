from src.OntologyIncorporation.MovieCategory import *
from src.OntologyIncorporation.HotelCategory import *
from src.OntologyIncorporation.FeatureExtraction import *


def capitalize(data):
    capitalized_arr = []
    try:
        for x in data:
            x = x.capitalize()
            capitalized_arr.append(x)
        return capitalized_arr
    except:
        print("Error in capitalizing")


def ontology_identification(text,m,h):
    categories = []

    irrelevant_hotel_category=h[5]
    irrelevant_movie_category = m[5]
    acting_category=m[0]
    genre_category=m[1]
    duration_category=m[2]
    plot_category=m[3]
    others_movie_category=m[4]
    room_category=h[0]
    hotelService_category=h[1]
    food_category=h[2]
    price_category=h[3]
    others_category=h[4]

    if len(irrelevant_hotel_category) > len(irrelevant_movie_category):
        domain = "Movie"

        words = feature_extraction(text)
        for i in range(len(words)):
            if i ==0:
                for j in range(len(words[i])):
                    acting_category.append(words[i][j])
            if i ==1:
                for j in range(len(words[i])):
                    plot_category.append(words[i][j])


        categories.append(acting_category)
        categories.append(genre_category)
        categories.append(duration_category)
        categories.append(plot_category)
        categories.append(others_movie_category)
        return domain, categories

    elif len(irrelevant_movie_category) > len(irrelevant_hotel_category):
        domain = "Hotel"

        words = feature_extraction(text)
        for i in range(len(words)):
                for j in range(len(words[i])):
                    hotelService_category.append(words[i][j])

        categories.append(room_category)
        categories.append(hotelService_category)
        categories.append(food_category)
        categories.append(price_category)
        categories.append(others_category)
        return domain, categories


def domain_identification(array1,text):
    arr = []
    a = []
    try:
        capitalized_arr = capitalize(array1)
        for x in capitalized_arr:

            if hotel_onto.search_one(iri="*" + x + "*") and movie_onto.search_one(iri="*" + x + "*"):
                arr.append(x)
                # hotel_category_identification(capitalized_arr)
                # movie_category_identification(capitalized_arr)
            else:
                a.append(x)

        if a == capitalized_arr:
            print("Error: doesn't match movie or hotel domain")
        elif hotel_onto.search_one(iri="*" + arr[0] + "*") and movie_onto.search_one(iri="*" + arr[0] + "*"):
            m=movie_category_identification(arr)
            h=hotel_category_identification(arr)

        return ontology_identification(text,m,h)

    except Exception as e:
        print(str(e) + "d")


def categories(dom,subcategories):
    if dom == 'Hotel':
        hh_cat = ["Room", "Hotel Service", "Food", "Price", "Others"]
        for i in range(len(subcategories)):
            if len(subcategories[i]) == 0:
                hh_cat[i] = ''

        hh_cat1 = [j for j in hh_cat if j]

        return (dom, hh_cat1)

    elif dom == 'Movie':
        mm_cat =["Acting and Production", "Genre", "Duration", "Plot", "Others"]
        for i in range(len(subcategories)):
            if len(subcategories[i]) == 0:
                mm_cat[i] = ''

        mm_cat1 = [j for j in mm_cat if j]
        return (dom, mm_cat1)



