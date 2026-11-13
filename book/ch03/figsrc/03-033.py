import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(70)
text(ax,22,64,'49 000 × 1 200','encre','m'); arrow(ax,(34,64),(46,64),'varie'); text(ax,62,64,'49 × 12 = 588','sujet','m')
for x in [56,60,64,68,72]: disc(ax,x,56,1.1,'varie',fill=False,lw=1)
text(ax,28,56,'zéros mis de côté','varie','s'); arrow(ax,(24,61.5),(54,57),'varie',lw=0.7)
arrow(ax,(64,54.5),(64,50.5),'varie'); text(ax,64,47,'rendus : 58 800 000','resultat','m')
line(ax,[(4,42),(84,42)],'fixe',lw=0.5); line(ax,[(4,24),(84,24)],'fixe',lw=0.5)
text(ax,44,35,'oubli des zéros : 588','limite','m'); text(ax,44,29,'100 000 fois trop petit','limite','s')
# 405 : le zéro du milieu n'est PAS à droite -> encadré en rouge, flèche vers l'étiquette
for x,c in [(8,'4'),(12,'0'),(16,'5')]: text(ax,x,18,c,'resultat','m')
text(ax,20,18,'× 12 = 4 860','resultat','m',ha='left')
disc(ax,12,18,2.3,'limite',fill=False,lw=1.1)
text(ax,62,18,'zéro du milieu : pas à droite','limite','s')
text(ax,22,6,'45 × 12 = 540','limite','m'); arrow(ax,(34,6),(46,6),'varie')
text(ax,59,6,'5 400 : faux','limite','m'); text(ax,78,6,'≠ 4 860','resultat','m')
save(fig,'03-033')
