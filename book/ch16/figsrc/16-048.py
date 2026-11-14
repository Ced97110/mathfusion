import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,63,'solution : 4','sujet','s')
box(ax,14,48,60,12,'sujet',label=r'$x+3=7$',size='l')
for cx,role,lab,t,s in [(22,'resultat',r'$x=4$','− 3 des\ndeux membres','solution : 4'),(66,'limite',r'$x=7$','− 3 à gauche\nseulement','solution : 7')]:
    arrow(ax,(cx,48),(cx,28),'varie')
    box(ax,cx-12,16,24,12,role,label=lab,size='l')
    text(ax,cx+2 if cx<44 else cx-2,38,t,'varie','s',ha='left' if cx<44 else 'right')
    text(ax,cx,10,s,role,'s')
save(fig,'16-048')
