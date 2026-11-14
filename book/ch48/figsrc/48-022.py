import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 74, 'entiers, produit', 'sujet', 's'); text(ax, 22, 69, 'neutre 1', 'sujet', 's')
disc(ax, 22, 56, 5, 'sujet', label='1')
xs = [10 + i * 13.6 for i in range(6)]
for i, x in enumerate(xs):
    role = 'resultat' if i == 1 else ('limite' if i == 3 else 'autre')
    disc(ax, x, 22, 5, role, label=str(i))
text(ax, xs[1], 11, "neutre 1′", 'resultat', 's')
text(ax, 44, 3.5, 'cadran à six positions', 'autre', 's')
arrow(ax, (27, 54), (xs[3] - 2, 27.5), 'limite'); text(ax, 56, 50, r'$f(1)=3$', 'limite', 's')
arrow(ax, (18, 51.5), (xs[1] + 0.5, 27.5), 'resultat'); text(ax, 6, 42, r"exigé : $1'$", 'resultat', 's', ha='left')
save(fig, '48-022')
