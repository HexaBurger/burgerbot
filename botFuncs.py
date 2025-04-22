from twitchio.ext import commands
import re, random, string, twitchio

def commandLength(ctx: commands.Context):
    return len(ctx.command.name) + len(ctx.prefix) + 1

def nameScore(scoreName: str, name: str) -> float:
    scores = dict()
    score = 0
    multStr = ""

    for i, s in enumerate(scoreName):
        if not s in scores:
            multStr += s
            scores[s] = 1 - i / len(scoreName)

    mult = 1 + 0.02 * len(multStr)
    
    for s in name:
        if s in scores: score += scores[s]

    for s in multStr:
        if s not in name:
            mult = 1
            break

    return score * mult
    
def corpusSpeech(text: str) -> str:
    chars = list(string.ascii_lowercase)
    random.seed()
    randID = random.randint(100,999)

    text = re.sub(r'c[hH]',f'<{randID}?24>',text)
    text = re.sub(r'C[hH]',f'<{randID}!24>',text)
    rep = (("b",19),("c",24),("d",15),("f",19),("g",9),("h",10),("j",19),("l",15),("m",18),("n",19),("p",10),("q",17),("r",19),("s",24),("t",15),("v",10),("w",9),("x",24),("z",1))

    for a,b in rep:
        text = text.replace(a,f'<{randID}?{b}>')
        text = text.replace(a.upper(),f'<{randID}!{b}>')
        
    for i in range(26):
        text = text.replace(f'<{randID}?{i}>',chars[i])
        text = text.replace(f'<{randID}!{i}>',chars[i].upper())

    return text
