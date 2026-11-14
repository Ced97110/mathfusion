import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def row(y,a,b,c,role,tag):
    box(ax,2,y,22,12,'sujet',label=a,size='m'); box(ax,34,y,20,12,'fixe',label=b,size='m'); box(ax,66,y,20,12,role,label=c,size='m')
    arrow(ax,(24,y+6),(34,y+6),'varie'); arrow(ax,(54,y+6),(66,y+6),'varie')
    text(ax,29,y+10,r'$x=4$','varie','s'); text(ax,60,y+10,r'$x=4$','varie','s')
    text(ax,76,y-3.5,tag,role,'s')
row(38,r'$x+3$',r'$4+3$','7','fixe','nombre')
row(10,r'$x+3=7$',r'$4+3=7$',r'$7=7$','resultat','vrai')
text(ax,44,58,'on remplace x par 4','encre','s')
save(fig,'16-036')
