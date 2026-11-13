import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(70)
box(ax, 2, 46, 14, 11, 'sujet', label=r'$\sqrt{3}$', size='l')
text(ax, 21, 51.5, r'$\times$', 'encre', 'l'); text(ax, 24.5, 51.5, '(', 'encre', 'l')
box(ax, 27, 46, 10, 11, 'fixe', label='7', size='l')
text(ax, 42, 51.5, '+', 'encre', 'l')
box(ax, 47, 46, 12, 11, 'autre', label=r'$\sqrt{6}$', size='l')
text(ax, 63, 51.5, ')', 'encre', 'l')
arrow(ax, (9, 58), (32, 58.5), 'varie', curve=-0.35)
arrow(ax, (12, 58), (53, 58.5), 'varie', curve=-0.35)
text(ax, 40, 66, r'chaque terme $\times\sqrt{3}$', 'varie', 's')
arrow(ax, (32, 45), (26, 31), 'resultat'); arrow(ax, (53, 45), (62, 31), 'resultat')
box(ax, 14, 20, 24, 10, 'fixe', label=r'$7\sqrt{3}$', size='m')
text(ax, 43, 25, '+', 'encre', 'l')
box(ax, 47, 20, 36, 10, 'autre', label=r'$\sqrt{18}=3\sqrt{2}$', size='m')
text(ax, 44, 9, 'des deux côtés : environ 16,37', 'fixe', 's')
save(fig, '22-095')
