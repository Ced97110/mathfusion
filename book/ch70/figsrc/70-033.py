import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mat(x, y, cw, ch, rows, role):
    n = len(rows)
    for i, row in enumerate(rows):
        for j, s in enumerate(row):
            box(ax, x + j * cw + 0.4, y + (n - 1 - i) * ch + 0.4, cw - 0.8, ch - 0.8, role, label=s, size='m', r=0.4)
text(ax, 44, 62, 'second membre nul', 'fixe', 'm', weight='bold')
line(ax, [(44, 6), (44, 56)], 'fixe', lw=0.6, dash=True)
# gauche : déterminant non nul
mat(12, 36, 10, 9, [['1', '1'], ['1', '−1']], 'sujet')
text(ax, 22, 29, r'$1\times(-1)-1\times1=-2$', 'sujet', 's')
arrow(ax, (22, 26), (22, 20), 'fixe')
box(ax, 2, 8, 40, 11, 'resultat', label=r'seule solution : $(0,\ 0)$', size='s')
# droite : déterminant nul
mat(56, 36, 10, 9, [['1', '1'], ['2', '2']], 'autre')
text(ax, 66, 29, r'$1\times2-1\times2=0$', 'autre', 's')
arrow(ax, (66, 26), (66, 20), 'fixe')
box(ax, 46, 8, 40, 11, 'resultat', label=r'aussi la solution $(1,\ -1)$', size='s')
save(fig, '70-033')
