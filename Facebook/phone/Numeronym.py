"""
isNumeronym("f6k", "facebook") -> true
isNumeronym("f2e3k", "facebook") -> true
isNumeronym("f2e", "facebook") -> false
"""
def isNumeronym(s1, s2):
    if not s1 and not s2:
        return True
    if not s1 or not s2:
        return False
    i = j = 0
    m = len(s1)
    n = len(s2)
    while i < m and j < n:
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif s1[i].isdigit() and s1[i] != '0':
            k = i+1
            while k < m and s1[k].isdigit():
                k += 1
            num = int(s1[i:k])
            while num > 0:
                j += 1
                num -= 1
                if j >= n:
                    return False
            i = k
        else:
            return False
    if j < n-1:
        return False
    return True



#test cases
t = [('f6k', 'facebook'),   #True
 ('f2e3k', 'facebook'),     #True
 ('f2e', 'facebook'),       #False
 ('b12k', 'booooooooooook'),#True
 ('f8', 'facebook'),        #False
 ('f0aceb2k', 'facebook'),  #False
 ('f51', 'facebook')]       #False

for a, b in t:
    print isNumeronym(a, b)
