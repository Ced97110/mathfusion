import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cw = 11; ch = 8; x0 = 14; ytop = 36
text(ax, 44, 54, r'multiplier par $u$ : $f=\lambda^3-2$', 'encre', 'm')
heads = [r'$1\to u$', r'$u\to u^2$', r'$u^2\to2$']
vals = [['0', '0', '2'], ['1', '0', '0'], ['0', '1', '0']]
for j in range(3):
    text(ax, x0 + (j + 0.5) * cw, ytop + 5, heads[j], 'varie' if j < 2 else 'resultat', 's')
for i in range(3):
    for j in range(3):
        role = 'resultat' if j == 2 and i == 0 else ('varie' if vals[i][j] == '1' else 'fixe')
        box(ax, x0 + j * cw, ytop - (i + 1) * ch + 0.0, cw, ch, role, label=vals[i][j], size='m', r=0.4, lw=0.5)
text(ax, x0 + 1.5 * cw, ytop - 3 * ch - 4, 'des 1 sous la diagonale', 'varie', 's')
text(ax, x0 + 1.5 * cw, ytop - 3 * ch - 9, 'dernière colonne : coefficients de $f$', 'resultat', 's')
save(fig, '77-091')
