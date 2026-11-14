import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, '0 : le seul nombre sans signe', 'sujet', 'm')
disc(ax, 44, 36, 9, 'sujet', label='0', size='xl')
cells = [(2, 48, 'opposé\n−0 = 0', 'resultat'), (48, 48, 'distance\n|0| = 0', 'resultat'),
         (2, 10, 'produit\n0 × a = 0', 'resultat'), (48, 10, 'division\na ÷ 0 : impossible', 'limite')]
for x, y, s, r in cells:
    box(ax, x, y, 38, 14, r, label=s, size='s')
    cx = x + 19; cy = y + (0 if y > 30 else 14)
    line(ax, [(44 + (cx - 44) * 0.0, 36 + (9 if y > 30 else -9)), (cx, cy)], r)
save(fig, '13-128')
