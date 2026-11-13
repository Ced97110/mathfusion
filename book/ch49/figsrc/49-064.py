import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
text(ax,22,88,'FG : infinité de mots','sujet','m'); text(ax,72,88,'G : 8 gestes','resultat','m')
text(ax,52,82.5,'η','encre','m')
for i in range(8):
    y0=72-9.3*i; yc=y0+3.5; r='varie' if i==0 else 'sujet'
    box(ax,4,y0,36,7,r)
    for j in range(3): disc(ax,10+6*j,yc,1.4,r)
    arrow(ax,(41,yc),(63,yc),r)
    disc(ax,72,yc,2.8,'varie' if i==0 else 'resultat',label='1' if i==0 else None,size='s')
text(ax,33,75.5,'K','varie','m')
text(ax,44,2.5,'FG/K : 8 paquets, un par élément de G','encre','s')
save(fig,'49-064')
