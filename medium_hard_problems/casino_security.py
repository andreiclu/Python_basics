"""
Casino Security
You're head of security at a casino that has money being stolen from it. You get the data in the form of strings and you have to set off an alarm if a thief is detected.

If there is no guard between thief and money, return "ALARM!"
If the money is protected, return "Safe"
String Components
x - Empty Space
T - Thief
G - Guard
$ - Money
Examples
security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"

security("xxTxxG$xxxx$xxxx") ➞ "Safe"

security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"
"""

def security(txt):

    a = txt.replace('x','')

    if 'T$' in a or '$T' in a:
        return "Alarm!"
    else:
        return "Safe!"




print(security("xGxx$xxGxxxTTT"))

print(security("TxGxx$xxx$xxxGxxT"))

print(security("xxxTxxxxT"))

print(security("xxGxxxGGG"))

print(security("xxTxxG$xxxx$xxxx"))

