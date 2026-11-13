import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def row(yc, a, b, other, rl, rb, subs, cap, sr):
    box(ax, 3, yc - 5, 30, 10, 'fixe', fill=False)
    text(ax, 14.5, yc, a, 'sujet', 'l', ha='right'); text(ax, 14.7, yc, b, rl, 'l', ha='left', weight='bold')
    text(ax, 25, yc, other, 'sujet', 'm')
    for k, s in enumerate(subs):
        yy = yc + 6 - 12 * k
        box(ax, 40, yy - 4, 44, 8, sr, label=s, size='s')
        arrow(ax, (33, yc), (40, yy), sr)
    text(ax, 18, yc - 9, cap, rl, 's')
row(60, '2', '5', r'$\times 23$', 'resultat', None, (r'$25 \times 20 = 500$', r'$25 \times 3 = 75$'), 'dernier chiffre : 5', 'resultat')
row(26, '3', '8', r'$\times 47$', 'fixe', None, (r'$38 \times 40 = 1\,520$', r'$38 \times 7 = 266$'), 'ni 0 ni 5 : plus lourd', 'fixe')
save(fig, '10-061')
