from owlready2 import *

try:
    movie_onto = get_ontology("D:/research/PP2/api-for-ontology-based-sentiment-analysis/ontologies/movie-ontology.owl")
    hotel_onto = get_ontology("D:/research/PP2/api-for-ontology-based-sentiment-analysis/ontologies/hotel-ontology.owl")
    movie_onto.load()
    hotel_onto.load()

    if movie_onto.load() and hotel_onto.load():
        print("Movie and Hotel Ontology loaded")

    elif movie_onto.load():
        print("Error Loading Hotel Ontology")

    elif hotel_onto.load():
        print("Error Loading Movie Ontology")

except Exception as e:
    print(" ")


