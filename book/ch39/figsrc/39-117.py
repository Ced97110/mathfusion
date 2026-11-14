import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(92)
box(ax, 4, 78, 38, 10, 'sujet', label=r'$z=-1+\sqrt{3}\,i$', size='m')
arrow(ax, (42, 83), (50, 83), 'varie', lw=1.0)
text(ax, 67, 83, r'$z^2=-2-2\sqrt{3}\,i$', 'varie', 'm')
text(ax, 44, 70, r'$z^3=z^2\times z$ : quatre termes', 'encre', 's')
terms = [('2', 'sujet', ''), (r'$-2\sqrt{3}\,i$', 'varie', ''), (r'$+2\sqrt{3}\,i$', 'varie', ''), ('+6', 'sujet', r'$-6i^2=6$')]
x0, w, g = 4, 18, 3
for k, (lab, role, sub) in enumerate(terms):
    x = x0 + k * (w + g)
    box(ax, x, 48, w, 12, role, label=lab, size='s')
    if sub:
        text(ax, x + w / 2, 43, sub, 'sujet', 's')
# les deux termes en i s'annulent
xa = x0 + 1 * (w + g) + w / 2
xb = x0 + 2 * (w + g) + w / 2
arrow(ax, (xa + 2, 61.5), (xb - 2, 61.5), 'varie', lw=1.0, curve=-0.6, both=True)
brace(ax, x0 + 1 * (w + g), x0 + 2 * (w + g) + w, 46, 'varie', label='s’annulent : 0', down=True, size='s')
arrow(ax, (x0 + 11, 36), (x0 + 11, 25), 'resultat', lw=1.0)
arrow(ax, (x0 + 3 * (w + g) + w / 2, 36), (x0 + 3 * (w + g) + w / 2 - 20, 25), 'resultat', lw=1.0)
box(ax, 20, 8, 48, 16, 'resultat', label=r'$2+0+6=8$' + '\n' + r'$z^3=8$', size='m')
save(fig, '39-117')
