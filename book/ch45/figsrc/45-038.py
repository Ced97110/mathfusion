import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(85)
def row(y,lab,a,b,ra,rb):
    text(ax,44,y+11,lab,'encre','m',weight='bold')
    box(ax,6,y-5,32,10,ra,label=a,size='m')
    arrow(ax,(41,y),(53,y),'varie')
    box(ax,56,y-5,26,10,rb,label=b,size='m')
row(70,'1. Neutre',r'$0$',r'$1$','sujet','resultat')
row(42,'2. Calcul',r'$x+y$',r'$2^x\cdot 2^y$','sujet','resultat')
row(14,'3. Un seul antécédent',r'$3$',r'$8$','sujet','resultat')
save(fig,'45-038')
