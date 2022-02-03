"""
Create a function that takes an imgur link (as a string) and extracts the unique id and type.
Return an object containing the unique id, and a string indicating what type of link it is.

The link could be pointing to:

An album (e.g. http://imgur.com/a/cjh4E)
A gallery (e.g. http://imgur.com/gallery/59npG)
An image (e.g. http://imgur.com/OzZUNMM)
An image (direct link) (e.g. http://i.imgur.com/altd8Ld.png)
Examples
imgurUrlParser("http://imgur.com/a/cjh4E") ➞ { id: "cjh4E", type: "album" }

imgurUrlParser("http://imgur.com/gallery/59npG") ➞ { id: "59npG", type: "gallery" }

imgurUrlParser("http://i.imgur.com/altd8Ld.png") ➞ { id: "altd8Ld", type: "image" }
"""
import re
def imgurUrlParser(url):

    di = {}
    nw =url.split('/')
    if not nw[-1].endswith('png'):
        di['id'] = nw[-1]
    else:
        di['id'] = nw[-1].strip('.png')
        di['type'] = 'image'
    for i in range(len(nw)):
        if nw[i] == 'gallery':
            di['type'] = 'gallery'
        if nw[i] == 'a':
            di['type'] = 'album'
    return di



print(imgurUrlParser("http://imgur.com/gallery/59npG"))

print(imgurUrlParser("http://i.imgur.com/altd8Ld.png"))