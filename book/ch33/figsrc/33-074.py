import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 20, 58, 'entrée', 'fixe', 'm', weight='bold'); text(ax, 68, 58, 'sortie', 'fixe', 'm', weight='bold')
bw, bh = 34, 14
def row(y, name, role_in, lab_in, role_out, lab_out, fr):
    box(ax, 3, y, bw, bh, role_in, label=lab_in, size='s')
    box(ax, 51, y, bw, bh, role_out, label=lab_out, size='s')
    arrow(ax, (3 + bw + 1, y + bh / 2), (50, y + bh / 2), 'fixe', lw=1.2)
    text(ax, 3, y + bh + 3, name, 'encre', 's', ha='left')
ang = 'angles\nde −π/2 à π/2'.replace('π/2', r'$\pi/2$'); num = 'nombres\nde −1 à 1'
row(36, 'sinus restreint', 'sujet', ang, 'varie', num, 0)
row(8, 'arcsinus', 'varie', num, 'sujet', ang, 0)
save(fig, '33-074')
