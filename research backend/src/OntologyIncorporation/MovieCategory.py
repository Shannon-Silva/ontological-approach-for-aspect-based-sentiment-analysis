from src.OntologyIncorporation.MovieOntology import *



def movie_category_identification(data):
    acting_category = []
    genre_category = []
    duration_category = []
    plot_category = []
    others_movie_category = []
    irrelevant_movie_category = []
    try:
        for x in data:
            onto_class=movie_onto.search_one(iri = "*"+x+"*")
            if Characters.__subclasscheck__(onto_class):
                acting_category.append(x)

            elif Genre.__subclasscheck__(onto_class):
                genre_category.append(x)

            elif Duration.__subclasscheck__(onto_class):
                duration_category.append(x)

            elif Plot.__subclasscheck__(onto_class) or Music.__subclasscheck__(onto_class) or x == "Movie":
                plot_category.append(x)

            elif Director.__subclasscheck__(onto_class) or Producer.__subclasscheck__(onto_class) or Title.__subclasscheck__(onto_class) or ReleasedDate.__subclasscheck__(onto_class) or Award.__subclasscheck__(onto_class):
                others_movie_category.append(x)

            else:
                irrelevant_movie_category.append(x)

        return acting_category, genre_category, duration_category, plot_category, others_movie_category, irrelevant_movie_category



    except Exception as e:
        print(e)
        print("Error in Movie Category Identification!")


