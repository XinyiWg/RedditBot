import random
import pickle



def capitalize_sentences(sentences):
    """(str) -> str
    Returns the string with first letter being capitalized. Each sentence ends with a '!', '.' or '?' 
    >>> capitalize_sentences("hello. hello! hello???? HI!")
    'Hello. Hello! Hello???? HI!'
    
    >>> capitalize_sentences("! hey")
    '! Hey'
    
    >>> capitalize_sentences(" hey")
    'hey'
    
    >>> capitalize_sentences("hey.")
    'Hey.'
    
    >>> capitalize_sentences("good morning")
    'Good morning'
    """
    
    punctuation = '.!?'
    new_sentences = ''
    
    
    for  index, char in enumerate(sentences): 
        
        # Case1: For first sentence:The first string in first sentence is a letter
        condition1 = index == 0 and char not in punctuation 
        # Case2: Each sentence(except first sentence) starts after a space
        condition2 = index >= 2 and sentences[index-1] == " " and sentences[index-2] in punctuation
       
        if condition1 or condition2:
            new_sentences += char.upper()
        else:
               new_sentences += char
    
    return new_sentences


def capitalize_sentence_grid(grid):
    """(list) -> list
    Returns a list that make every sentences begin with capital letter without modifying the original grid.
    
    the punctuation always appears at the end of a word
    >>> grid = [["you", "might", "think"], ["these", "are", "separate", "sentences"], \
               ["but", "they", "are", "not!", "ok,", "this"], ["one", "is."]]
    >>> capitalize_sentence_grid(grid)
    [['You', 'might', 'think'], ['these', 'are', 'separate', 'sentences'], ['but', 'they', \
    'are', 'not!', 'Ok,', 'this'], ['one', 'is.']]
    
    >>> grid = [["you", "are", "a", "genius."], ["i", "am", "not.", "this"], \
               ["is", "a", "fact", "that", "couldn't", "be"], ["ignored.", "right"]]
    >>> capitalize_sentence_grid(grid)
    [['You', 'are', 'a', 'genius.'], ['I', 'am', 'not.', 'This'], ['is', 'a', 'fact', 'that', "couldn't", 'be'], ['ignored.', 'Right']]
    
    >>> grid = [["the", "weather", "is", "good."], ["isn't", "it?", "i", "enjoy"], \
               ["it", "a", "lot.", "what"],["about"],["you?"],[ "couldn't", "agree"], ["more,", "dude."]]
    >>> capitalize_sentence_grid(grid)           
    [['The', 'weather', 'is', 'good.'], ["Isn't", 'it?', 'I', 'enjoy'], ['it', 'a', 'lot.', 'What'], ['about'], \
    ['you?'], ["Couldn't", 'agree'], ['more,', 'dude.']]
    """
    punctuation = '.!?'
    final_list = []
    
    for index1, sublist in enumerate(grid):
        new_str = ""
        copy_sublist = sublist[:]
        if index1 == 0:
            new_str = " ".join(sublist)
            
        elif grid[index1-1][-1][-1] in punctuation:
            copy_sublist[0] = '. ' + copy_sublist[0]
            new_str = " ".join(copy_sublist)
        else:
            copy_sublist[0] = ' ' + copy_sublist[0]
            new_str = " ".join(copy_sublist)
            
        if new_str[0] != '.':
            converted_list = capitalize_sentences(new_str).split()
        else:
            converted_list = capitalize_sentences(new_str).strip(' .').split()
            
        final_list.append(converted_list)
     
    return final_list



