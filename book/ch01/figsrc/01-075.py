import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
NB = ' '
fig, ax = canvas(78)
cx = [12, 33.3, 54.7, 76]
digits = ['6', '5', '0', '7']
terms = ['6 × 1' + NB + '000', '5 × 100', '0 × 10', '7 × 1']
vals = ['6' + NB + '000', '500', '0', '7']
for x, d, t, v in zip(cx, digits, terms, vals):
    box(ax, x - 6, 62, 12, 12, 'sujet', label=d, size='l', weight='bold')
    arrow(ax, (x, 61), (x, 51), 'varie')
    box(ax, x - 9, 40, 18, 10, 'varie', label=t, size='m')
    text(ax, x, 31, v, 'resultat', 'm', weight='bold')
box(ax, 49.7, 27, 10, 8, 'resultat', fill=False)
for px in (22.6, 44, 65.4):
    line(ax, [(px - 1, 45), (px + 1, 45)], 'varie', lw=1.0)
    line(ax, [(px, 44), (px, 46)], 'varie', lw=1.0)
brace(ax, 3, 85, 24, 'resultat')
text(ax, 44, 13, '6' + NB + '000 + 500 + 0 + 7 = 6' + NB + '507', 'resultat', 'm', weight='bold')
save(fig, '01-075')
