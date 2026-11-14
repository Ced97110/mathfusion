import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def row(y, groups, size, roles, title):
    step = 4.6; extra = 2.5
    total = groups * size * step + (groups - 1) * extra
    x = (W - total) / 2
    for g in range(groups):
        for i in range(size):
            box(ax, x, y, 4.0, 4.0, roles[g], r=0.4, lw=0.6); x += step
        x += extra
    text(ax, W / 2, y + 8, title, 'encre', 'm')
row(52, 3, 4, ['sujet', 'varie', 'autre'], 'horloge : 12 ÷ 4 = 3 lignes')
row(33, 2, 4, ['sujet', 'varie'], 'carré : 8 ÷ 4 = 2 classes')
row(14, 2, 3, ['sujet', 'varie'], 'permutations : 6 ÷ 3 = 2 classes')
text(ax, W / 2, 4, r'$|G/N| = |G| \div |N|$', 'resultat', 'l')
save(fig, '47-146')
