import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$x^5-2$   avec  p = 2', 'sujet', 'l')
vals = ['1', '0', '0', '0', '0', '−2']
heads = [r'$x^5$', r'$x^4$', r'$x^3$', r'$x^2$', r'$x$', r'$1$']
w = 13.0
x0 = 5.0
for i, v in enumerate(vals):
    box(ax, x0 + i * w, 50, w - 1.0, 10, 'varie' if i == 0 else 'sujet', label=v, size='m')
    text(ax, x0 + i * w + (w - 1.0) / 2, 63, heads[i], 'fixe', 's')
text(ax, x0 + w / 2 - 0.5, 44.5, '2 ne divise\npas 1', 'varie', 's')
brace(ax, x0 + w, x0 + 6 * w - 1, 48, 'sujet', depth=1.8)
text(ax, x0 + 3.5 * w, 41, '2 divise tous les autres', 'sujet', 's')
text(ax, 83, 30, '4 ne divise pas −2', 'sujet', 's', ha='right')
box(ax, 8, 8, 72, 12, 'resultat', label=r'irréductible sur $\mathbb{Q}$, pour tout $n$', size='m')
save(fig, '54-225')
