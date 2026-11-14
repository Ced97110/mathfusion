import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def glyph(ax, k, cx, cy, s, role, lw=1.2):
    cyb = -.2 if k == 'b' else .2
    st = [(-.25, .5), (-.25, -.5)]
    bowl = [(.03 + .28 * math.cos(t * math.pi / 12), cyb + .28 * math.sin(t * math.pi / 12)) for t in range(25)]
    for pts in (st, bowl):
        line(ax, [(cx + x * s, cy + y * s) for x, y in pts], role, lw=lw)
xs = [26 + 10.5 * i for i in range(6)]
fig, ax = canvas(84)
def band(y, first, role):
    for i, x in enumerate(xs):
        glyph(ax, first if i % 2 == 0 else ('p' if first == 'b' else 'b'), x, y, 10, role)
band(72, 'b', 'sujet')
line(ax, [(18, 62), (84, 62)], 'resultat', lw=1.0, dash=True)
text(ax, 10, 62, r'miroir $D$', 'resultat', 's')
band(52, 'p', 'limite')
arrow(ax, (xs[1], 44), (xs[2], 44), 'varie')
text(ax, xs[2] + 4, 44, 'glisser d’une lettre', 'varie', 's', ha='left')
band(30, 'b', 'resultat')
text(ax, 2, 72, 'bande', 'sujet', 's', ha='left'); text(ax, 2, 52, 'retournée', 'limite', 's', ha='left')
text(ax, 2, 30, '+ glissée', 'resultat', 's', ha='left')
text(ax, 44, 17, 'retombe sur la bande', 'resultat', 's')
save(fig, '74-027')
