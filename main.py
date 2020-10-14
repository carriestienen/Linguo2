import nltk
from nltk.corpus import treebank



def get_index_by_pos_tag(tagged, postags):
    """expects list of tuples and list of strings
    returns list of numbers"""
    indeces = []
    for i in range(0,len(tagged)):
        if tagged[i][1] in postags:
            indeces.append(i)
    return indeces

#print("Enter a sentence")
sentence = "It was a bright cold day in April, and the clocks were striking thirteen. Why are you reading my book?"
tokens = nltk.word_tokenize(sentence)
#print(tokens)
tagged = nltk.pos_tag(tokens)
#print(tagged)

entities = nltk.chunk.ne_chunk(tagged)
"""print(entities)
print(type(entities))
print(type(tagged))
print(type(tagged[0]))
print(type(tagged[0][0]))
print(tagged[0][1])
print(type(tokens))
print(type(tokens[0]))"""

gerund_indeces = get_index_by_pos_tag(tagged, ["VBG"])
if not(gerund_indeces is None):
    check_gerund(tagged, gerund_indeces)

article_indeces = get_index_by_pos_tag(tagged,["NN","NNS"])
check_article(tagged, article_indeces)
