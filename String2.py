

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def verbing(s):
    a=len(s)
    b=0
    
    if a>= 3:
        if s[-3:]=='ing':
            b= s+'ly'
        elif s[-3:]!='ing' :
            b= s+'ing'
    else:
         b=s
    return b


def not_bad(s):
    x=s.find('not')
    y=s.find('bad')
    
    if (x<y):
        s=s.replace(s[x:y+3],'good');
    return s


def front_back(a, b):
    
    c=int((len(a)/2)+0.5)
    d=int((len(b)/2)+0.5)
    x=a[0:c]+b[0:d]+a[c:]+b[d:]
    
    return x
    


def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')
  print()

  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  
  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()

