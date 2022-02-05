from src.OntologyIncorporation.OntologyConfig import *

with movie_onto:
    class Movies(Thing):
        pass

    class Movie(Movies):
        pass

    class Title(Movie):
        pass

    class ReleasedDate(Movie):
        pass

    class Plot(Movie):
        pass

    class Producer(Movie):
        pass

    class Music(Movie):
        pass

    class Genre(Movie):
        pass

    class Duration(Movie):
        pass

    class Director(Movie):
        pass

    class Characters(Movie):
        pass

    class Award(Movie):
        pass

    class Storyline(Plot):
        pass

    class Story(Plot):
        pass

    class Skit(Plot):
        pass

    class Scenario(Plot):
        pass

    class Location(Plot):
        pass

    class Film(Plot):
        pass

    class Thriller(Genre):
        pass

    class Romance(Genre):
        pass

    class Mystery(Genre):
        pass

    class Musical(Genre):
        pass

    class Horror(Genre):
        pass

    class Fantasy(Genre):
        pass

    class Crime(Genre):
        pass

    class Comedy(Genre):
        pass

    class Adventure(Genre):
        pass

    class Action(Genre):
        pass

    class Start(Duration):
        pass

    class End(Duration):
        pass

    class Length(Duration):
        pass

    class Role(Characters):
        pass

    class Protagonist(Characters):
        pass

    class Player(Characters):
        pass

    class Performer(Characters):
        pass

    class Dancer(Characters):
        pass

    class Actor(Characters):
        pass

    class Minor(Role):
        pass

    class Main(Role):
        pass

    class Lead(Role):
        pass

    class Actress(Actor):
        pass

    class Male(Actor):
        pass

    class Female(Actor):
        pass

