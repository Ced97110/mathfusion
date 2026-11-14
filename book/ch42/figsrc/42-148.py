import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
for y,(a,b),(ra,rb),(la,lb),t in ((36,('A {1, 2}','B {2, 3}'),('sujet','autre'),('A','B'),'A puis B'),(12,('B {2, 3}','A {1, 2}'),('autre','sujet'),('B','A'),'B puis A')):
    box(ax,2,y-6,22,12,ra,label=a,size='s'); text(ax,28,y,r'$\cup$','varie','l')
    box(ax,32,y-6,22,12,rb,label=b,size='s'); arrow(ax,(56,y),(62,y),'resultat')
    box(ax,64,y-6,22,12,'resultat',label=r'$\{1,2,3\}$',size='s'); text(ax,27,y+9,t,'varie','s')
save(fig,'42-148')
