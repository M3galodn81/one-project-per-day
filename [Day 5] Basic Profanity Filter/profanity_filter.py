import string

# Pls help me fix this abomination

bad_word_path = "[Day 5] Basic Profanity Filter/list_of_bad_words.txt"
bad_word_list = []

with open(bad_word_path,'r') as file:
    lines = file.readlines()

for line in lines:
    bad_word_list.append(line)


def censor_check(word):
    if word in bad_word_list:
        return True
    
    for letter in word:
        if (letter in string.digits) or (letter in string.punctuation):
            for bad_word in bad_word_list:
            #check length of word
                
                if len(bad_word) == len(word):
                    if bad_word[0] == word[0] and bad_word[-1] == word[-1]:
                        print(word, "is flagged")
                        return True
                    else:
                        return False
                else:
                    return False    
        else:
            return False           

def reconstruct_sentence(message):
    message_word_list = message.split(" ")

    for i in range(len(message_word_list)):
        word = message_word_list[i]
        print(f"censor_check({word}) : {censor_check(word)}")
        if censor_check(word) == True:
            message_word_list[i] = '*' * len(word)

    censored_message = " ".join(message_word_list)
    print(censored_message)

print(string.punctuation)



message = input("Enter a message: ")
reconstruct_sentence(message)

