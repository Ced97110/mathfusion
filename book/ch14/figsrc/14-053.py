import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 2, 72, r'$a^2/a^5$ : on annule les facteurs', 'sujet', 'm', ha='left')
xs = [8 + 12 * k for k in range(5)]
for k, x in enumerate(xs):
    role = 'fixe' if k < 2 else 'sujet'
    if k < 2:
        disc(ax, x, 60, 4, 'fixe', label='a')
        line(ax, [(x, 56), (x, 50)], 'fixe', dash=True)
    disc(ax, x, 46, 4, role, label='a')
line(ax, [(2, 53), (66, 53)], 'encre', lw=1.0)
text(ax, 78, 60, 'haut : 2', 'fixe', 's')
text(ax, 78, 46, 'bas : 5', 'sujet', 's')
text(ax, 78, 53, 'barre', 'encre', 's')
arrow(ax, (44, 40), (44, 32), 'varie')
text(ax, 48, 36, 'il reste 3 « a » en bas', 'varie', 's', ha='left')
box(ax, 4, 8, 34, 20, 'resultat', label=r'$\frac{1}{a^3}$', size='l')
box(ax, 50, 8, 34, 20, 'varie', label=r'$a^{2-5}=a^{-3}$', size='m')
text(ax, 44, 18, '=', 'encre', 'l')
save(fig, '14-053')
