
# coding: utf-8

# In[2]:


import sys
import operator


def print_words(fname):
    wc= count_(fname)
    for key in sorted(wc):
     print( "%s: %s" % (key, wc[key]))
    
    
def count_(fname):    

    text= open(fname)
    w_dic= text.read().lower().split()
    w_c= {}
    for w in w_dic:
        if ',' in w or  '.' in w:
            w= w[0:-1]
        if w not in w_c:
            w_c[w] = 0
        w_c[w] += 1 
    return w_c    
    
  


def print_top(fname):
    wc= count_(fname)
    s = sorted(wc.items(), key=operator.itemgetter(1),reverse=True)
   
    for key in range(20):
        print( s[key][0],s[key][1])
   



def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()

