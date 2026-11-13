import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, k = 4, 40
X = lambda v: ox + v * k
text(ax, 4, 63, r'$1+\tan^2\theta$ = 1 + 0,4903 = 1,4903', 'sujet', 's', ha='left')
box(ax, X(0), 54, 1.0 * k, 5, 'sujet', r=0.5); box(ax, X(1.0), 54, 0.4903 * k, 5, 'varie', r=0.5)
text(ax, 4, 46, r'$\sec^2\theta$ = 1,4904', 'resultat', 's', ha='left')
box(ax, X(0), 37, 1.4904 * k, 5, 'resultat', r=0.5)
text(ax, 4, 29, r'formule fausse : $\sec\theta$ = 1,2208', 'limite', 's', ha='left')
box(ax, X(0), 20, 1.2208 * k, 5, 'limite', r=0.5)
box(ax, X(1.2208), 20, (1.4903 - 1.2208) * k, 5, 'limite', fill=False, dash=True, r=0.5)
line(ax, [(X(1.4903), 17), (X(1.4903), 60)], 'fixe', dash=True)
text(ax, X(1.4903) + 2, 11, 'écart 0,27', 'limite', 's', ha='right')
text(ax, 4, 11, 'écart 0,0001 (arrondis)', 'resultat', 's', ha='left')
save(fig, '31-079')
