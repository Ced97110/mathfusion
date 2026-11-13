import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$c>0$ : $p$ et $q$ même signe', 'sujet', 's')
rows = [(44, r'$3\times4=12$', 'resultat', (3, 4)), (28, r'$-3\times-4=12$', 'resultat', (-3, -4)), (12, r'$3\times-4=-12$', 'limite', (3, -4))]
for y, lab, r, pts in rows:
    text(ax, 3, y, lab, r, 's', ha='left')
    f = numberline(ax, 38, 84, y, -5, 5, labels=False, arrow_right=False)
    for v in pts:
        disc(ax, f(v), y, 1.4, r); text(ax, f(v), y + 4, r'$%d$' % v, r, 's')
text(ax, f(0), 5.5, r'$0$', 'fixe', 's')
save(fig, '18-071')
