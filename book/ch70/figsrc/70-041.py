import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
box(ax, 24, 70, 40, 9, 'sujet', label=r'$Res(f,g)=0$', size='m')
arrow(ax, (38, 70), (22, 65), 'fixe')
arrow(ax, (50, 70), (66, 65), 'fixe')
text(ax, 44, 66, 'ou', 'fixe', 'm')
box(ax, 2, 47, 40, 17, 'varie', label='cas 1\n$a_n=0$ et $b_m=0$', size='s')
box(ax, 46, 47, 40, 17, 'autre', label='cas 2\nfacteur commun\nde degré $\\geq1$', size='s')
cw, ch, x0, y0 = 10, 8, 6, 24
for i, row in enumerate([[r'$x$', '−1'], [r'$x$', '−2']]):
    for j, s in enumerate(row):
        box(ax, x0 + j * cw + 0.4, y0 + (1 - i) * ch + 0.4, cw - 0.8, ch - 0.8, 'varie' if j == 0 else 'fixe', label=s, size='m', r=0.4)
arrow(ax, (x0 + 10, 47), (x0 + 10, y0 + 2 * ch + 2), 'varie')
text(ax, 37, y0 + 12, r'$\det=-x$', 'sujet', 's')
text(ax, 37, y0 + 4, r'$x=0$ : $\det=0$', 'resultat', 's')
for k, (yy, nm) in enumerate([(32, r'$f$'), (20, r'$g$')]):
    text(ax, 49, yy + 5, nm, 'sujet' if k == 0 else 'autre', 'm', weight='bold')
    box(ax, 54, yy, 20, 10, 'autre', label='facteur\ncommun', size='s')
    box(ax, 75, yy, 11, 10, 'fixe', label='reste', size='s')
arrow(ax, (66, 47), (66, 43), 'autre')
text(ax, 66, 13, 'une racine commune', 'resultat', 's')
save(fig, '70-041')
