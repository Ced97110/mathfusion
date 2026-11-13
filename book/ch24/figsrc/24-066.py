import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,'24 ml à 10 % et 16 ml à 20 %','fixe','s')
box(ax,4,38,80,10,'sujet',label=r'$0{,}10 \times 24 + 0{,}20 \times 16 = 5{,}6$')
arrow(ax,(44,37),(44,22),'varie'); text(ax,62,29.5,'chaque côté × 10','varie','s')
box(ax,4,10,80,10,'resultat',label=r'$1 \times 24 + 2 \times 16 = 56$')
text(ax,44,4,'mêmes solutions, seulement des entiers','fixe','s')
save(fig,'24-066')
