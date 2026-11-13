import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,4,46,80,12,'fixe',label=r'fraction $+$ fraction $\times\sqrt{2}$',size='m')
arrow(ax,(44,45),(44,35),'varie'); text(ax,50,40,'on abrège','varie','s',ha='left')
box(ax,24,22,40,12,'sujet',label=r'$\mathbb{Q}(\sqrt{2})$',size='xl')
line(ax,[(30,21),(30,17)],'sujet'); line(ax,[(58,21),(58,17)],'varie')
text(ax,24,12,'ℚ : fractions','sujet','s',ha='center'); text(ax,64,12,r'$(\sqrt{2})$ : on ajoute $\sqrt{2}$','varie','s')
save(fig,'51-075')
