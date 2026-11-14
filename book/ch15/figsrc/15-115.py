import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
heads = [r'$x^2$', r'$x$', 'constante']
xs = [34, 54, 74]
for x, h in zip(xs, heads): text(ax, x, 66, h, 'encre', 's')
data = [(54, r'$x^2+4$', ['1', '0', '4'], 'sujet'),
        (38, r'$x^2+7x+2$', ['1', '7', '2'], 'autre'),
        (14, 'somme', ['1+1=2', '7', '4+2=6'], 'resultat')]
for y, lab, v, r in data:
    text(ax, 1, y + 5, lab, r, 's', ha='left')
    for x, s in zip(xs, v):
        miss = (lab == r'$x^2+4$' and s == '0')
        box(ax, x - 9, y - 1, 18, 9, 'varie' if miss else r, label=s, dash=miss)
text(ax, 44, 30, 'pas de terme en $x$ : 0', 'varie', 's')
text(ax, 44, 4, r'$2x^2+7x+6$', 'resultat', 'l', weight='bold')
save(fig, '15-115')
