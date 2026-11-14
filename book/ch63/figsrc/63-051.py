import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
bw, gap = 25, 5
xs = [1.5 + (bw + gap) * i for i in range(3)]
heads = ['polynôme', 'corps de\ndécomposition', 'son groupe']
labs = [r'$f=x^2-2$' + '\nsur ' + r'$\mathbb{Q}$', r'$E=\mathbb{Q}(\sqrt{2})$' + '\nracines ' + r'$\pm\sqrt{2}$', r'$\{1,\sigma\}$' + '\n2 éléments']
roles = ['sujet', 'autre', 'resultat']
for x, h, l, r in zip(xs, heads, labs, roles):
    text(ax, x + bw / 2, 51, h, r, 's')
    box(ax, x, 26, bw, 18, r, label=l, size='s')
for i in range(2):
    arrow(ax, (xs[i] + bw, 35), (xs[i + 1], 35), 'fixe')
brace(ax, 1.5, 86.5, 24, 'fixe', label=r'groupe de Galois de $f$')
save(fig, '63-051')
