import json
import sys
from concurrent.futures import ProcessPoolExecutor as PPE
import glob
import plyvel
def _term_chaine(arr):
  index, fn = arr
  try:
    print('now iter', index)
    db = plyvel.DB(f'tmp/level_min_batch_{index:04d}/', create_if_missing=True)
    fp = open(fn) 
    for aindex, line in enumerate(fp):
      #if aindex > 1000:
      #  break
      line = line.strip()
      terms = line.split()
      terms += ['<EOS>']
      for i in range(len(terms)-1):
        key = bytes(terms[i], 'utf8')
        next = bytes(terms[i+1], 'utf8')
        if db.get(key) is None:
          db.put(key, b'0' )
        db.put(key, bytes(str(int(db.get(key).decode())+1),'utf8') )
      
      # two terms
      for i in range(len(terms)-2):
        key = bytes(' '.join( terms[i:i+2] ), 'utf8')
        next = bytes(terms[i+2], 'utf8')
        if db.get(key) is None:
          db.put(key, b'0' )
        db.put(key, bytes(str(int(db.get(key).decode())+1),'utf8') )
      # three terms
      for i in range(len(terms)-3):
        key = bytes(' '.join( terms[i:i+3] ), 'utf8')
        next = bytes(terms[i+2], 'utf8')
        if db.get(key) is None:
          db.put(key, b'0' )
        db.put(key, bytes(str(int(db.get(key).decode())+1),'utf8') )
  except Exception as ex:
    print(ex)

arrs = [(index,fn) for index, fn in enumerate(glob.glob('tmp/tokenized_*.txt'))]
#_term_chaine(arrs[0])
print('run as concurrent')
with PPE(max_workers=4) as exe:
  exe.map(_term_chaine, arrs)
