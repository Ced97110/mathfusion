import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for x, s, role in [(34, r'$n$', 'sujet'), (41, r'$=$', 'encre'), (48, r'$d$', 'autre'), (55, r'$\times$', 'encre'), (62, r'$q$', 'varie')]:
    text(ax, x, 51, s, role, 'xl')
sp, r = 8.0, 3.0
x0, y0 = 12.0, 12.0
for i in range(3):
    for j in range(4):
        disc(ax, x0 + j*sp, y0 + i*sp, r, 'sujet')
xa, xb = x0 - 4, x0 + 3*sp + 4
brace(ax, xa, xb, y0 + 2*sp + 4.5, 'sujet', r'$n$ = 12 jetons en tout', down=False)
box(ax, xa + 0.5, y0 - 3.8, xb - xa - 1, 7.6, 'varie', fill=False, lw=0.9)
text(ax, (xa + xb)/2, 4.5, r'$q$ = 4 jetons par rangée', 'varie', 's')
xv = xb + 2
line(ax, [(xv, y0 - 3.8), (xv + 1.4, y0 - 3.8), (xv + 1.4, y0 + 2*sp + 3.8), (xv, y0 + 2*sp + 3.8)], 'autre')
text(ax, xv + 3.5, y0 + sp + 2, r'$d$ = 3', 'autre', 's', ha='left')
text(ax, xv + 3.5, y0 + sp - 2, 'rangées', 'autre', 's', ha='left')
text(ax, 71, 4.5, r'$3 \times 4 = 12$', 'resultat', 'm')
save(fig, '05-049')
