def sentence_maker(phrase):
    interogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#print(sentence_maker("how are you"))

results = []#create an empty list 
while True:
    user_input = input ("Say something: ") #ask user input
    if user_input == "\end": #check if the input is finished
        break
    else:
        results.append(sentence_maker(user_input)) #append the user input in the results list we created it, useing the function by calling it


print(" ".join(results)) #simply print results

#next will concatinate the strings with .join()
