import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, 'coefficients : des fractions', 'fixe', 'm')
for i, c in enumerate(['1', '0', r'$-2$']):
    box(ax, 22 + i * 16, 42, 12, 10, 'sujet', label=c)
text(ax, 10, 47, r'$x^2-2$', 'sujet', 'm')
steps = [(r'$x\to\sqrt{2}$', 'varie'), (r'$(\sqrt{2})^2-2$', 'varie'), (r'$2-2$', 'varie'), ('0', 'resultat')]
ws = [20, 26, 16, 10]; x = 3
for k, ((lab, r), w_) in enumerate(zip(steps, ws)):
    box(ax, x, 14, w_, 10, r, label=lab, size='s' if k < 3 else 'l')
    if k < 3: arrow(ax, (x + w_ + 0.3, 19), (x + w_ + 3.2, 19), 'varie')
    x += w_ + 3.5
text(ax, 44, 6, 'un polynôme nul en $\\sqrt{2}$ suffit', 'resultat', 's')
save(fig, '61-051')
