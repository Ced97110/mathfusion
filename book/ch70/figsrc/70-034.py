import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [['1', '−5', '6'], ['1', '−2', '0'], ['0', '1', '−2']]
roles = ['sujet', 'varie', 'autre']
names = [r'$f$', r'$y\,g$', r'$g$']
cw, ch, x0, y0 = 10, 9, 14, 44
for j, s in enumerate([r'$y^2$', r'$y$', '1']):
    text(ax, x0 + j * cw + cw / 2, y0 + 3 * ch + 3, s, 'fixe', 's')
for i, row in enumerate(rows):
    text(ax, 7, y0 + (2 - i) * ch + ch / 2, names[i], roles[i], 'm', weight='bold')
    for j, s in enumerate(row):
        box(ax, x0 + j * cw + 0.4, y0 + (2 - i) * ch + 0.4, cw - 0.8, ch - 0.8, roles[i], label=s, size='m', r=0.4)
cx = x0 + 1.5 * cw
arrow(ax, (cx, y0 - 1), (cx, y0 - 8), 'fixe')
text(ax, cx, y0 - 12, r'$4-10+6=0$', 'resultat', 's')
text(ax, 69, 79, 'racine commune 2', 'resultat', 's')
arrow(ax, (69, 76), (69, 70), 'resultat')
box(ax, 50, 58, 36, 11, 'resultat', label=r'$(2^2,\,2,\,1)=(4,\,2,\,1)$', size='s')
box(ax, 50, 44, 36, 11, 'fixe', label=r'$(0,\ 0,\ 0)$', size='m')
text(ax, 68, 38, 'deux solutions', 'fixe', 's')
arrow(ax, (68, 35), (68, 29), 'fixe')
box(ax, 50, 18, 36, 10, 'resultat', label='déterminant 0', size='m')
arrow(ax, (cx + 11, y0 - 12), (49, 23), 'resultat')
save(fig, '70-034')
