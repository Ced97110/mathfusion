import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
def plan(cx, role):
    poly(ax, [(cx - 17, 36), (cx + 17, 36), (cx + 17, 66), (cx + 17 - 34, 66)], role)
plan(22, 'sujet'); plan(66, 'sujet')
line(ax, [(8, 51), (36, 51)], 'fixe', lw=2.2)
text(ax, 22, 72, '1 pli', 'varie', 'm', weight='bold')
text(ax, 22, 31, 'droite fixe : dimension 1', 'fixe', 's')
r = 9
arrow(ax, (66 + r, 51), (66, 51 + r), 'varie', curve=0.4, lw=1.2)
disc(ax, 66, 51, 1.5, 'resultat')
text(ax, 66, 72, 'quart de tour', 'varie', 'm', weight='bold')
text(ax, 66, 31, 'point fixe : dimension 0', 'resultat', 's')
text(ax, 22, 25, r'$k=1$ : $2-1=1$', 'limite', 's')
text(ax, 22, 19, r'pas $\leq 0$', 'limite', 's')
text(ax, 66, 25, 'il faut dimension 0 :', 'encre', 's')
text(ax, 66, 19, r'$2-k\leq 0$', 'encre', 'm')
arrow(ax, (66, 15.5), (66, 12.5), 'resultat', lw=1.0)
box(ax, 4, 1, 80, 11, 'resultat', label=r'donc $k\geq 2$ : au moins 2 plis', size='m', weight='bold')
save(fig, '72-141')
