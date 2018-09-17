from pwn import *
from z3 import *

r=remote("misc.chal.csaw.io",9002)

r.recvuntil('****')

def rec():
  return r.recvuntil('\n').strip('\n')

def usez3(q):
  X, y, z = Reals('X y z')
  s = Solver()
  q=q.replace('=','==')
  eval("""s.add(X>-500, X<1000, """+q+""")""")
  print s.check()
  m=s.model()
  out=(str(m).split('=')[1].replace(' ','').replace(']',''))
  if out.find('/')!=-1:
      l=out.split('/')
      return float(int(l[0]))/int(l[1])
  return int(out)


while(1):
  rec()
  eq=rec()
  q=eq
  print q
  eq=eq.split(' ')
  sol=usez3(q)
  r.sendlineafter("What does X equal?: ",str(sol))
  r.recvuntil("YAAAAAY keep going")
r.interactive()