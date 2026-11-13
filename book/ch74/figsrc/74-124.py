import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x0, y0, cw, ch = 6, 20, 16, 13
M = [['$a$', '$b$'], ['$c$', '$d$']]
roles = [['resultat', 'fixe'], ['fixe', 'resultat']]
for i in range(2):
    for j in range(2):
        box(ax, x0 + j * cw, y0 + (1 - i) * ch, cw, ch, roles[i][j], label=M[i][j], size='xl')
text(ax, x0 + cw / 2, y0 + 2 * ch + 7, 'image de $x$', 'sujet', 's')
text(ax, x0 + 1.5 * cw, y0 + 2 * ch + 7, 'image de $y$', 'autre', 's', ha='center')
line(ax, [(x0 + cw / 2, y0 + 2 * ch + 3), (x0 + cw / 2, y0 + 2 * ch + 0.5)], 'sujet')
line(ax, [(x0 + 1.5 * cw, y0 + 2 * ch + 3), (x0 + 1.5 * cw, y0 + 2 * ch + 0.5)], 'autre')
text(ax, x0 + cw, 12, r'$a,\ b,\ c,\ d$ : entiers', 'sujet', 's')
arrow(ax, (x0 + 2 * cw + 3, y0 + ch), (50, y0 + ch), 'varie', lw=1.1)
box(ax, 52, y0 + ch - 7, 33, 14, 'resultat', label=r'trace $a+d$ = entier', size='s')
text(ax, 68.5, y0 + ch + 12, 'somme de deux entiers', 'resultat', 's')
text(ax, 68.5, y0 + ch - 12, r'quart de tour : $0+0=0$', 'resultat', 's')
save(fig, '74-124')
