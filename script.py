import random;
from googletrans import Translator;
import unidecode;

"""
Initial logic for learning 1 chinese character a day using the command prompt
"""

def pick_word():
    # get random word
    with open('english-words.txt','r') as english_words:

        # load english words
        words_list = [];
        for word in english_words:
            words_list.append(word.strip());

        # check to make sure not out of words
        if len(words_list) == 0:
            return ('out_of_words');

        # get random word
        index = random.randint(0,len(words_list)-1);
        random_word = words_list[index];

    # delete word
    with open('english-words.txt','w') as english_words:
        for word in words_list:
            if word != random_word:
                english_words.write(word + '\n');

    # add word to past
    with open('history.txt','a+') as past_words:
        past_words.write(random_word + '\n');

    return random_word;

def main():
    print();
    print('Welcome to Learn Chinese!');
    print();

    random_word = pick_word();
    if random_word == 'out_of_words':
        print('Congratulations, you\'ve finished learning all the words!');
    else:
        print('The word of the day is: {}'.format(random_word));
        print();

        translator = Translator();
    
        translation = translator.translate(random_word,dest='zh-CN');
        print('Characters: {}'.format(translation.text));
        print('Pinyin: {}'.format(translation.pronunciation));
        print();

        url = 'https://www.mdbg.net/chinese/dictionary?wdqb='
        pronunciation = unidecode.unidecode(translation.pronunciation);
        search_term = pronunciation.replace(' ','');
        url += search_term;
        print('For more information, variants, and definitions: {}'.format(url));





if __name__ == ('__main__'):
    main();
