import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
y=30; A,D,C=8,24,72
line(ax,[(A,y),(D,y)],'fixe',2.2); line(ax,[(D,y),(C,y)],'sujet',2.2)
for x,r in [(A,'fixe'),(D,'varie'),(C,'sujet')]: disc(ax,x,y,1.8,r)
for x,n in [(A,'A'),(D,'D'),(C,'C')]: text(ax,x,y+5,r'$'+n+'$')
brace(ax,A,D,25,'fixe','1'); brace(ax,D,C,25,'sujet',r'$a$')
brace(ax,A,C,16,'resultat',r'$AC = 1 + a$')
save(fig,'61-211')
