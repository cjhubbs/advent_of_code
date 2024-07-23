import string 

other_case = {'A': 'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z','a': 'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}

reducible_pairs = ['Aa','aA','Bb','bB','Cc','cC','Dd','dD','Ee','eE','Ff','fF','Gg','gG','Hh','hH','Ii','iI','Jj','jJ','Kk','kK','Ll','lL','Mm','mM','Nn','nN','Oo','oO','Pp','pP','Qq','qQ','Rr','rR','Ss','sS','Tt','tT','Uu','uU','Vv','vV','Ww','wW','Xx','xX','Yy','yY','Zz','zZ']

def reduce(chain):
    while 1:
        start_len = len(chain)
        for p in reducible_pairs:
            chain = chain.replace(p,"")
        if len(chain) == start_len:
            return len(chain)


f = open("input-5.txt", "r")
chain = f.read().strip()

print(reduce(chain))

for char in string.ascii_uppercase:
    temp_chain = chain.replace(char,"")
    temp_chain = temp_chain.replace(other_case[char],"")
    temp_len = reduce(temp_chain)
    print(char,": ",temp_len)