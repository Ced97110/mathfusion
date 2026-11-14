import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 24, 62, r'$f=y^2-3y+2$', 'sujet', 's')
text(ax, 64, 62, r'$g=y-1$', 'autre', 's')
text(ax, 24.5, 54, 'tableau de Sylvester', 'fixe', 's')
rows = [['1', '−3', '2'], ['1', '−1', '0'], ['0', '1', '−1']]
roles = ['sujet', 'autre', 'autre']
cw, ch, x0, y0 = 11, 9, 8, 24
for i, row in enumerate(rows):
    for j, s in enumerate(row):
        box(ax, x0 + j * cw + 0.4, y0 + (2 - i) * ch + 0.4, cw - 0.8, ch - 0.8, roles[i], label=s, size='m', r=0.4)
line(ax, [(x0 - 1, y0), (x0 - 1, y0 + 27)], 'fixe', lw=1.3)
line(ax, [(x0 + 34, y0), (x0 + 34, y0 + 27)], 'fixe', lw=1.3)
arrow(ax, (x0 + 37, y0 + 13.5), (58, y0 + 13.5), 'varie')
text(ax, 51, y0 + 17.5, 'déterminant', 'varie', 's')
box(ax, 59, y0 + 9, 27, 9, 'resultat', label=r'$Res_y(f,g)=0$', size='s')
save(fig, '70-039')
