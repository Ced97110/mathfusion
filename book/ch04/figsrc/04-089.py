import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
ax.set_ylim(22,96)  # cadrage serré sur le contenu (y de 26 à 92), coordonnées de la spec inchangées
# expression sur deux étages : 6 + √(36 − 20), le tout divisé par 2
text(ax,17,80,'6 +','encre','l')
line(ax,[(27,79),(28.5,77),(31,85.5),(50,85.5)],'sujet',lw=1.0)
text(ax,41,80,'36 − 20','encre','l')
line(ax,[(8,73),(56,73)],'fixe',lw=1.2)
text(ax,32,67.5,'2','encre','l')
# étape 1 : tout le haut
box(ax,7,75,50,12.5,'varie',fill=False,dash=True)
text(ax,32,91,'1. tout le haut d’abord','varie','s')
# intérieur de la racine
box(ax,33,76.5,16,7,'sujet',fill=False,dash=True)
text(ax,66,73,'= 5','resultat','l')
# colonne des actions (gauche) et des états (droite)
actions=[('2. 36 − 20 = 16',58),('3. √16 = 4',48),('4. 6 + 4 = 10',38),('5. 10 ÷ 2 = 5',28)]
for t,y in actions:
    text(ax,19,y,t,'varie','m')
    arrow(ax,(34,y),(49,y),'varie')
states=[('(6 + √16) / 2',58),('(6 + 4) / 2',48),('10 / 2',38),('5',28)]
for t,y in states:
    if t=='5': text(ax,66,y,t,'resultat','l')
    else: text(ax,66,y,t,'sujet','m')
save(fig,'04-089')
