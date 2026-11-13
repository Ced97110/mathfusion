import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
bw, bh = 20, 9; xh, xk = 18, 46; y1, y2 = 46, 18
assert 3 + 2 == 5 and (9 + 8) % 12 == 5 and 3 + 6 == 9 and 2 - 6 + 12 == 8
for (y, a, b, res, lab) in [(y1, r'$h_1=3$', r'$k_1=2$', '= 5', 'départ'), (y2, r'$h_2=9$', r'$k_2=8$', r'$=17=5$', 'arrivée')]:
    box(ax, xh, y, bw, bh, 'sujet', label=a); box(ax, xk, y, bw, bh, 'autre', label=b)
    text(ax, 42, y + bh / 2, '+', 'encre'); text(ax, 77, y + bh / 2, res, 'resultat', 'm', weight='bold')
    text(ax, 2, y + bh / 2, lab, 'fixe', 's', ha='left')
arrow(ax, (xh + bw / 2, y1), (xh + bw / 2, y2 + bh), 'varie'); text(ax, xh + bw / 2 + 2.5, 36.5, r'$+6$', 'varie', 'm', ha='left')
arrow(ax, (xk + bw / 2, y1), (xk + bw / 2, y2 + bh), 'varie'); text(ax, xk + bw / 2 + 2.5, 36.5, r'$-6$', 'varie', 'm', ha='left')
text(ax, 44, 7, r'$a=6\in H\cap K$', 'varie', 'm')
save(fig, '50-194')
