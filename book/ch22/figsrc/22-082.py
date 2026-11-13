import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(52)
text(ax, 44, 46, 'propriété du quotient', 'varie', 's')
box(ax, 2, 22, 28, 14, 'sujet', label=r'$\sqrt{3/5}$', size='l')
arrow(ax, (32, 29), (47, 29), 'varie')
text(ax, 62, 37, r'$\sqrt{3}$', 'sujet', 'l')
line(ax, [(52, 32), (72, 32)], 'sujet', lw=1.0)
box(ax, 56, 21, 12, 8, 'varie', label=r'$\sqrt{5}$', size='l')
text(ax, 62, 13, 'un radical en bas', 'varie', 's')
text(ax, 16, 17, 'racine de 3 cinquièmes', 'sujet', 's')
save(fig, '22-082')
