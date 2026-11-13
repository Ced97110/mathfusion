import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
rows=[(r'$6\times4+6\times7$','6'),(r'$5\times2+5\times9$','5'),(r'$8\times3+8\times1$','8')]
for i,(s,n) in enumerate(rows):
    y=46-16*i
    box(ax,2,y-5,42,10,'fixe',label=s)
    arrow(ax,(44,y),(50,y),'autre')
    box(ax,50,y-5,8,10,'autre',label=n)
    arrow(ax,(58,y),(70,30),'autre')
text(ax,54,57,'nombre écrit 2 fois','autre','s')
box(ax,70,22,14,16,'autre',label=r'$a$',size='xl')
text(ax,77,17,'un seul signe','autre','s')
save(fig,'18-027')
