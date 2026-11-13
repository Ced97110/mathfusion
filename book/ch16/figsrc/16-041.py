import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,52,r'$5y+8$ avec $y=-6$','sujet','l')
def row(y,items,x0):
    x=x0
    for l,r,wd in items:
        box(ax,x,y,wd,11,r,label=l,size='m'); x+=wd+1.5
text(ax,44,41,'sans parenthèses : faux','limite','s')
row(26,[('5','fixe',8),(r'$-6$','varie',12),(r'$+\,8$','fixe',12),(r'$=\,7$','limite',12)],14)
text(ax,44,22,'avec parenthèses : juste','resultat','s')
row(7,[('5','fixe',8),(r'$\times$','fixe',8),(r'$(-6)$','varie',15),(r'$+\,8$','fixe',11),(r'$=\,-22$','resultat',17)],4.5)
save(fig,'16-041')
