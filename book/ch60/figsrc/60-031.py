import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# haut : ℤ, l'idéal engendré par 6
text(ax, 44, 75, 'D : +, ×, produit non nul', 'encre', 'm', weight='bold')
text(ax, 44, 67, 'D = ℤ : multiples de 6', 'sujet', 'm')
f = numberline(ax, 8, 70, 46, -18, 18, step=6)
for v in range(-18, 19, 6):
    disc(ax, f(v), 46, 1.7, 'sujet')
arrow(ax, (f(6), 49), (f(12), 49), 'varie', curve=-0.5)
text(ax, (f(6) + f(12)) / 2, 55, '× 2', 'varie', 's')
arrow(ax, (f(6) - 1, 49), (f(-18), 49), 'varie', curve=0.35)
text(ax, (f(6) + f(-18)) / 2, 58, '× (−3)', 'varie', 's')
line(ax, [(4, 33), (84, 33)], 'fixe', lw=0.5, dash=True)
# bas : F[λ], l'idéal engendré par λ − 1
text(ax, 44, 28, 'D = F[λ] : multiples de λ − 1', 'sujet', 'm')
box(ax, 4, 8, 16, 11, 'sujet', label='λ − 1', size='s')
box(ax, 26, 8, 24, 11, 'sujet', label='λ(λ − 1)', size='s')
box(ax, 56, 8, 28, 11, 'sujet', label='(λ + 2)(λ − 1)', size='s')
for xc, t in ((12, '× 1'), (38, '× λ'), (70, '× (λ + 2)')): text(ax, xc, 22.5, t, 'varie', 's')
save(fig, '60-031')
