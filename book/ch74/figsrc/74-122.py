import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'calcul direct : M N et N M', 'encre', 's')
box(ax, 4, 44, 32, 10, 'sujet', label=r'tr$(MN)=5$', size='m')
text(ax, 44, 49, '=', 'encre', 'l')
box(ax, 52, 44, 32, 10, 'varie', label=r'tr$(NM)=5$', size='m')
text(ax, 44, 34, 'avec M = P⁻¹ et N = AP', 'encre', 's')
bw = 24; gap = (W - 4 - 3 * bw) / 2
labs = [(r'tr$(P^{-1}\,AP)$', 'sujet'), (r'tr$(AP\,P^{-1})$', 'varie'), (r'tr$(A)$', 'resultat')]
for i, (lb, r) in enumerate(labs):
    x = 2 + i * (bw + gap)
    box(ax, x, 10, bw, 10, r, label=lb, size='s')
    if i < 2:
        arrow(ax, (x + bw, 15), (x + bw + gap, 15), 'varie', lw=1.1)
text(ax, 2 + bw + gap / 2 - 0.0, 25, 'échange', 'varie', 's')
text(ax, 2 + 2 * bw + 1.5 * gap, 25, r'$PP^{-1}$ disparaît', 'resultat', 's')
save(fig, '74-122')
