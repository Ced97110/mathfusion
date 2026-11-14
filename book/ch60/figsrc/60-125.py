import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
x0, x1 = 6, 78
y = 24
f = numberline(ax, x0, x1, y, 0, 13, step=1, labels=False, arrow_right=False)
for v in (0, 9, 13):
    text(ax, f(v), y - 5, str(v), 'encre', 'm')
arrow(ax, (f(0), y + 1.5), (f(9), y + 1.5), 'varie', curve=-0.35)
text(ax, f(4.5), y + 14, '9 (ordre 4)', 'varie', 's')
arrow(ax, (f(9), y + 1.5), (f(13), y + 1.5), 'autre', curve=-0.5)
text(ax, f(11), y + 10.5, '4 (ordre 3)', 'autre', 's')
text(ax, f(12.2), y - 16.5, '13 − 12 = 1', 'resultat', 's')
arrow(ax, (f(13), y - 13), (f(13), y - 8.2), 'resultat')
text(ax, 44, 58, r'$3 \times (-1) + 4 \times 1 = 1$', 'encre', 'm')
text(ax, 44, 51, '−3 et 9 ont le même reste', 'fixe', 's')
text(ax, 22, 6, 'dans ℤ/12 :  1 = 9 + 4', 'resultat', 'm', weight='bold', ha='left')
save(fig, '60-125')
