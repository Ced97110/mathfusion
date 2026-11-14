import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def chain(ax, items, acts, x, w, h, gap, top, axx):
    n = len(items)
    for i, (lab, role) in enumerate(items):
        y = top - h - i * (h + gap)
        box(ax, x, y, w, h, role, label=lab)
        if i < n - 1:
            arrow(ax, (axx, y), (axx, y - gap), "varie")
            text(ax, axx + 3, y - gap / 2, acts[i], "varie", "s", ha="left")

fig, ax = canvas(80)
items = [(r'$u^2+u+1=0$', 'sujet'), (r'$u^2=-u-1$', 'sujet'), (r'$u^2=u+1$', 'resultat')]
chain(ax, items, ['passer $u$ et 1', r'$-1=1$ dans $F$'], 14, 60, 11, 12, 76, 44)
box(ax, 14, 4, 60, 10, 'fixe', label=r'$F=\{0,1\}$ : $1+1=0$', size='s')
save(fig, '61-234')
