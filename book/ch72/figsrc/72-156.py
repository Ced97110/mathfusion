import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$B(x,x)=0$ pour tout $x$', 'encre', 'm')
c, cy = 20, 34
arrow(ax, (c, cy), (c + 14, cy), 'sujet', lw=1.6); arrow(ax, (c, cy), (c, cy + 14), 'autre', lw=1.6)
text(ax, c + 8, cy - 4, '(1, 0)', 'sujet', 's'); text(ax, c - 3, cy + 17, '(0, 1)', 'autre', 's')
for k, (t, r) in enumerate([('(1, 0) avec lui-même : 0', 'fixe'), ('(0, 1) avec lui-même : 0', 'fixe'), ('(1, 0) avec (0, 1) : 1', 'resultat')]):
    box(ax, 40, 44 - k * 13, 46, 10, r, label=t, size='s')
save(fig, '72-156')
