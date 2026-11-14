import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cols = [36, 54, 72]
text(ax, 12, 38, r'$x^2-1$', 'sujet', 'm', weight='bold')
text(ax, 12, 24, '0', 'autre', 'm', weight='bold')
for c, i, a, b, ok in zip(cols, range(3), ('−1', '0', '1'), ('0', '0', '0'), (False, True, False)):
    text(ax, c, 53, f'rang {i}', 'fixe', 's')
    if not ok:
        box(ax, c - 8, 5, 16, 42, 'limite', fill=False, lw=1.1, dash=True)
    box(ax, c - 6, 33.5, 12, 9, 'sujet', label=a)
    box(ax, c - 6, 19.5, 12, 9, 'autre', label=b)
    text(ax, c, 11, '=' if ok else '≠', 'resultat' if ok else 'limite', 'xl', weight='bold')
save(fig, '54-084')
