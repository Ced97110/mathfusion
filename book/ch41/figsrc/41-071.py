import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Trois produits sous forme de barres : hauteur = produit (1,3 mm par unité).
fig, ax = canvas(64)
k = 1.3
u, v = (1, 2, 3), (4, 5, 6)
prod = [a * b for a, b in zip(u, v)]
assert prod == [4, 10, 18] and sum(prod) == 32
roles = ['sujet', 'sujet', 'varie']
names = [r'$u_1v_1$', r'$u_2v_2$', r'$u_3v_3$']
base = 22
bw = 14
xs = [8, 36, 64]
line(ax, [(2, base), (86, base)], 'fixe', lw=0.6)
for i in range(3):
    h = k * prod[i]
    box(ax, xs[i], base, bw, h, roles[i], r=0.01, lw=0.8)
    text(ax, xs[i] + bw / 2, base + h + 3, names[i], roles[i], 's')
    text(ax, xs[i] + bw / 2, base - 4, r'$%d\times %d=%d$' % (u[i], v[i], prod[i]), roles[i], 's')
for i in range(2):
    text(ax, (xs[i] + bw + xs[i + 1]) / 2, base + 5, '+', 'encre', 'l')
text(ax, xs[2] + bw / 2, base + k * 18 + 8, 'terme ajouté', 'varie', 's')
box(ax, 14, 1, 60, 9, 'resultat', label=r'$4+10+18=32$', size='m')
save(fig, '41-071')
