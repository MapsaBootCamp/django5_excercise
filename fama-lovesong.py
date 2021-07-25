
def lovesong(song:str,r,l):
    subs = [[0]*len(song)]*len(song)
    return count(song,subs,r,l)

def count (s: str ,subs, r , l):
    if l < r or subs[r][l] != 0:
        return subs[r][l]
    else:
        if s[l-1] == 'a':
            subs[r][l]=count(s,subs,r,l-1)+1
        elif s[l-1] == 'b':
            subs[r][l] = count(s,subs, r, l - 1) + 2
        elif s[l-1] == 'c':
            subs[r][l] = count(s,subs, r, l - 1) + 3
        return subs[r][l]

print(lovesong('aabcbac',1,5))

