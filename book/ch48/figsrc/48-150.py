import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
box(ax,12,78,64,12,'sujet'); text(ax,44,84,r'$\varphi(\alpha)\,\varphi(\beta)=\varphi(\alpha+\beta)$','sujet','m')
arrow(ax,(30,78),(22,72),'varie'); arrow(ax,(58,78),(66,72),'varie')
forms=[(22,'partie réelle',"cos(α+β) =\ncosα cosβ − sinα sinβ"),(66,'partie imaginaire',"sin(α+β) =\nsinα cosβ + cosα sinβ")]
for x,t,fm in forms:
    box(ax,x-21.5,46,43,26,'fixe'); text(ax,x,67,t,'fixe','s',weight='bold'); text(ax,x,56,fm,'encre','s')
cases=[(22,"90° et 90°\n0×0 − 1×1 = −1"),(66,"90° et 90°\n1×0 + 0×1 = 0")]
for x,c in cases:
    arrow(ax,(x,46),(x,38),'varie')
    box(ax,x-21.5,24,43,14,'resultat',label=c,size='s')
    arrow(ax,(x,24),(44+(x-44)*0.4,17),'resultat')
box(ax,24,4,40,13,'resultat'); text(ax,44,10.5,r'$\varphi(180°)=-1$','resultat','m')
save(fig,'48-150')
