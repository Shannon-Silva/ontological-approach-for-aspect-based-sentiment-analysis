import nltk

nltk.download('stopwords')
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import spacy
import pyLDAvis
import pyLDAvis.gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from nltk.corpus import stopwords

stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

# token = ['did', 'not', 'know', 'this', 'gem', 'was', 'hidden', 'way', 'out', 'by', 'the', 'coast', 'had', 'driven',
#          'past', 'it', 'before', 'but', 'never', 'drove', 'in', 'to', 'realize', 'it', 'sits', 'right', 'on', 'the',
#          'beach', 'and', 'affords', 'private', 'access', 'to', 'the', 'water', 'they', 'even', 'have', 'swimming',
#          'pools', 'overlooking', 'the', 'sea', 'have', 'not', 'been', 'there', 'before', 'their', 'renovations', 'but',
#          'think', 'what', 'they', 'have', 'done', 'with', 'the', 'place', 'is', 'very', 'stylish', 'and', 'classy',
#          'there', 'is', 'an', 'airy', 'open', 'feel', 'to', 'the', 'floor', 'plan', 'and', 'the', 'different',
#          'seating', 'areas', 'make', 'it', 'welcome', 'entrance', 'love', 'to', 'just', 'sit', 'by', 'the',
#          'fireplace', 'with', 'some', 'wine', 'and', 'book', 'we', 'dined', 'at', 'echo', 'and', 'enjoyed', 'the',
#          'service', 'and', 'the', 'food', 'was', 'expecting', 'exorbitant', 'prices', 'given', 'the', 'place', 'is',
#          'historical', 'hotel', 'and', 'they', 'just', 'renovated', 'but', 'you', 'll', 'be', 'surprised', 'they',
#          'have', 'some', 'very', 'affordable', 'prices', 'sometimes', 'we', 'felt', 'the', 'portions', 'were', 'even',
#          'way', 'larger', 'than', 'the', 'price', 'we', 'were', 'paying', 'two', 'meals', 'for', 'the', 'price', 'of',
#          'one', 'almost', 'our', 'room', 'was', 'ocean', 'front', 'and', 'beautiful', 'its', 'gorgeous', 'to', 'wake',
#          'up', 'to', 'the', 'sunrise', 'over', 'the', 'ocean', 'housekeeping', 'ensured', 'some', 'of', 'our',
#          'specific', 'requests', 'for', 'in', 'room', 'beverages', 'were', 'taken', 'care', 'of', 'only', 'wish',
#          'they', 'provided', 'microwaves', 'in', 'the', 'room', 'as', 'well', 'they', 'do', 'have', 'fridges', 'and',
#          'moved', 'to', 'proper', 'cups', 'instead', 'of', 'paper', 'glasses', 'for', 'the', 'coffee', 'really',
#          'cant', 'complain', 'we', 'had', 'lovely', 'experience', 'staying', 'here', 'and', 'cant', 'wait', 'to', 'go',
#          'back', 'this', 'might', 'end', 'up', 'becoming', 'our', 'annual', 'beach', 'vacation', 'very', 'close', 'to',
#          'atlanta', 'half', 'day', 'driving', 'ain', 'bad', 'and', 'lots', 'to', 'do', 'locally', 'whether', 'you',
#          'want', 'to', 'be', 'active', 'or', 'relaxed', 'thanks', 'king', 'and', 'prince', 'for', 'memorable',
#          'vacation']

# token=['feel', 'comfortable', 'hotel', 'good', 'price', 'hotel', 'grounds', 'beautiful', 'amazing', 'backyard', 'area', 'free', 'breakfast', 'served', 'pristine', 'pool', 'location', 'perfect', 'also', 'blocks', 'main', 'part', 'san', 'jose']
def extraction(tokens):
    comment = " ".join(tokens)

    def sent_to_words(sentences):
        for sentence in sentences:
            yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

    data_words = list(sent_to_words([comment]))
    bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)  # higher threshold fewer phrases.
    bigram_mod = gensim.models.phrases.Phraser(bigram)

    def remove_stopwords(texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

    def make_bigrams(texts):
        return [bigram_mod[doc] for doc in texts]

    def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacy.io/api/annotation"""
        texts_out = []
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return texts_out

    data_words_nostops = remove_stopwords(data_words)
    data_words_bigrams = make_bigrams(data_words_nostops)
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB'])
    id2word = corpora.Dictionary(data_lemmatized)
    texts = data_lemmatized
    corpus = [id2word.doc2bow(text) for text in texts]
    id2word[2]
    [[(id2word[id], freq) for id, freq in cp] for cp in corpus]
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=300,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=200,
                                                passes=10,
                                                alpha=0.1,
                                                per_word_topics=True)

    # def visualizeTopics(lda_model, corpus, id2word):
    visualisation = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(visualisation, 'LDA_Visualization.html')

    # def generateSubtopics():
    x = lda_model.show_topics(num_topics=300, num_words=20, formatted=False)
    topics_words = [(tp[0], [wd[0] for wd in tp[1]]) for tp in x]

    for topic, words in topics_words:
        if (topic == 1):
            line = " ".join(words)
            array1 = line.split()
            # print(array1)
            return array1


# if __name__ == '__main__':
# #     # visualizeTopics(lda_model, corpus, id2word)
# #     # generateSubtopics()
#     extraction(token)
