def frame(text, char):
    lens = []
    for i in text:
        lens.append(len(i))
    width = max(lens) 
    height = len(lens)
    n = 0
    result = char*(width+4)+"\n"
    while n<height:
        count_space = width - len(text[n])+1
        result+=char+" "+text[n]+count_space*" "+char+"\n"
        n+=1
    result += char*(width+4)
    return result
