import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = [34, 43, 52, 61, 70, 79]
numberline(ax, 30, 84, 30, 0, 5, arrow_right=False) if False else None
line(ax, [(30, 30), (84, 30)], 'fixe')
for i, x in enumerate(X):
    line(ax, [(x, 29), (x, 31)], 'fixe')
    text(ax, x, 26.6, str(i), 'fixe', 's')
for y, nrouge in [(36, 3), (16, 1)]:
    for i, x in enumerate(X):
        r = 'limite' if i < nrouge else 'resultat'
        ax.add_patch(Rectangle((x - 4, y), 8, 8, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))
text(ax, 16, 40, r'$2^n > n + 4$', 'encre', 's'); text(ax, 16, 20, 'autre affirmation', 'encre', 's')
arrow(ax, (61, 54), (61, 45), 'sujet'); text(ax, 61, 57.5, r'départ $n_0$ = 3', 'sujet', 'l')
arrow(ax, (43, 7), (43, 15), 'sujet'); text(ax, 52, 5, r'$n_0$ = 1', 'sujet', 'l')
save(fig, '01-136')
