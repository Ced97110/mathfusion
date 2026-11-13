import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 38, 54, 'dans R', 'sujet', 's'); text(ax, 70, 54, r'dans $R/P$', 'autre', 's')
for y, role, lab, a, b in ((32, 'resultat', r'$P=(6)$', r'$1\notin P$', r'$\bar1\neq\bar0$'),
                           (10, 'limite', r'$P=\mathbb{Z}$', r'$1\in P$', r'$\bar1=\bar0$')):
    box(ax, 3, y, 20, 12, role, label=lab, size='s'); box(ax, 27, y, 22, 12, role, label=a)
    arrow(ax, (49.5, y + 6), (56.5, y + 6), 'varie'); box(ax, 57, y, 26, 12, role, label=b)
save(fig, '52-125')
