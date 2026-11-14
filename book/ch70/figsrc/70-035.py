import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
rows = [[r'$a_2$', r'$a_1$', r'$a_0$'], [r'$b_1$', r'$b_0$', '0'], ['0', r'$b_1$', r'$b_0$']]
roles = [['sujet'] * 3, ['autre', 'autre', 'fixe'], ['fixe', 'autre', 'autre']]
names = [(r'$f$', 'sujet'), (r'$g$', 'autre'), (r'$g$ encore', 'autre')]
cw, ch, pitch, x0, ytop = 16, 10, 17, 20, 54
for j, s in enumerate([r'$y^2$', r'$y^1$', r'$y^0$']):
    text(ax, x0 + j * cw + cw / 2, ytop + 6, s, 'fixe', 'm')
for i, row in enumerate(rows):
    yb = ytop - ch - i * pitch
    text(ax, 9, yb + ch / 2, names[i][0], names[i][1], 'm', weight='bold')
    for j, s in enumerate(row):
        box(ax, x0 + j * cw + 0.4, yb + 0.4, cw - 0.8, ch - 0.8, roles[i][j], label=s, size='m', r=0.4)
g1 = ytop - ch - pitch          # bas de la ligne du milieu
g2top = ytop - ch - 2 * pitch + ch   # haut de la ligne du bas
arrow(ax, (x0 + cw / 2, g1 - 0.5), (x0 + 1.5 * cw, g2top + 0.5), 'varie', lw=1.3)
text(ax, x0 + 1.5 * cw + 3, (g1 + g2top) / 2, 'décalage d’une case', 'varie', 's', ha='left')
save(fig, '70-035')
