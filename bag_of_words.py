import re
vocab = ['a', 'am', 'an', 'if', 'i', 'there','was','you']

doc = ("I was there in a white shoe. \n"
       "If you want get it")
def get_bag_of_words(doc, vocab):
    doc = doc.lower()
    #doc = re.split("\W", doc)
    doc = [s for s in doc if len(s) > 0]
bag_of_words = get_bag_of_words(doc,vocab)