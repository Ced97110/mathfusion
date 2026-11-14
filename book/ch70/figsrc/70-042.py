import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [['0', '3', '2'], ['0', '5', '0'], ['0', '0', '5']]
cw, ch, x0, ytop = 12, 9, 24, 55
for i, row in enumerate(rows):
    for j, s in enumerate(row):
        role = 'varie' if j == 0 else ('fixe' if s == '0' else ('sujet' if i == 0 else 'autre'))
        box(ax, x0 + j * cw + 0.4, ytop - (i + 1) * ch + 0.4, cw - 0.8, ch - 0.8, role, label=s, size='m', r=0.4)
line(ax, [(x0 - 1, ytop - 3 * ch), (x0 - 1, ytop)], 'fixe', lw=1.3)
line(ax, [(x0 + 3 * cw + 1, ytop - 3 * ch), (x0 + 3 * cw + 1, ytop)], 'fixe', lw=1.3)
text(ax, x0 + cw / 2, ytop + 5, 'colonne de zéros', 'varie', 's')
text(ax, 11, ytop - ch / 2, r'$a_n=0$', 'varie', 's')
text(ax, 11, ytop - 1.5 * ch, r'$b_m=0$', 'varie', 's')
arrow(ax, (x0 + 3 * cw + 3, ytop - 1.5 * ch), (66, ytop - 1.5 * ch), 'fixe')
box(ax, 67, ytop - 1.5 * ch - 4.5, 19, 9, 'resultat', label=r'$Res=0$', size='s')
save(fig, '70-042')
