import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)

def bars(y, head, g_dash, sym, res, rrole, note):
    text(ax, 44, y + 20, head, rrole, 'm')
    text(ax, 3, y + 8, r'$|G|$', 'varie', 's', ha='left')
    text(ax, 3, y - 2, r'$[E:F]$', 'sujet', 's', ha='left')
    for i in range(4):
        box(ax, 20 + i * 9, y + 4, 8, 8, 'fixe' if g_dash else 'varie', fill=not g_dash, dash=g_dash)
        box(ax, 20 + i * 9, y - 6, 8, 8, 'sujet')
    text(ax, 58, y + 3, sym, rrole, 'l')
    text(ax, 73, y + 3, res, rrole, 's')
    if note:
        text(ax, 73, y - 3, note, rrole, 's')

bars(48, 'avec la séparabilité', False, '=', r"$[F':F]=1$", 'resultat', None)
bars(12, 'sans la séparabilité', True, r'$\leq$', r"$[F':F]=1$ ?", 'limite', 'non démontré')
save(fig, '63-106')
