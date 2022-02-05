from src.TextPreprocessing.Preprocesing import pre_process
from src.SubtopicExtraction.MovieSubTopics import extraction
from src.OntologyIncorporation.MainOntology import domain_identification
from src.TextPreprocessing.LineTokenize import selector
from src.SentimentAnalysis.SentimentMain import *
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource, request
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = 'reviews'
app.config['MONGO_USERNAME'] = 'root'
app.config['MONGO_PASSWORD'] = '1234'
app.config['MONGO_AUTH_SOURCE'] = 'admin'

app.config['MONGO_URI'] = 'mongodb://root:1234@ds145486.mlab.com:45486/reviews?retryWrites=false'

mongo = PyMongo(app)

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


def preprocessing(text):
    tokens = pre_process(text)
    # print(tokens)
    return tokens


def sub_Topics(text):
    token = preprocessing(text)
    topics = extraction(token)
    print(topics)
    return topics


def ontology_incorporation(text):
    token = preprocessing(text)
    topics = extraction(token)
    onto = domain_identification(topics, text)
    # print(onto)
    return onto


def line_tokenize(text):
    token = preprocessing(text)
    topics = extraction(token)
    onto = domain_identification(topics, text)
    lines = selector(onto, text)
    # print(lines[0:3])
    return lines


def sentiment_analysis(text):
    token = preprocessing(text)
    topics = extraction(token)
    onto = domain_identification(topics, text)
    lines = selector(onto, text)
    sent = analysis(lines[0:2], [text])
    # print(sent)


def api(text):
    token = preprocessing(text)
    topics = extraction(token)
    onto = domain_identification(topics, text)
    lines = selector(onto, text)
    sent = analysis(lines, [text])

    print("Comment: " + text)
    print("Domain: " + lines[0])
    # print(token)
    # print(topics)
    # print(onto)
    # print(lines)
    # print(sent)
    print("-----------------------------------------")

    for j in range(len(lines[2])):
        print(str(lines[2][j] + ": [" + str(sent[0][j]) + ", " + str(sent[1][j]) + ", " + str(sent[2][j]) + "]"))

    print()
    print("Overall Sentiment: " + str(sent[3]))

    return onto[0], lines[2], sent[0], sent[1], sent[2], sent[3], token, topics, lines[1]


@app.route('/<comment>', methods=['GET'])
def analyse(comment):
    result = api(comment)

    a = {}
    b = {}
    chartData = {}
    chartData1 = {}
    redData = {}
    yellowData = {}
    greenData = {}
    NegativeData = {}
    NeutralData = {}
    PositiveData = {}

    redData['label'] = 'Negative'
    redData['backgroundColor'] = '#d2222d'
    redData['data'] = result[2]

    yellowData['label'] = 'Neutral'
    yellowData['backgroundColor'] = '#ffbf00'
    yellowData['data'] = result[3]

    greenData['label'] = 'Positive'
    greenData['backgroundColor'] = '#238823'
    greenData['data'] = result[4]

    chartData['labels'] = result[1]
    chartData['datasets'] = [redData, yellowData, greenData]

    a['table_name'] = result[0]
    a['chartData'] = chartData

    NegativeData['label'] = 'Negative'
    NegativeData['backgroundColor'] = '#d2222d'
    NegativeData['data'] = [result[5][0]]

    NeutralData['label'] = 'Neutral'
    NeutralData['backgroundColor'] = '#ffbf00'
    NeutralData['data'] = [result[5][1]]

    PositiveData['label'] = 'Positive'
    PositiveData['backgroundColor'] = '#238823'
    PositiveData['data'] = [result[5][2]]

    chartData1['datasets'] = [NegativeData, NeutralData, PositiveData]

    b['table_name'] = result[0]
    b['chartData'] = chartData1
    a['total'] = b

    a['words'] = result[6]
    a['topics'] = result[7]
    a['onto'] = [result[0],result[1]]
    a['lines'] = result[8]
    a['senti'] = [result[2], result[3], result[4], result[5]]

    return jsonify(a)


@app.route('/hotel', methods=['GET'])
def hotel_all():
    hotel = mongo.db.hotel

    output = []

    for q in hotel.find():
        output.append({'ID': q['ID'],
                       'Comment': q['Comment'],
                       'Categories': q['Categories'],
                       'Negative': q['Negative'],
                       'Neutral': q['Neutral'],
                       'Positive': q['Positive'],
                       'table_name': "Hotel",
                       'Overall': q['Overall']})

    return jsonify({'data': output})


@app.route('/Hotel/<ID>', methods=['GET'])
def get_one_hotel(ID):
    hotel = mongo.db.hotel

    q = hotel.find_one({'ID': ID})

    a = {}
    chartData = {}
    NegativeData = {}
    NeutralData = {}
    PositiveData = {}

    if q:
        NegativeData['label'] = 'Negative'
        NegativeData['backgroundColor'] = '#d2222d'
        NegativeData['data'] = q['Negative']

        NeutralData['label'] = 'Neutral'
        NeutralData['backgroundColor'] = '#ffbf00'
        NeutralData['data'] = q['Neutral']

        PositiveData['label'] = 'Positive'
        PositiveData['backgroundColor'] = '#238823'
        PositiveData['data'] = q['Positive']

        chartData['labels'] = q['Categories']
        chartData['datasets'] = [NegativeData, NeutralData, PositiveData]

        a['table_name'] = "Hotel"
        a['comment'] = q['Comment']
        a['chartData'] = chartData

    else:
        a = 'No results found'

    return jsonify(a)


