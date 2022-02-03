"""
Create a function that counts the embedded names in the string and determines the equality. The names are embedded in a string of mixed special symbols and characters. The names to be counted to are adjoined with the ampersand symbol & and as the second parameter. See the following examples for more details.

Examples
equal_count("Peter!@#$Paul&*#Peter!--@|#$Paul#$Peter@|Paul$%^^Peter++Paul%$%^Peter++Paul#$#$#Peter@|Paul", "Peter&Paul")
➞ {"Peter":6, "Paul": 6, "equality": True}

equal_count("Elliot!@#$Sam!--@|#$Elliot@|Sam++Elliot$%^Elliot@|Sam!@#Elliot!@#$Sam!--@|#$Elliot", "Sam&Elliot")
➞ {"Sam": 4, "Elliot": 6, "equality": False, "difference": 2}
# "difference" key is added if count is not equal.

equal_count("Tim!@#$Kit&&*#Tim!--@|#$Kit#$%Tim@|Kit$%^^Tim++Kit%$%^Tim++Kit#$#$#Tim@|Kit", "Ken&Tom")
➞ {"Ken": 0, "Tom": 0, "equality": True}
"""

def equal_count(txt, names):
    a,b = names.split('&')

    d = {a:txt.count(a), b:txt.count(b), 'equality': True }
    dif = abs(d[a]-d[b])
    if d[a] == d[b]:
        return d
    d['equality'] = False
    d['difference'] = dif
    return d

print(equal_count("Peter!@#$Paul&*#Peter!--@|#$Paul#$Peter@|Paul$%^^Peter++Paul%$%^Peter++Paul#$#$#Peter@|Paul", "Peter&Paul"))

print(equal_count("Elliot!@#$Sam!--@|#$Elliot@|Sam++Elliot$%^Elliot@|Sam!@#Elliot!@#$Sam!--@|#$Elliot", "Sam&Elliot"))

print(equal_count("Tim!@#$Kit&&*#Tim!--@|#$Kit#$%Tim@|Kit$%^^Tim++Kit%$%^Tim++Kit#$#$#Tim@|Kit", "Ken&Tom"))