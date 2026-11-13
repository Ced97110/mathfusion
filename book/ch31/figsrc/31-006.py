import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax,22,64,'à la main','fixe','m'); text(ax,66,64,'avec la table','resultat','m')
box(ax,4,42,36,14,'fixe',label='4 ÷ 0,8660',size='l')
text(ax,22,37,'division posée','fixe','s'); text(ax,22,33,'4 décimales','fixe','s')
box(ax,48,42,36,14,'resultat',label='4 × 1,1547',size='l')
text(ax,66,37,'= 4,6188','resultat','m'); text(ax,66,33,'une multiplication','resultat','s')
arrow(ax,(40,49),(48,49),'varie')
text(ax,44,26,'colonnes de la table','encre','s')
for i,t in enumerate([r'1/cos $\theta$',r'1/sin $\theta$',r'cos $\theta$/sin $\theta$']):
    box(ax,4+i*28,8,26,12,'sujet',label=t,size='s')
save(fig,'31-006')
