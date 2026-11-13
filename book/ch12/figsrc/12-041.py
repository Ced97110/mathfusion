import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
rows=[(34,r'$8=5$','limite','faux',r'$8\neq5$','resultat','vrai'),(8,r'$8=8$','resultat','vrai',r'$8\neq8$','limite','faux')]
for y,a,ra,ta,b,rb,tb in rows:
    box(ax,4,y,28,18,ra,label=a,size='l'); text(ax,18,y-3,ta,ra,'s')
    box(ax,56,y,28,18,rb,label=b,size='l'); text(ax,70,y-3,tb,rb,'s')
    arrow(ax,(33,y+9),(55,y+9),'varie')
text(ax,44,48,'barrer','varie','m')
save(fig,'12-041')
