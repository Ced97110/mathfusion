import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,8,80,32,0,11,labels=False,arrow_right=False)
Hs=[0,3,6,9]; G=[2,5,8,11]
for v in range(12):
    if v not in Hs+G: disc(ax,f(v),32,1.0,'fixe')
for v in Hs:
    disc(ax,f(v),32,1.9,'sujet'); text(ax,f(v),26,str(v),'sujet','s')
for v in G:
    disc(ax,f(v),32,1.9,'resultat'); text(ax,f(v),26,str(v),'resultat','s')
for v in Hs: arrow(ax,(f(v)+1,34.5),(f(v+2)-1,34.5),'varie',curve=-0.6)
text(ax,44,50,r'$g+H$ avec $g=2$','resultat','m')
text(ax,44,43,'+ 2','varie','s') if False else None
text(ax,20,18,'H : multiples de 3','sujet','s')
text(ax,62,18,'2 + H : la ligne de 2','resultat','s')
save(fig,'47-038')
