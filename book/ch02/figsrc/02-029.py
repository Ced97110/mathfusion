import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
for x,y,s,r in [(30,54,'1','encre'),(42,54,'8','encre'),(20,46,'+','encre'),(30,46,'3','encre'),(42,46,'4','encre'),(30,35,'5','resultat'),(42,35,'2','resultat')]:
    text(ax,x,y,s,r,'l')
line(ax,[(18,41),(47,41)],'encre')
text(ax,50,54,'8 + 4 =','encre','m',ha='left'); text(ax,62,54,'12','varie','m',ha='left')
disc(ax,30,62,2.2,'varie',label='1',size='s')
arrow(ax,(63,57),(32.5,62.5),'varie',lw=1.0,curve=0.2)
text(ax,58,67.5,'note : ajoute 1 dizaine ici','varie','s')
box(ax,26.5,31,7,34.5,'varie',fill=False,dash=True,lw=0.6)
text(ax,50,40,'petit 1 + 1 + 3 = 5','encre','s',ha='left')
text(ax,50,46,'ni chiffre de 18, ni de 52','fixe','s',ha='left')
text(ax,50,34,'52 s’écrit sans la note','resultat','s',ha='left')
save(fig,'02-029')
