import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$\sigma_k:\ \omega\mapsto\omega^k$', 'encre', 'xl')
text(ax, 24, 56.5, 'indice : numérote', 'fixe', 's')
text(ax, 64, 56.5, 'exposant : facteurs', 'fixe', 's')
disc(ax, 14, 28, 5, 'sujet', label=r'$\omega$')
ys = [46, 36, 26, 16]
for k, y in enumerate(ys, start=1):
    disc(ax, 72, y, 4.5, 'resultat', label=(r'$\omega$' if k == 1 else rf'$\omega^{k}$'))
    arrow(ax, (19, 28 + (y - 28) * 0.15), (66.5, y - (y - 28) * 0.0), 'varie')
    y0 = 28 + (y - 28) * 0.15
    s = (54 - 19) / 47.5
    text(ax, 54, y0 + s * (y - y0) + 2.8, rf'$\sigma_{k}$', 'varie', 's')
text(ax, 44, 5, r'$\omega^5=1$ , $\omega\neq1$', 'fixe', 's')
save(fig, '63-048')
