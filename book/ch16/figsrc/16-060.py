import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
rows = ((52, 'addition : on peut défaire', r'$x+3$', r'$+\,3$', r'$-\,3$ : on retrouve $x$', 'resultat', 'resultat'),
        (14, r'multiplication par 0 : non', r'$0\times x$', r'$\times$ 0', r'$\div$ 0 : impossible', 'limite', 'limite'))
for y, head, res, fw, bw, rr, rb in rows:
    text(ax, 2, y + 18, head, 'fixe', 's', ha='left', weight='bold')
    box(ax, 4, y, 22, 12, 'sujet', label=r'$x$'); box(ax, 62, y, 22, 12, rr, label=res)
    arrow(ax, (27, y + 9), (61, y + 9), 'varie'); text(ax, 44, y + 12.5, fw, 'varie', 's')
    arrow(ax, (61, y + 3), (27, y + 3), rb); text(ax, 44, y - 1.5, bw, rb, 's')
save(fig, '16-060')
