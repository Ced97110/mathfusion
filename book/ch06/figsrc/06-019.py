import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(70)
text(ax, 44, 64, 'numérateur', 'sujet', 'l')
text(ax, 14, 52, '3', 'sujet', 'xl'); line(ax, [(9, 47), (19, 47)], 'encre'); text(ax, 14, 42, '4', 'fixe', 'xl')
text(ax, 27, 47, '=', 'encre', 'l')
text(ax, 40, 47, '3', 'sujet', 'xl'); text(ax, 47, 47, '/', 'encre', 'xl'); text(ax, 54, 47, '4', 'fixe', 'xl')
arrow(ax, (38, 61), (15, 56), 'sujet'); arrow(ax, (44, 61), (40, 51), 'sujet')
bar(ax, 12, 14, 64, 10, ['sujet'] * 3 + ['fixe'])
brace(ax, 12, 60, 12, 'sujet', '3 parts prises')
brace(ax, 12, 76, 26, 'fixe', '4 parts égales', down=False)
save(fig, '06-019')
