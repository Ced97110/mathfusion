import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
U, OX, OY = 8, 12, 8
P = lambda x, y: (OX + U * x, OY + U * y)
for i in range(2):
    for j in range(5):
        disc(ax, *P(i, j), 0.6, 'fixe')
arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.3)
for k in range(1, 4):
    arrow(ax, P(1, k), P(1, k + 1), 'sujet', lw=1.3)
disc(ax, *P(1, 4), 1.2, 'resultat')
text(ax, 24, 14, r'$1\times(1,1)$', 'varie', 's', ha='left')
text(ax, 23, 28, r'$3\times(0,1)$', 'sujet', 's', ha='left')
text(ax, 25, 41.5, r'$(1,4)$', 'resultat', 's', ha='left', weight='bold')
text(ax, 44, 54, r'$\eta(e_2)=(1,3)=f_1+3f_2$', 'encre', 'm')
text(ax, 44, 48, r'$\rho(1,3)=(1,1)+3(0,1)=(1,4)$', 'encre', 's')
cw, rh, cx, cy = 7.0, 7.0, 68, 28
x0, y0 = cx - cw, cy - rh
for sx, d in ((x0 - 0.8, 1), (x0 + 2 * cw + 0.8, -1)):
    line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + 2 * rh + 0.4), (sx + 1.3 * d, y0 + 2 * rh + 0.4)], 'fixe', lw=0.9)
vals = [['2', '1'], ['3', '4']]
for i in range(2):
    for j in range(2):
        text(ax, x0 + (j + 0.5) * cw, y0 + 2 * rh - (i + 0.5) * rh, vals[i][j], 'fixe' if j == 0 else 'resultat', 'm', weight='normal' if j == 0 else 'bold')
text(ax, cx, 41.5, '$CA$', 'encre', 'm')
text(ax, cx, 14, '2e colonne : $(1,4)$', 'resultat', 's')
save(fig, '58-218')
