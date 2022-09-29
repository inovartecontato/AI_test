import re

def closestWord(phrase):
    with open('read_data.txt', 'r') as file:
        file = file.readlines()
        filestr = "\n".join(file)
        filelenght = len(filestr.split(" "))
        matches = re.findall('(?<='+phrase+' )\w+', filestr) 
        new_phrase = phrase
        while len(matches)==0:
            new_l = new_phrase.split(" ")
            del new_l[0]
            new_phrase = " ".join(new_l)
            matches = re.findall('(?<='+new_phrase+' )\w+', filestr) 
            if len(new_l)==0:
                break

        probabilities = {}
        for lines in matches:
            if lines in probabilities:
                probabilities[lines] += (1 / filelenght)
            else:
                probabilities[lines] = (1 / filelenght)

    if len(probabilities)>0:
        closestWord = max(probabilities)
        return closestWord
    else:
        return ""

def elaborate(phrase,answersize):
    answer = prompt
    for i in range(0,answersize):
        old_answer = answer
        new_word = closestWord(answer)
        if new_word != "":
            answer = answer +" "+ new_word
    
    return answer

prompt = input("Prompt: ")
print(elaborate(prompt,10))
