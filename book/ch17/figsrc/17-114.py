import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$x > x + 1$ : essais', 'sujet', 'l')
rows = [(44, '$x=-10$', '−10', '−9', '−10 > −9 : faux'), (30, '$x=0$', '0', '1', '0 > 1 : faux'), (16, '$x=100$', '100', '101', '100 > 101 : faux')]
for y, lab, a, b, v in rows:
    text(ax, 2, y, lab, 'encre', 's', ha='left')
    line(ax, [(20, y), (50, y)], 'fixe')
    disc(ax, 28, y, 1.3, 'varie'); disc(ax, 40, y, 1.3, 'sujet')
    text(ax, 28, y + 4, a, 'varie', 's'); text(ax, 40, y + 4, b, 'sujet', 's')
    text(ax, 86, y, v, 'limite', 's', ha='right')
text(ax, 44, 5, 'aucune solution', 'limite', 'm', weight='bold')
save(fig, '17-114')
