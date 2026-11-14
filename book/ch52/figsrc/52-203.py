import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,22,60,r'$k=0$ : ℤ','sujet','m'); text(ax,66,60,r'$k=6$ : ℤ/6ℤ','autre','m')
for i in range(5):
    x=8+i*7
    disc(ax,x,44,1.5,'sujet'); disc(ax,x,18,1.5,'resultat'); arrow(ax,(x,42),(x,20),'varie',lw=0.7)
for i in range(9):
    x=48+i*4.5
    disc(ax,x,44,1.5,'sujet' if i<6 else 'varie')
for j in range(6):
    disc(ax,48+j*7.2,18,1.5,'resultat')
for i in range(9):
    arrow(ax,(48+i*4.5,42),(48+(i%6)*7.2,20),'varie' if i>=6 else 'fixe',lw=0.6)
text(ax,22,8,'toutes distinctes','resultat','s'); text(ax,66,8,'6 valeurs, puis ça boucle','resultat','s')
save(fig,'52-203')
