import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,6,58,76,16,'sujet'); text(ax,44,70,r'départ : $b\equiv 0$','sujet'); text(ax,44,63,'8 ≡ 0 : 8 est multiple de 4','sujet','s')
box(ax,6,34,76,16,'varie'); text(ax,44,46,r'étape clé : $b$ devient 0','varie'); text(ax,44,39,r'5 × 8 ≡ 5 × 0 = 0','varie','s')
box(ax,6,10,76,16,'resultat'); text(ax,44,22,r'arrivée : $ab\equiv 0$','resultat'); text(ax,44,15,r'40 ≡ 0, donc 40 ∈ $I$','resultat','s')
arrow(ax,(44,58),(44,50),'fixe'); arrow(ax,(44,34),(44,26),'fixe')
save(fig,'52-036')
