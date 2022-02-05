from src.OntologyIncorporation.MainOntology import *


def test_hotel():
    subtopics = ['good','wonderful','rate','locate','hotel','big','enough','breakfast','access','love','place','offer','space','room']
    review = "The hotel is wonderful. It is strategically located in the best place ever and one can access it very easily. They offer the best rate. The rooms are good and quite big with enough space. I loved their breakfast mostly."

    assert domain_identification(subtopics, review) == ('Hotel', [['Room'], ['Hotel'], ['Breakfast'], ['Offer'], []]), "Should be Hotel domain and categories"


def test_movie():
    subtopics = ['potterhead','unnecessary','sorry','belove','comedy','poor','slapstick','franchise','installment','phantom','racist','menace','get','fantastic','act','villain','caricature','feature','repetitive','stupid']
    review = "Fantastic Beasts is an unnecessary installment of a beloved franchise that features a stupid caricature doing slapstick comedy, a repetitive villain, racist characters, and poor acting. Sorry Potterheads, you just got Phantom Menace-d"
    assert domain_identification(subtopics, review) == ('Movie', [['Sorry Potterheads'], ['Comedy', 'Act'], [], ['Fantastic Beasts', 'Phantom'], []]), "Should be Movie domain and categories"


def test_movie_categories():
    subtopics = [['Sorry Potterheads'], ['Comedy', 'Act'], [], ['Fantastic Beasts', 'Phantom'], []]
    domain = 'Movie'

    assert categories(domain,subtopics) == ('Movie', ['Acting and Production', 'Genre', 'Plot']), "3 categories identified for movie"


def test_hotel_categories():
    subtopics = [['Room'], ['Hotel'], ['Breakfast'], ['Offer'], []]
    domain = 'Hotel'

    assert categories(domain,subtopics) == ('Hotel', ['Room', 'Hotel Service', 'Food', 'Price']) , "4 categories identified for hotel"


if __name__ == "__main__":
    test_hotel()
    test_movie()
    test_movie_categories()
    test_hotel_categories()
    print("Everything passed")