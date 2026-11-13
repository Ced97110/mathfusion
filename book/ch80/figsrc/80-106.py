import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,16,64,'sous-espaces','sujet','s'); text(ax,72,64,'sous-espaces','resultat','s')
for i,(a,b) in enumerate([(r'$\{0\}$',r'$\{0\}$'),(r'droite $(a,a)$',r'droite $(a,a)$'),(r'$\mathbb{C}^2$',r'$\mathbb{C}^2$')]):
    y=48-i*16
    box(ax,3,y-5,26,10,'sujet',label=a,size='s'); box(ax,59,y-5,26,10,'resultat',label=b,size='s')
    arrow(ax,(29,y),(59,y),'varie'); 
    text(ax,44,y+3.5,r'$[\eta]$','varie','s')
text(ax,44,6,r'$U\mapsto\eta(U)$ pour chaque $U$','varie','s')
save(fig,'80-106')
