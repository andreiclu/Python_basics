"""
Write a function that retrieves the top 3 longest words of a newspaper headline and transforms them into hashtags. If multiple words tie for the same length, retrieve the word that occurs first.

Examples
get_hash_tags("How the Avocado Became the Fruit of the Global Trade")
➞ ["#avocado", "#became", "#global"]

get_hash_tags("Why You Will Probably Pay More for Your Christmas Tree This Year")
➞ ["#christmas", "#probably", "#will"]

get_hash_tags("Hey Parents, Surprise, Fruit Juice Is Not Fruit")
➞ ["#surprise", "#parents", "#fruit"]

get_hash_tags("Visualizing Science")
➞ ["#visualizing", "#science"]
"""

def get_hash_tags(s):

    d = sorted((s.strip(',').split()), key=lambda x:len(x), reverse=True)

    # a = s.strip(',')
    # b = a.split()
    #
    # c = sorted(b, key= lambda x:len(x), reverse=True)
    lst = []
    d[0] = '#'+d[0]
    d[1] = '#'+d[1]
    d[2] = '#'+d[2]
    lst.append(d[0].lower())
    lst.append(d[1].lower())
    lst.append(d[2].lower())

    return lst


print(get_hash_tags("Hey Parents, Surprise, Fruit Juice Is Not Fruit"))


print(get_hash_tags("How the Avocado Became the Fruit of the Global Trade"))

