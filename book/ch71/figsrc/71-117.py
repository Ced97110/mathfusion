import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,24,71,'matrice symétrique','sujet','m')
for (r,c,v,role) in [(0,0,'5','fixe'),(0,1,'3','varie'),(1,0,'3','varie'),(1,1,'5','fixe')]:
    box(ax,8+c*16,40+(1-r)*14,16,14,role,label=v,size='l')
text(ax,66,48,'diagonale\n(5 et 5)','fixe','s')
text(ax,66,62,'hors diagonale :','varie','s')
text(ax,66,57.5,'deux cases égales','varie','s')
box(ax,16,6,56,10,'resultat',label=r'$3+3=6$ : le terme $6xy$',size='m')
arrow(ax,(41,61),(60,16),'varie',curve=-0.25)
arrow(ax,(14,40),(24,16),'varie',curve=0.2)
save(fig,'71-117')