@app.route('/Hotel/total/<ID>', methods=['GET'])
def get_tot_hotel(ID):
    hotel = mongo.db.hotel

    q = hotel.find_one({'ID': ID})

    a = {}
    chartData = {}
    NegativeData = {}
    NeutralData = {}
    PositiveData = {}

    if q:
        tot = q['Overall']
        NegativeData['label'] = 'Negative'
        NegativeData['backgroundColor'] = '#d2222d'
        NegativeData['data'] = [tot[0]]

        NeutralData['label'] = 'Neutral'
        NeutralData['backgroundColor'] = '#ffbf00'
        NeutralData['data'] = [tot[1]]

        PositiveData['label'] = 'Positive'
        PositiveData['backgroundColor'] = '#238823'
        PositiveData['data'] = [tot[2]]

        chartData['datasets'] = [NegativeData, NeutralData, PositiveData]

        a['table_name'] = "Hotel"
        a['comment'] = q['Comment']
        a['chartData'] = chartData

    else:
        a = 'No results found'

    return jsonify(a)


@app.route('/hotel', methods=['POST'])
def add_hotel():
    hotel = mongo.db.hotel

    _ID = request.json['_ID']
    Negative = request.json['Negative']
    Positive = request.json['Positive']
    Neutral = request.json['Neutral']
    Categories = request.json['Categories']
    Overall = request.json['Overall']
    Comment = request.json['Comment']

    hotel_id = hotel.insert(
        {'_ID': _ID, 'Comment': Comment, 'Categories': Categories, 'Negative': Negative, 'Neutral': Neutral,
         'Positive': Positive, 'Overall': Overall})
    new_hotel = hotel.find_one({'_id': hotel_id})

    output = {'_ID': new_hotel['_ID'], 'Comment': new_hotel['Comment'], 'Categories': new_hotel['Categories'],
              'Negative': new_hotel['Negative'], 'Neutral': new_hotel['Neutral'], 'Positive': new_hotel['Positive'],
              'Overall': new_hotel['Overall']}

    return jsonify({'result': output})


@app.route('/movie', methods=['GET'])
def movie_all():
    movie = mongo.db.movie

    output = []

    for q in movie.find():
        output.append({'_ID': q['_ID'],
                       'Comment': q['Comment'],
                       'Categories': q['Categories'],
                       'Negative': q['Negative'],
                       'Neutral': q['Neutral'],
                       'Positive': q['Positive'],
                       'table_name': "Movie",
                       'Overall': q['Overall']})

    return jsonify({'data': output})


@app.route('/Movie/<_ID>', methods=['GET'])
def get_one_movie(_ID):
    movie = mongo.db.movie

    q = movie.find_one({'_ID': _ID})

    a = {}
    chartData = {}
    NegativeData = {}
    NeutralData = {}
    PositiveData = {}

    if q:
        NegativeData['label'] = 'Negative'
        NegativeData['backgroundColor'] = '#d2222d'
        NegativeData['data'] = q['Negative']

        NeutralData['label'] = 'Neutral'
        NeutralData['backgroundColor'] = '#ffbf00'
        NeutralData['data'] = q['Neutral']

        PositiveData['label'] = 'Positive'
        PositiveData['backgroundColor'] = '#238823'
        PositiveData['data'] = q['Positive']

        chartData['labels'] = q['Categories']
        chartData['datasets'] = [NegativeData, NeutralData, PositiveData]

        a['table_name'] = "Movie"
        a['comment'] = q['Comment']
        a['chartData'] = chartData
        a['total'] = q['Overall']

    else:
        a = 'No results found'

    return jsonify(a)


@app.route('/Movie/total/<_ID>', methods=['GET'])
def get_tot_movie(_ID):
    movie = mongo.db.movie

    q = movie.find_one({'_ID': _ID})

    a = {}
    chartData = {}
    NegativeData = {}
    NeutralData = {}
    PositiveData = {}

    if q:
        tot = q['Overall']
        NegativeData['label'] = 'Negative'
        NegativeData['backgroundColor'] = '#d2222d'
        NegativeData['data'] = [tot[0]]

        NeutralData['label'] = 'Neutral'
        NeutralData['backgroundColor'] = '#ffbf00'
        NeutralData['data'] = [tot[1]]

        PositiveData['label'] = 'Positive'
        PositiveData['backgroundColor'] = '#238823'
        PositiveData['data'] = [tot[2]]

        # chartData['labels'] =['Negative','Neutral','Positive']
        chartData['datasets'] = [NegativeData, NeutralData, PositiveData]

        a['table_name'] = "Movie"
        a['comment'] = q['Comment']
        a['chartData'] = chartData

    else:
        a = 'No results found'

    return jsonify(a)


@app.route('/movie', methods=['POST'])
def add_movie():
    movie = mongo.db.movie

    _ID = request.json['_ID']
    Negative = request.json['Negative']
    Positive = request.json['Positive']
    Neutral = request.json['Neutral']
    Categories = request.json['Categories']
    Overall = request.json['Overall']
    Comment = request.json['Comment']

    movie_id = movie.insert(
        {'_ID': _ID, 'Comment': Comment, 'Categories': Categories, 'Negative': Negative, 'Neutral': Neutral,
         'Positive': Positive, 'Overall': Overall})
    new_movie = movie.find_one({'_id': movie_id})

    output = {'_ID': new_movie['_ID'], 'Comment': new_movie['Comment'], 'Categories': new_movie['Categories'],
              'Negative': new_movie['Negative'], 'Neutral': new_movie['Neutral'], 'Positive': new_movie['Positive'],
              'Overall': new_movie['Overall']}

    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
