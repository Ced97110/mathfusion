import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(84)
box(ax, 24, 68, 40, 11, 'sujet', label=r'$\sqrt{8}\,\sqrt{48}$', size='l')
arrow(ax, (44, 67), (44, 60), 'varie'); text(ax, 62, 63.5, '1. simplifier', 'varie', 's')
box(ax, 14, 46, 8, 11, 'varie', label='2'); box(ax, 24, 46, 14, 11, 'sujet', label=r'$\sqrt{2}$')
text(ax, 44, 51.5, r'$\cdot$', 'encre', 'l')
box(ax, 50, 46, 8, 11, 'varie', label='4'); box(ax, 60, 46, 14, 11, 'sujet', label=r'$\sqrt{3}$')
arrow(ax, (18, 45), (28, 33), 'varie'); arrow(ax, (54, 45), (40, 33), 'varie')
arrow(ax, (31, 45), (60, 33), 'sujet') if False else None
box(ax, 14, 22, 28, 10, 'varie', label=r'$2\times4=8$', size='s')
box(ax, 46, 22, 34, 10, 'sujet', label=r'$\sqrt{2}\times\sqrt{3}=\sqrt{6}$', size='s')
arrow(ax, (67, 45), (63, 33), 'sujet')
text(ax, 28, 16, '2. les nombres devant', 'varie', 's'); text(ax, 63, 16, '3. les radicandes', 'sujet', 's')
arrow(ax, (28, 21), (40, 12), 'resultat') if False else None
box(ax, 26, 1.5, 36, 9, 'resultat', label=r'$8\sqrt{6}$ ≈ 19,6', size='m')
save(fig, '22-154')
