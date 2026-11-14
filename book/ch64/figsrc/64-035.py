import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [4, 24, 44, 64]; w = 15; y = 26; h = 13
labs = [r'$D_4$ : 8', r'$V$ : 4', r'$W$ : 2', r'$\{e\}$ : 1']
for i, (x, l) in enumerate(zip(xs, labs)):
    box(ax, x, y, w, h, 'sujet' if i == 0 else 'fixe', label=l, size='m')
for i in range(3):
    text(ax, (xs[i] + w + xs[i + 1]) / 2, y + h / 2, r'$\supset$', 'encre', 'm')
brace(ax, xs[0], xs[2] + w, y + h + 4, 'limite', label=r'$W$ normal dans $D_4$ : non', down=False)
brace(ax, xs[0], xs[3] + w, y - 2, 'resultat', label='sous-normale : oui', down=True)
text(ax, xs[2] + w / 2, 8, r'$W=\{e,(12)(34)\}$', 'fixe', 's')
save(fig, '64-035')
