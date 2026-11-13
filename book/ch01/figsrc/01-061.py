import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
text(ax,44,69,'Traits : chaque trait vaut 1','autre','s')
for x in [8,11,14,17,25,28,31,56,59,62,70,73,76,79]:
    line(ax,[(x,52),(x,63)],'autre',lw=1.4)
arrow(ax,(35,57.5),(51,57.5),'varie')
text(ax,44,46,'même total : 7','autre','s')
line(ax,[(4,41),(84,41)],'fixe',dash=True)
text(ax,44,37,'Position : la place compte','sujet','s')
for x0,digs in [(4,'4329'),(56,'3429')]:
    for i,d in enumerate(digs):
        role='varie' if d=='3' else 'sujet'
        box(ax,x0+7*i,17,7,9,role,label=d,size='l')
text(ax,44,21.5,'≠','encre','l')
arrow(ax,(14.5,26),(59.5,26),'varie',curve=-0.25)
for x,s in [(14.5,'300'),(59.5,'3 000')]:
    arrow(ax,(x,17),(x,11),'resultat')
    text(ax,x,8.5,s,'resultat','m')
save(fig,'01-061')
