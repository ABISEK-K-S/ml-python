


def donuts(count):
    if count<10:
        str="Number of donuts: {}".format(count);
    else:
        str="Number of donuts: many";

     
    return str

def both_ends(s):
    if len(s)<2:
        str=""
    else:
        str= s[0:2] 
        str= str+s[-2:]  
    return str

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
        
        
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
    
    
def fix_start(s):
    var = s[0]
    for i in range(0, len(s)):
        if s[i]== var:
            s = s.replace(s[i],'*')
    s=var+s[1:] 
    return s
    
    
def mix_up(a, b):
  
  temp=a[0:2]
  a=b[0:2]+a[2:]
  b=temp+b[2:]
  return a+" "+b    
    
    
def main():
  print('donuts')
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print()
  print('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print()
  print('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print()
  print('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')
      
if __name__ == '__main__':
  main()

