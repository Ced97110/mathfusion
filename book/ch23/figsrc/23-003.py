import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# row 1: one term with x
y = 56
box(ax, 2, y, 13, 9, 'varie', True, label=r'$4x$')
box(ax, 16, y, 13, 9, 'fixe', True, label=r'$+7$')
box(ax, 30, y, 13, 9, 'fixe', True, label=r'$=30$')
arrow(ax, (45, y + 4.5), (58, y + 4.5), 'resultat')
text(ax, 51.5, y + 8, r'$-7$, $\div4$', 'resultat', 's')
box(ax, 60, y, 26, 9, 'resultat', True, label=r'$x=5{,}75$')
brace(ax, 2, 15, y, 'varie', label='1 terme en x')
# row 2: two terms with x
y = 28
box(ax, 2, y, 13, 9, 'sujet', True, label=r'$x^2$')
box(ax, 16, y, 13, 9, 'varie', True, label=r'$4x$')
box(ax, 30, y, 13, 9, 'fixe', True, label=r'$=30$')
arrow(ax, (45, y + 4.5), (58, y + 4.5), 'limite')
text(ax, 51.5, y + 8, r'$-$ ou $\div$', 'limite', 's')
box(ax, 60, y, 26, 9, 'limite', True, label='impossible')
brace(ax, 2, 29, y + 9, 'varie', label='2 termes en x', down=False)
text(ax, 44, 12, r'$x=2$ : 4 et 8 ; $x=3$ : 9 et 12', 'encre', 's')
save(fig, '23-003')
