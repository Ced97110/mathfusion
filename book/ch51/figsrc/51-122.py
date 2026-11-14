import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'quaternions $\mathbb{H}$ : l’ordre compte', 'encre', 'm')
def row(y, a, b, ra, rb, res, rr):
    box(ax, 6, y, 14, 12, ra, label=a, size='l', weight='bold'); text(ax, 26, y + 6, r'$\times$', 'encre', 'l')
    box(ax, 32, y, 14, 12, rb, label=b, size='l', weight='bold'); text(ax, 52, y + 6, '=', 'encre', 'l')
    box(ax, 58, y, 22, 12, rr, label=res, size='l', weight='bold')
row(28, r'$i$', r'$j$', 'sujet', 'autre', r'$k$', 'resultat')
row(6, r'$j$', r'$i$', 'autre', 'sujet', r'$-k$', 'varie')
text(ax, 83, 24, r'$\neq$', 'limite', 'l', weight='bold', ha='right')
save(fig, '51-122')
