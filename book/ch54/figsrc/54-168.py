import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$\varphi_{\alpha}$ : $\alpha$ est la valeur de $x$', 'varie', 'm')
box(ax, 3, 28, 24, 12, 'sujet', label=r'$p=x^2-4$')
vals = [(1, '-3'), (2, '0'), (3, '5')]
ys = [54, 34, 14]
for (a, v), y in zip(vals, ys):
    arrow(ax, (27, 34), (62, y + 4), 'varie')
    text(ax, 50, 34 + (23 / 35) * (y + 4 - 34) + (4.5 if y >= 34 else -4.5), rf'$\varphi_{{{a}}}$', 'varie', 'm')
    box(ax, 64, y - 1, 20, 10, 'resultat', label=rf'${v}$', size='m')
text(ax, 12, 20, 'même polynôme', 'sujet', 's')
text(ax, 12, 12, 'indice différent', 'varie', 's')
save(fig, '54-168')
