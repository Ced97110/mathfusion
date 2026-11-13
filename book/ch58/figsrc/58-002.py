import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
# deux ventes : (2, 1) et (1, 2) : mêmes nombres, ordre différent
def sale(cx, a, b):
    # a disques de riz au-dessus de la case 1, b disques de lentilles au-dessus de la case 2
    for k in range(a):
        disc(ax, cx - 6.5 + (k - (a - 1) / 2) * 4.2, 38, 1.7, 'sujet')
    for k in range(b):
        disc(ax, cx + 6.5 + (k - (b - 1) / 2) * 4.2, 38, 1.7, 'autre')
    box(ax, cx - 11.5, 22, 10, 9, 'sujet', label=str(a), size='l', weight='bold')
    box(ax, cx + 1.5, 22, 10, 9, 'autre', label=str(b), size='l', weight='bold')
    text(ax, cx - 6.5, 17.5, 'riz', 'sujet', 's')
    text(ax, cx + 6.5, 17.5, 'lentilles', 'autre', 's')
sale(22, 2, 1)
sale(66, 1, 2)
text(ax, 44, 26.5, '≠', 'encre', 'xl')
text(ax, 22, 8, 'vente (2, 1)', 'encre', 'm')
text(ax, 66, 8, 'vente (1, 2)', 'encre', 'm')
save(fig, '58-002')
