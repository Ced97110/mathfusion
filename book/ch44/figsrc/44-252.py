import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
rows=[(52,'fixe',r'$g$',2,r'$g^{2}$',r'2 facteurs $g$'),(32,'autre',r'$g^{-1}$',1,r'$g^{-1}$',r'1 facteur $g^{-1}$'),(12,'sujet',r'$g^{-1}$',2,r'$g^{-2}$',r'2 facteurs $g^{-1}$')]
for y,r,l,n,nm,d in rows:
    text(ax,3,y+5.5,nm,r,'l',ha='left')
    for k in range(n): box(ax,22+k*19,y,16,11,r,label=l)
    text(ax,62,y+5.5,d,r,'s',ha='left')
save(fig,'44-252')
