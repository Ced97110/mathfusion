import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, r'groupe $G$ à 12 éléments', 'encre', 's')
def block(yh, head, role, rows):
    text(ax, 4, yh, head, role, 'm', ha='left')
    for i, (lab, n) in enumerate(rows):
        y = yh - 8 - 8 * i
        text(ax, 4, y, lab, role, 's', ha='left')
        box(ax, 34, y - 3.5, 5 * (n - 1) + 6, 7, role, fill=False, lw=0.7)
        for j in range(n):
            disc(ax, 37 + 5 * j, y, 2.0, role)
        last = i == len(rows) - 1
        text(ax, 59, y, r'existe, $k=m$' if last else 'existe', 'resultat', 's', ha='left')
block(63, r'$p=2$, $m=2$', 'sujet', [(r'$k=0$ : $2^0=1$', 1), (r'$k=1$ : $2^1=2$', 2), (r'$k=2$ : $2^2=4$', 4)])
block(31, r'$p=3$, $m=1$', 'autre', [(r'$k=0$ : $3^0=1$', 1), (r'$k=1$ : $3^1=3$', 3)])
save(fig, '50-040')
