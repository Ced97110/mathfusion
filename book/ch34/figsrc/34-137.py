import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
x0, w = 14, 20
for i in range(3):
    box(ax, x0 + i * w, 52, w, 11, 'sujet' if i < 2 else 'varie', label=r'$\theta$', size='m')
brace(ax, x0 + 1, x0 + 3 * w - 1, 64, 'fixe', r'$3\theta$', down=False)
brace(ax, x0 + 1, x0 + 2 * w - 1, 51, 'sujet', r'$2\theta$', down=True)
text(ax, 44, 36, r'$\cos 3\theta=\cos 2\theta\,\cos\theta-\sin 2\theta\,\sin\theta$', 'sujet', 's')
box(ax, 4, 28, 80, 15, 'sujet', fill=False, lw=0.8)
arrow(ax, (44, 27.5), (44, 20.5), 'varie')
text(ax, 46, 24, 'angles doubles', 'varie', 's', ha='left')
box(ax, 14, 8, 60, 12, 'resultat', label=r'$\cos 2\theta,\ \sin 2\theta\ \to\ \theta\ \mathrm{seul}$', size='s')
text(ax, 44, 3, r'$\theta=30^\circ$ : 90° = 60° + 30°', 'encre', 's')
save(fig, '34-137')
