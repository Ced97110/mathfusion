import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [12, 38, 68]
ry = [46, 20]
text(ax, cx[0], 61, r'$\bar{9}$', 'sujet', 'l')
text(ax, cx[1], 61, r'$\bar{7}$', 'autre', 'l')
text(ax, cx[2], 61, 'somme', 'resultat', 'm')
vals = [('9', '7', '16'), ('21', r'$-5$', '16')]
roles = ['sujet', 'autre', 'resultat']
for r in range(2):
    for c in range(3):
        box(ax, cx[c] - 8, ry[r] - 4.5, 16, 9, roles[c], label=vals[r][c])
    text(ax, 25, ry[r], '+', 'encre', 'm')
    arrow(ax, (cx[1] + 9, ry[r]), (cx[2] - 9, ry[r]), 'encre')
for c in range(2):
    line(ax, [(cx[c], ry[0] - 5.5), (cx[c], 38)], roles[c])
    line(ax, [(cx[c], 28), (cx[c], ry[1] + 5.5)], roles[c])
    text(ax, cx[c], 33, r'$\equiv$', roles[c], 'm')
line(ax, [(cx[2], ry[0] - 5.5), (cx[2], ry[1] + 5.5)], 'resultat')
text(ax, cx[2] + 3, 33, 'même', 'resultat', 's', ha='left')
save(fig, '43-124')
