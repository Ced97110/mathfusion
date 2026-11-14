import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
g=8.5; ox,oy=8,28
for a in range(9):
    for b in range(4):
        r='fixe'
        if a==b: r='sujet'
        if b==0: r='autre'
        if a==0 and b==0: r='resultat'
        disc(ax,ox+a*g,oy+b*g,1.7,r)
disc(ax,ox+8*g,oy+3*g,1.7,'varie')
arrow(ax,(ox+3*g+2.4,oy+3*g+0.0),(ox+8*g-2.4,oy+3*g),'varie')
text(ax,ox+5.5*g,oy+3*g+4,'+ (5, 0)','varie','s')
text(ax,ox+3*g,oy+3*g+4,'(3, 3)','sujet','s')
text(ax,ox+8*g-3,oy+3*g-4.5,'(8, 3)','varie','s')
text(ax,4,20,'S : paires de deux nombres égaux','sujet','s',ha='left')
text(ax,4,14,'I : paires dont le second est 0','autre','s',ha='left')
text(ax,4,8,'S ∩ I = {(0, 0)} : idéal de S','resultat','s',ha='left')
text(ax,4,2.6,'S + I : toutes les paires, sous-anneau','fixe','s',ha='left')
save(fig,'52-167')
