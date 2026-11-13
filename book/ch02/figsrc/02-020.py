import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for y,und in [(60,[(4,5.9,'sujet')]),(37,[(4,12.6,'varie')]),(14,[(4,19.3,'resultat')])]:
    text(ax,4,y,'a + b = S','fixe','l',ha='left')
    for x0,x1,r in und: line(ax,[(x0,y-2.8),(x1,y-2.8)],r,lw=1.6)
    f=numberline(ax,32,82,y,0,10,1,labels=False,arrow_right=False)
    text(ax,32,y-3.4,'0','fixe','s')
    disc(ax,f(4),y,1.3,'sujet')
    if y==60: text(ax,f(4),y-3.4,'a = 4','sujet','s')
    else: arrow(ax,(f(4),y+0.5),(f(7),y+0.5),'varie',curve=-0.4)
    if y==37: text(ax,59.5,43,'b = 3','varie','s')
    if y==14:
        disc(ax,f(7),y,1.6,'resultat'); text(ax,f(7),y-3.4,'S = 7','resultat','s')
        text(ax,73,19.5,"on s'arrête",'resultat','s')
save(fig,'02-020')
