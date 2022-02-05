# Ontological-approach-for-aspect-based-sentiment-analysis
The research implementation of an extendible ontology-based approach for aspect-based sentiment analysis. It also focuses on learning the aspects using topic modelling to automate the aspect detection. The results indicate that the  proposed approach can be effective in classifying sentiments under different aspects.

# Main Objective
Provide an API that could take in a comment or review, and then give a sentiment analysis for each category according to automatically identified categories, based on ontology instead of providing an overall sentiment for a particular comment

# Methodology
1. Collection of Reviews
    * Webscrape sites such as IMDB and TripAdvisor for reviews using python scrpits
    * Take user input review through the API
2. Review Pre-Processing (Word-tokenize)
    * Cleaning the input review through removal of numbers, tags, stopwords etc... using NLTK
    * Use NLTK in Word Tokenization
3. Sub-Topic Extraction
    * Extract meaningful keywords from word tokens through LDA
    * Use LDA to identify the frequency of keywords and to simpligy keywords
4. Ontology Incorporation
    * Use Protégé to build a service ontology; Hotel Service and a product ontology; Movie
    * SPARQL is used to query the input keywords to identify the domain of the input review
    * Cython and OwlReady2 an ontology-oriented programming language helps to query for categories and dynamically create classes
5. Category Pre-Processing (Line-tokenize)
    * Use of custom engineered python script to identify lines relevant to each category
6. Sentiment Analysing
    * Use of Google Colab to train the module using the collected dataset from Kaggle
    * SVM algorithm helps in analysing for each category in positive, neutral and negative legends
7. Business Logic Handler
    * Use of a Python Script which holds together all the above components
    
# Technologies used
1. Python
    * Cython
    * NLTK
    * OwlReady2
2. Protégé
3. Flask
4. ReactJs
5. MongoDB
6. Google Colab
