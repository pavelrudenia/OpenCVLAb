with open(r'text.txt',encoding="utf8") as f:
   lst = f.read().lower().translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~—',)
   ).split()
res = {x:lst.count(x) for x in lst if len(x)>2}
print(res)
print(max(res, key=res.get))