def fill_in_madlib(madlib_str, d):
    """(str) -> dict
    Returns the final string with randomly chosen word from dictionary
    Note: same representing symbol should choose the same word, xx_1,xx_2 should be two different words
    AssertionError will be raised if any of  type or value input is not correct.
    
    >>> random.seed(12)
    >>> d = {'ADV-UNDOUTEDLY': ['undoutedly', 'most likely', 'probably', 'without doubt', 'difinitely'], \
     'N-DECISION': ['decision', 'choice', 'conclusion', 'resolution', 'selection']}
    >>> fill_in_madlib("Dee Buh-Ger? Hey bros. Never ever vote for him. Such a shame. [ADV-UNDOUTEDLY], \
    he will bring nothing beneficial to us. Make a wise [N-DECISION]. Vote anybody except Dee Buh-Ger!", d)
    'Dee Buh-Ger? Hey bros. Never ever vote for him. Such a shame. difinitely, he will bring nothing beneficial to us. \
    Make a wise conclusion. Vote anybody except Dee Buh-Ger!'
    
    >>> random.seed(1006)
    >>> d = {'PAST-TENSE-VERB': ['pondered', 'scribbled', 'snoozled', 'studied'], \
                  'ADJECTIVE': ['dreamy', 'weak', 'weary', 'starry', 'lazy']}
    >>> fill_in_madlib("Once upon a midnight [ADJECTIVE_4], while I [ADJECTIVE_4], [ADJECTIVE_4] \
    and [ADJECTIVE_5] and [ADJECTIVE_6] and [ADJECTIVE_8] and [ADJECTIVE_8],", d)
    'Once upon a midnight weary, while I weary, weary and dreamy and weak and lazy and lazy,'
    
    Possible AssertionError below:
    >>> d = {'COLOR': ['red', 'yellow']}
    >>> fill_in_madlib(" Today is a [COLOR], [COLOR_1], [COLOR_2], [COLOR_3] day!", d)
    AssertionError: The number of speech is over the range! We do not have that many words in the dictionary!
    
    >>>d = {'COLOR': ['red', 'yellow']}
    >>>fill_in_madlib(1234567, d)
    AssertionError: Your input is not invalid! Not correct type!
    
    >>>d = {'COLOR': ['red', 'yellow']}
    >>>fill_in_madlib("Today is a [COLORS] day", d)
    AssertionError: Your input is not invalid! your intended changing word is not in the dictionary!
    """
    
    # Wrong Type
    if  type(madlib_str) != str or type(d) != dict:
        raise AssertionError('Your input is not invalid! Not correct type!')
    
    
    final_sentence = ''
    remaining_str = madlib_str
    name_choice = {}
    num_of_speech_with_diff_num = 0
    copy_d = {}
    
    for key in d:
        value_list = []
        for elenment in d[key]:
            value_list.append(elenment)
            copy_d[key] = value_list
            
    
    
    while remaining_str.find('[') != -1:
         
        begin = remaining_str.find('[')
        end = remaining_str.find(']')
        
        
        name = remaining_str[begin + 1 : end].upper()
        category = name.strip('_1234567890')
        if name != category and name not in name_choice:
            num_of_speech_with_diff_num += 1
            # Wrong value. The number of different speech required in txt is over the number of words dictionary is able to provide!
            if num_of_speech_with_diff_num > len(d[category]):
                raise AssertionError('The number of speech is over the range! We do not have that many words in the dictionary!')
        
        # Wrong value. speech not in the dictionary
        if category not in d:
            raise AssertionError('Your input is not invalid! your intended changing word is not in the dictionary!')
            
        
        former_str = remaining_str[:begin]
        final_sentence += former_str
        remaining_str = remaining_str[end+1:]  
        
        # in the form of[ABC] or [ABC_1] for the first time
        if name not in name_choice:
            if name == category: # if [ABC] appears after [ABC_1]
                word = random.choice(d[category])
                
            else:
                word = random.choice(copy_d[category])
                copy_d[category].remove(word)
            name_choice[name] = word
                
        # in the form of [ABC_1] and it's at least the second time appearing
        elif name in name_choice:
            word = name_choice[name]
            
        final_sentence += word
        
        # Finish the remaining part of the sentence
        if '[' not in remaining_str:
            final_sentence += remaining_str
        final_sentence = capitalize_sentences(final_sentence)
    return final_sentence


def load_and_process_madlib(filename):
    """(str) -> NoneType
    loading word dictionary in word_dic.pkl and sentence need to be finished in 'filename' first,
    and then call fill_in_madlib to finish blanks
    In the end, write the finished sentences to filename_filled.txt
    """
    
    f = open("word_dict.pkl", "rb")
    d = pickle.load(f)
    f.close()
    
   
    fobj = open(filename, "r") 
    madlib_str= fobj.read()
    fobj.close()
    
    sentence = fill_in_madlib(madlib_str, d)
    
    filled_txt = open(filename.replace('.txt', '_filled.txt'), "w")
    filled_txt.write(sentence)
    filled_txt.close()
    
    
    
def generate_comment():
    """() -> str
    Retuens a string that after being blanked and write in 'filename_filled.txt'
    Note: 10 madlibk.txt can be chosen randomly
    
    >>> random.seed(9001)
    >>> d = {'PAST-TENSE-VERB': ['pondered', 'scribbled', 'snoozled', 'studied'], \
              'ADJECTIVE': ['dreamy', 'weak', 'weary', 'starry', 'lazy']}
    >>> generate_comment()
    'Once upon a midnight dreamy, while I snoozled, lazy and starry,'
    
    >>> random.seed(12)
    >>> d = {'COLOR': ['red', 'yellow']}
    >>> generate_comment()
    """
    k = random.randint(1,10)
    madlib_name = 'madlib' + str(k) + '.txt'
    madlibk = open(madlib_name, "r")
    madlibk_str= madlibk.read()
    madlibk.close()
    load_and_process_madlib(madlib_name)
    filled_txt = open(madlib_name.replace('.txt', '_filled.txt'), "r")
    sentence = filled_txt.read()
    filled_txt.close()
    
    
    return sentence
    

