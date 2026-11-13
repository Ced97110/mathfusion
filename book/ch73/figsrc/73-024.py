import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(42)
xs = [10 + 17 * k for k in range(5)]; cy = 18
for k, x in enumerate(xs):
    disc(ax, x, cy, 5, 'limite' if k == 0 else 'sujet', label=str(k), size='l')
brace(ax, xs[0] - 6, xs[4] + 6, cy + 6, 'fixe', 'F : addition, un groupe', down=False)
brace(ax, xs[1] - 6, xs[4] + 6, cy + 17, 'sujet', r'$F^*$ : sans 0, groupe pour $\times$', down=False)
text(ax, xs[0], cy - 9, 'pas d’inverse', 'limite', 's')
text(ax, xs[1], cy - 9, '1 : neutre', 'resultat', 's')
arrow(ax, (xs[2] + 5.5, cy - 4), (xs[3] - 5.5, cy - 4), 'resultat', both=True)
text(ax, (xs[2] + xs[3]) / 2, cy - 9, r'$2\times3=1$', 'resultat', 's')
text(ax, xs[4], cy - 9, r'$4\times4=1$', 'resultat', 's')
save(fig, '73-024')
