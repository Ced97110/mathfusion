import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,r'$4+7\sqrt{2}$','encre','l')
for i in range(4): box(ax,4+i*9.5,34,8,8,'fixe')
brace(ax,4,4+3*9.5+8,32,'fixe',r'4 briques $1$')
for i in range(7): box(ax,4+i*11.5,12,10,8,'varie')
brace(ax,4,4+6*11.5+10,10,'varie',r'7 briques $\sqrt{2}$')
text(ax,44,2.5,'2 sortes de briques : degré 2','sujet','s') if False else None
save(fig,'61-028')
