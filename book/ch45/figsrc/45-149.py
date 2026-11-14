import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cw, ch, gx, gy, x0 = 11, 10, 4, 3, 6
ys = [26, 26 + ch + gy]
for c in range(3):
    x = x0 + c * (cw + gx)
    box(ax, x, ys[1], cw, ch, 'sujet', label=r'$a$', size='l')
    box(ax, x, ys[0], cw, ch, 'varie', label=r'$b$', size='l')
    text(ax, x + cw / 2, 56, r'$a+b$', 'encre', 's')
xr = x0 + 3 * (cw + gx) - gx + 3
text(ax, xr + 8, ys[1] + ch / 2, r'$na$', 'sujet', 'm')
text(ax, xr + 8, ys[0] + ch / 2, r'$nb$', 'varie', 'm')
text(ax, 44, 14, r'$n(a+b)=na+nb$', 'resultat', 'l')
text(ax, 44, 6, '3 colonnes ou 2 lignes : même total', 'fixe', 's')
save(fig, '45-149')
