import json
import random

def getn(w):
    return w["n"][random.randint(0,len(w["n"])-1)]

def geta(w):
    return w["a"][random.randint(0,len(w["a"])-1)]

def handleSentence(s):
    res = s["sen"]
    acnt = 1
    while acnt <= s["a"] :
        res = res.replace("%a"+str(acnt),geta(words))
        acnt = acnt + 1
    ncnt = 1
    while ncnt <= s["n"] :
        res = res.replace("%n"+str(ncnt),getn(words))
        ncnt = ncnt + 1
    return res


f = open("sentence.json","r")
sens = json.load(f)
f = open("word.json","r")
words = json.load(f)

res = ""

sencnt = 0

while sencnt < len(sens["front"]):
    res = res + handleSentence(sens["front"][sencnt])
    sencnt = sencnt + 1

res = res + "\n"

sencnt = 0

while sencnt < len(sens["mid"]):
    res = res + handleSentence(sens["mid"][sencnt])
    sencnt = sencnt + 1

res = res + "\n"

sencnt = 0

while sencnt < len(sens["end"]):
    res = res + handleSentence(sens["end"][sencnt])
    sencnt = sencnt + 1

f = open("result.txt","w")
f.write(res)
f.close()