import string
from itertools import cycle
from collections import Counter

cipher = "cdiiddwpgswtgt"

# Load a small English wordlist for scoring
with open("/usr/share/dict/words") as f:
    english = {w.strip().lower() for w in f if w.strip().isalpha()}

def score_english(s):
    # simple score: number of real words of length ≥3
    return sum(1 for w in s.split() if len(w)>=3 and w in english)

def caesar(s, shift):
    return "".join(
        chr((ord(c)-97 + shift) %26 +97) if 'a'<=c<='z' else c
        for c in s
    )

def progressive(s, shift, forward=True):
    out=[]
    for i,c in enumerate(s):
        delta = shift + i
        if forward:
            v = (ord(c)-97 + delta)%26
        else:
            v = (ord(c)-97 - delta)%26
        out.append(chr(v+97))
    return "".join(out)

def vigenere(s, key):
    out=[]
    for c,k in zip(s, cycle(key)):
        delta = ord(k)-97
        v = (ord(c)-97 - delta)%26
        out.append(chr(v+97))
    return "".join(out)

def xor_singlebyte(s, key):
    out=[]
    for c in s:
        out.append(chr((ord(c)^key)%256))
    return "".join(out)

candidates = []

# 1) All Caesar shifts
for sh in range(26):
    pt = caesar(cipher, sh)
    candidates.append((f"caesar {sh}", pt, score_english(pt)))

# 2) Progressive shifts +/- initial 0–5
for base in range(6):
    for dirn in (True, False):
        pt = progressive(cipher, base, forward=dirn)
        candidates.append((f"prog_shift {'+' if dirn else '-'}{base}", pt, score_english(pt)))

# 3) Vigenère with some common small keys
for key in ["key", "ctf", "flag", "john", "pass", "pwd"]:
    pt = vigenere(cipher, key)
    candidates.append((f"vigenere {key}", pt, score_english(pt)))

# 4) Single‑byte XOR
for k in range(1,256):
    pt = xor_singlebyte(cipher, k)
    # filter to printable
    if all(32 <= ord(ch) < 127 for ch in pt):
        candidates.append((f"xor {k}", pt, score_english(pt)))

# sort by English score descending, then print top 10
for tag,pt,sc in sorted(candidates, key=lambda x:(-x[2], x[0]))[:10]:
    print(f"{tag:20s} | score={sc:2d} | {pt}")
