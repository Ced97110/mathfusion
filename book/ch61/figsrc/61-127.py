import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
names=[('E','sujet',70,r'$E$ : contient $u$'),('K','fixe',48,r'$K$ : les $a_i$ y sont'),('L','varie',26,r'$L$ : engendré par les $a_i$'),('F','fixe',4,r'$F$ : corps de base')]
for k,r,y,l in names: box(ax,3,y,40,14,r,label=l,size='s')
for y in (62,40,18):
    arrow(ax,(10,y-4+4),(10,y),'fixe',both=False) if False else None
arrow(ax,(8,26),(8,18),'resultat'); text(ax,27,22,r'$[L:F]$ fini','resultat','s')
arrow(ax,(8,70),(8,62),'sujet'); text(ax,27,66,r'$u$ : degré $n$','sujet','s')
line(ax,[(8,48),(8,40)],'fixe'); line(ax,[(8,26+14),(8,40)],'fixe')
box(ax,50,70,36,14,'sujet',label=r'Départ : $u$ sur $K$',size='s')
box(ax,50,37,36,14,'varie',label=r'Clé : garder les $a_i$',size='s')
box(ax,50,4,36,14,'resultat',label=r'Arrivée : $u$ sur $F$',size='s')
arrow(ax,(68,70),(68,51),'fixe'); arrow(ax,(68,37),(68,18),'fixe')
save(fig,'61-127')
