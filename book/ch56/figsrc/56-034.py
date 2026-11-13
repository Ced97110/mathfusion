import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# Gauche : entiers non nuls, 2 sans inverse
text(ax, 22, 58, 'entiers non nuls', 'fixe', 'm')
box(ax, 6, 36, 14, 12, 'fixe', label='2')
arrow(ax, (20.8, 42), (28, 42), 'limite')
box(ax, 28, 36, 14, 12, 'limite', label='1/2', dash=True)
text(ax, 22, 28, 'inverse non entier', 'limite', 's')
text(ax, 22, 21, 'pas un groupe', 'limite', 'm')
# Droite : U = {1, -1}, table des produits
text(ax, 66, 58, 'U = {1, −1}', 'sujet', 'm')
cw = 11
x0, y0 = 50, 26
text(ax, x0 + cw * 1.5, y0 + cw * 2 + 3, '1', 'sujet', 'm')
text(ax, x0 + cw * 2.5, y0 + cw * 2 + 3, '−1', 'sujet', 'm')
heads = ['1', '−1']
vals = [['1', '−1'], ['−1', '1']]
for i in range(2):
    text(ax, x0 + cw * 0.5, y0 + cw * (1 - i) + cw / 2, heads[i], 'sujet', 'm')
    for j in range(2):
        box(ax, x0 + cw * (1 + j), y0 + cw * (1 - i), cw, cw, 'resultat', label=vals[i][j])
text(ax, 66, 18, 'chaque produit reste', 'resultat', 's')
text(ax, 66, 13, 'dans U', 'resultat', 's')
save(fig, '56-034')
