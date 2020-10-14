#make sure gerunds follow a proper verb
def check_gerund(words, indeces):
    for i in indeces:
        prev_word = words[i-1][0]
        prev_word_postag = words[i-1][1]
        if not(prev_word_postag in ["VBD","VB","VBP"] or prev_word == "not"):
            print("You cannot have the word %s in front of a gerund." % prev_word)

#make sure nouns have articles
def check_article(words, indeces):
    for i in indeces:
        prev_word = words[i-1][0]
        prev_word_postag = words[i-1][1]
        #print("previous word and postag %s %s" % (prev_word, prev_word_postag))

        is_prev_word_adj = prev_word_postag in ["JJ"]

        if prev_word_postag == "PRP$":
            pass
        elif is_prev_word_adj:
            j = 2
            while is_prev_word_adj:
                prev_word = words[i-j][0]
                prev_word_postag = words[i-j][1]
                #print("previous word and postag %s %s" % (prev_word, prev_word_postag))
                is_prev_word_adj = prev_word_postag in ["JJ"]
                if not is_prev_word_adj:
                    if not prev_word_postag == "DT":
                        print("You need an article in front of %s." % words[i][0])
                j += 1

