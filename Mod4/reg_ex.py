# ^0253\s[0-9]{6}
# ^076\s[0-9]{7}
# ^[\w.+\-]+@gmail\.com$
#
import re

versuri_necenzurate_celebre = """
La noi in cartier cu sau fara legatura
Love nu egal lovele manele nu egal cultura
Portretul luptatorului la tinerete nu-i caricatura
"""

# ura = "ura"
#
# versuri_necenzurate_celebre.replace('ura', 'ula')
# print(versuri_necenzurate_celebre)

print(re.sub("ura", "ula", versuri_necenzurate_celebre))

