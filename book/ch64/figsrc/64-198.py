import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [2 + i * 17.8 for i in range(5)]; w = 13; y = 28; h = 12
labs = [r'$S_4$' + '\n24', r'$A_4$' + '\n12', r'$V$' + '\n4', r'$W$' + '\n2', r'$\{e\}$' + '\n1']
for i, (x, l) in enumerate(zip(xs, labs)):
    box(ax, x, y, w, h, 'sujet' if i == 0 else 'fixe', label=l, size='s')
for i in range(4):
    arrow(ax, (xs[i] + w + 0.3, y + h / 2), (xs[i + 1] - 0.3, y + h / 2), 'fixe')
brace(ax, xs[0], xs[3] + w, y + h + 4, 'limite', label=r'$W$ normal dans $S_4$ : non', down=False)
brace(ax, xs[0], xs[4] + w, y - 2, 'resultat', label='sous-normale : oui', down=True)
text(ax, 44, 8, r'$\rho(12)(34)\rho^{-1}=(14)(23)\notin W$', 'limite', 's')
save(fig, '64-198')
