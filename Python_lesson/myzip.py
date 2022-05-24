def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    return res

def mymapPad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res

s1 = "abc"
s2 = "xyz123"
print(myzip(s1, s2))
print(mymapPad(s1, s2))
print(mymapPad(s1, s2, pad="Default"))