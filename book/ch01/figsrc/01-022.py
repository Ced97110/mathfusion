import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
line(ax,[(6,26),(12,26)],'fixe')
line(ax,[(12,26),(13,27.6),(14,24.4),(15,27.6),(16,26)],'fixe')
arrow(ax,(16,26),(85,26),'fixe',lw=0.9)
for x in (6,28,52,76): line(ax,[(x,24.8),(x,27.2)],'fixe',lw=0.8)
text(ax,6,22,'0','fixe','s')
disc(ax,28,26,1.3,'sujet')
text(ax,28,22,'1 000 000 000','sujet','s'); text(ax,28,42,'entier donné','sujet','s')
for a in (28,52):
    arrow(ax,(a,27.5),(a+24,27.5),'varie',curve=-0.3)
    text(ax,a+12,34,'+1','varie','s')
for x,l,t in ((52,'1 000 000 001','plus grand'),(76,'1 000 000 002','encore plus')):
    disc(ax,x,26,1.3,'resultat')
    text(ax,x,22,l,'resultat','s'); text(ax,x,42,t,'resultat','s')
text(ax,44,10,'pour tout entier : +1 marche','resultat','m')
save(fig,'01-022')
