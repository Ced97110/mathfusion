import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# row 1 : the known case, C over R
box(ax, 4, 54, 14, 9, 'fixe', label=r'$\mathbb{C}$')
box(ax, 70, 54, 14, 9, 'fixe', label=r'$\mathbb{R}$')
arrow(ax, (18.5, 58.5), (69.5, 58.5), 'autre', lw=1.2)
text(ax, 44, 63, r'$z\mapsto z\bar{z}=|z|^2$', 'autre', 's')
text(ax, 44, 53, r'$|zw|^2=|z|^2|w|^2$', 'autre', 's')
# row 2 : same idea in a field extension
box(ax, 4, 28, 14, 9, 'sujet', label=r'$E$')
box(ax, 70, 28, 14, 9, 'sujet', label=r'$F$')
arrow(ax, (18.5, 32.5), (69.5, 32.5), 'sujet', lw=1.2)
text(ax, 44, 37, r'$u\mapsto\eta_1(u)\cdots\eta_n(u)$', 'sujet', 's')
text(ax, 44, 27, r'$N(uv)=N(u)N(v)$', 'sujet', 's')
box(ax, 14, 6, 60, 9, 'sujet', label='norme = produit des conjugués', size='s')
save(fig, '67-137')
