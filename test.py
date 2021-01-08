s = "1. First sentence. \n2. Second sentence. \n1. Another sentence. \n3. Third sentence."

def do_it(sentence):
    possible = [str(i) + "." for i in range(1,10)]
    sentence = sentence.replace("\n", '')
    for i in possible:
        sentence = sentence.replace(i, '(*)', 1)
    l = sentence.split("(*) ")
    l.pop(0)
    return l
l = do_it(s)
print(l)
