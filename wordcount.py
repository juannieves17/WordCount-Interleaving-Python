
lineCounter = 0
def word_count_dict(filename):
    
    word_count = {}  # Map each word to its count
    input_file = open(filename, 'r')
    global lineCounter
    for line in input_file: 
        lineCounter = lineCounter +1    
        words = line.split()
        for word in words:
            word = word.lower()
            # Special case if we're seeing this word for the first time.
            if not word in word_count: 
                line_array = [lineCounter]
                word_count[word] = [1 ,line_array]
            else:
                if not lineCounter in word_count[word][1]:
                    word_count[word][1].append(lineCounter)
                word_count[word][0] = word_count[word][0] +1
                
                word_count[word] = [word_count[word][0] , word_count[word][1]]
    input_file.close()
    return word_count


def print_words(filename):
    word_count = word_count_dict(filename)
    #Sorted by the frecuency
    words = sorted(word_count.items(), key=get_count, reverse=True)
    #Sort the words remaining with the same sorted frecuency
    final = sortWords(words)
    
    #Presents the table 
    print "\nFrecuency | Word | Lines"    
    for word , count in final:
        print count[0], word, count[1]

def sortWords(words):
    frecuency = []
    result = []
    c = 0
    for i in range(len(words)):
        l = words[i][1][0]
        if not l in frecuency:
            frecuency.append(l)
            
    for f in frecuency:
       sortedWords = []
       while c != len(words) and words[c][1][0] == f:
            sortedWords.append(words[c])
            c+=1
       sortedWords.sort()
       result.extend(sortedWords)
    return result

def get_count(word_count_tuple):
    return word_count_tuple[1]

def get_word(word_count_tuple):
    return word_count_tuple[0]



def main():
    filename = 'small.txt'
    input_file = open(filename, 'r')
    for line in input_file:
        print line
    print_words(filename)

if __name__ == '__main__':
    main()
