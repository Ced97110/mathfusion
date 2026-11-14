import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
def mat(x0, vals, role):
    for (dx, dy), v in zip([(0, 8), (8, 8), (0, 0), (8, 0)], vals):
        box(ax, x0 + dx, 20 + dy, 8, 8, role, label=v)
mat(4, ['1', '−2', '2', '1'], 'sujet'); mat(30, ['2', '−3', '3', '2'], 'autre')
line(ax, [(22.5, 31.5), (26.5, 35.5)], 'encre'); line(ax, [(22.5, 35.5), (26.5, 31.5)], 'encre')
line(ax, [(47, 32), (51, 32)], 'encre'); line(ax, [(47, 35), (51, 35)], 'encre')
box(ax, 54, 20, 28, 16, 'resultat', label='matrice de $zw$', size='s')
text(ax, 12, 15, '$N(z)=5$', 'sujet', 's'); text(ax, 38, 15, '$N(w)=13$', 'autre', 's'); text(ax, 68, 15, '$N(zw)=65$', 'resultat', 's')
text(ax, 44, 7, 'N = déterminant', 'fixe', 's')
save(fig, '78-079')
