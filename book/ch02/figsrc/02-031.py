import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
for y in (58,24):
    f=numberline(ax,8,84,y,0,10,1,labels=False,role='fixe',arrow_right=False)
    text(ax,8,y-4.5,'0','fixe','s')
    disc(ax,f(9),y,1.3,'sujet'); text(ax,f(9),y-4.5,r'$m$ = 9','sujet','s')
arrow(ax,(76.4,60),(46,60),'varie',curve=0.3)
text(ax,61.2,70,r'recule de $s$ = 4','varie','s')
disc(ax,38.4,24,1.3,'varie'); text(ax,38.4,19.5,r'$s$ = 4','varie','s')
disc(ax,46,58,1.6,'resultat'); text(ax,46,53.5,r'$d$ = 5 : un point','resultat','s')
line(ax,[(38.4,24),(76.4,24)],'resultat',lw=2.5)
brace(ax,38.4,76.4,26.5,'resultat',r'$d$ = 5 : une longueur',down=False)
text(ax,46,42,'même nombre : 5','resultat','s')
save(fig,'02-031')
