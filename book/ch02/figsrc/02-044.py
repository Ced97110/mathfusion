import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
text(ax,44,82,'addition : 4 + 9 = 9 + 4','autre','m')
for y in (56,28):
    numberline(ax,30,80,y,0,10,1,labels=False,role='fixe'); text(ax,30,y-3.5,'0','fixe','s')
f=lambda v:30+5*v
text(ax,12,64,'9 − 4','varie','l',weight='bold')
disc(ax,f(9),56,1.2,'varie'); text(ax,f(9),52.5,'9','varie','s')
arrow(ax,(f(9),60),(f(5),60),'varie')
disc(ax,f(5),56,1.4,'resultat'); text(ax,f(5),52.5,'5','resultat','s')
text(ax,12,40,'4 − 9','limite','l',weight='bold')
disc(ax,f(4),28,1.2,'limite'); text(ax,f(4),24.5,'4','limite','s')
arrow(ax,(f(4),32),(5,32),'limite')
line(ax,[(5,28),(30,28)],'limite',dash=True)
text(ax,17,23,'pas de réponse','limite','s')
text(ax,44,8,"l'ordre change le calcul",'encre','m',weight='bold')
save(fig,'02-044')
