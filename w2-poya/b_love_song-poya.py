import string



def love_song(user_string:str):
    alphabet=list(string.ascii_lowercase)
    temp=''
    
    for char in user_string:
        temp += char * (alphabet.index(char)+1)
    print(len(temp))

str_input=input()
love_song(str_input)

    