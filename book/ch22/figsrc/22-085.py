import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(64)
fr(ax, 14, 40, r'$\sqrt{3}$', r'$\sqrt{5}$', 'sujet')
text(ax, 29, 40, r'$\times$', 'encre', 'xl')
fr(ax, 44, 40, r'$\sqrt{5}$', r'$\sqrt{5}$', 'varie')
text(ax, 44, 55, 'vaut 1', 'varie', 's')
text(ax, 59, 40, '=', 'encre', 'xl')
fr(ax, 74, 40, r'$\sqrt{15}$', r'$5$', 'resultat')
arrow(ax, (50, 28), (70, 28), 'resultat', curve=0.0) if False else None
box(ax, 2, 9, 40, 9, 'varie', label=r'bas : $\sqrt{5}\times\sqrt{5}=5$', size='s')
box(ax, 46, 9, 40, 9, 'sujet', label=r'haut : $\sqrt{3}\times\sqrt{5}=\sqrt{15}$', size='s')
arrow(ax, (44, 34), (22, 19), 'varie')
arrow(ax, (44, 34), (66, 19), 'sujet')
save(fig, '22-085')
