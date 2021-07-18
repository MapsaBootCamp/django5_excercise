def love_song():
    import string
    lenght,repeation = [int(x) for x in input("Enter two value: ").split()]
    subset = input("pls enter the song :")
    emty_list =[]
    while True:
        low, up = list(map(int, input("Enter a multiple value: ").split()))
        emty_list.append(low)
        if len(emty_list) <= repeation:
            pass
        else:
            break
        letter = string.ascii_lowercase
        sub_subset = subset[low-1:up]
        empty_list1 = []
        for char in letter:
            if char in sub_subset:
                counter = sub_subset.count(char)
                index_ =letter.index(char)+1
                exponent = index_*counter
                empty_list1.append(exponent)
        print(sum(empty_list1))




print(love_song())
        



    
# import string
# letter = string.ascii_lowercase

# sub_subset = subset[low-1:up]
# print(letter)
# sumention = 0 
# empty_list = []
# for char in letter:
#     if char in sub_subset:
#         counter = sub_subset.count(char)
#         index_ =letter.index(char)+1
#         exponent = index_*counter
#         empty_list.append(exponent)
# print(sum(empty_list))









    
