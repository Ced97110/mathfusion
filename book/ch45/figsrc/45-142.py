import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
text(ax,20,51,'multiplicative','fixe','m',weight='bold'); text(ax,66,51,'additive','sujet','m',weight='bold')
L=[r'opération $a\cdot b$',r'neutre $1$',r'inverse $a^{-1}$',r'répété $a^n$']
R=[r'$a+b$',r'$0$',r'$-a$',r'$n\,a$']
for y,l,r in zip([38,26,14,2],L,R):
    box(ax,4,y,32,9,'fixe',label=l,size='s'); box(ax,50,y,32,9,'sujet',label=r,size='m')
    arrow(ax,(38,y+4.5),(48,y+4.5),'varie')
save(fig,'45-142')
