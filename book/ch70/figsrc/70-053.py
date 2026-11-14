import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
rows = [['$a$', '$b$', '$c$'], ['$2a$', '$b$', '0'], ['0', '$2a$', '$b$']]
roles = [['sujet'] * 3, ['autre', 'autre', 'fixe'], ['fixe', 'autre', 'autre']]
cw, ch, x0, ytop = 17, 9, 20, 46
for i, row in enumerate(rows):
    for j, s in enumerate(row):
        box(ax, x0 + j * cw + 0.4, ytop - (i + 1) * ch + 0.4, cw - 0.8, ch - 0.8, roles[i][j], label=s, size='m', r=0.4)
text(ax, 11, ytop - 0.5 * ch, r'$f$', 'sujet', 'm')
text(ax, 11, ytop - 1.5 * ch, r'$f′$', 'autre', 'm')
text(ax, 10, ytop - 2.5 * ch, r'$f′$ décalé', 'autre', 's')
text(ax, 44, 12, r'cas : $a,b,c=1,\ -4,\ 4$', 'fixe', 's')
save(fig, '70-053')
