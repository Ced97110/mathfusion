import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, 'Triangle, $p = 3$ : valeurs de $n_p$', 'encre', 's')
X = {1: 20, 2: 40}
text(ax, 3, 66, r'1. $n_p$ divise 2 : la divisibilité seule', 'varie', 's', ha='left')
for v, x in X.items(): disc(ax, x, 58, 3.6, 'varie', label=str(v), size='m')
text(ax, 55, 58, 'reste 1 ou 2', 'varie', 's', ha='left')
box(ax, 2, 26, 84, 27, 'autre', fill=False, dash=True)
text(ax, 5, 30, r'2. idée de plus : $n_p \equiv 1$ (mod 3)', 'autre', 's', ha='left')
for v, x in X.items():
    line(ax, [(x, 54.4), (x, 47.6)], 'fixe', dash=True, lw=0.7)
    disc(ax, x, 44, 3.6, 'resultat' if v == 1 else 'limite', label=str(v), size='m')
text(ax, 50, 46.5, r'$2 - 1 = 1$ n’est pas', 'limite', 's', ha='left')
text(ax, 50, 42, 'un multiple de 3', 'limite', 's', ha='left')
box(ax, 14, 6, 60, 10, 'resultat', label=r'seul $n_p = 1$ reste', size='m')
save(fig, '50-072')
