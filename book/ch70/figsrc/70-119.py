import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$f=y^2-1$, tableau à $n=2$ lignes', 'sujet', 's')
for cx, role, c, cells, det, tag in [(22, 'autre', '5', ['5', '0', '0', '5'], r'$5\times5-0\times0=25$', r'$\neq0$ : pas de racine commune'),
                                      (66, 'limite', '0', ['0', '0', '0', '0'], r'$0\times0-0\times0=0$', r'$=0$ : racines communes')]:
    text(ax, cx, 56, r'$g=%s$' % c, role, 'm')
    for k, t in enumerate(cells):
        box(ax, cx - 13 + 13 * (k % 2), 40 - 12 * (k // 2) + 0, 12, 10, role, label=t)
    text(ax, cx, 22, det, role, 's')
    text(ax, cx, 14, tag, 'resultat' if role == 'autre' else 'limite', 's')
save(fig, '70-119')
