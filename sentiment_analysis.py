punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def strip_punctuation(strng):
    for char in strng:
        if char in punctuation_chars:
            strng=strng.replace(char,"")
    return strng

def get_neg(string):
    count=0
    string=strip_punctuation(string)
    string=string.lower()
    for word in string.split(" "):
        if word in negative_words:
            count+=1
    return count

def get_pos(string):
    count=0
    string=strip_punctuation(string)
    string=string.lower()
    for word in string.split(" "):
        if word in positive_words:
            count+=1
    return count

fhw = open("resulting_data.csv", 'w')
fhw.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
fhw.write("\n")

fh=open("project_twitter_data.csv", "r")
list_of_lines=fh.readlines()

for line in list_of_lines[1:]:
    vals=line.strip().split(",")
    raw_string='{},{},{},{},{}'.format(vals[1],vals[2],get_pos(vals[0]),get_neg(vals[0]),get_pos(vals[0])-get_neg(vals[0]))
    fhw.write(raw_string+"\n")
fhw.close()
