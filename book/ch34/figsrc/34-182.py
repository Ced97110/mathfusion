import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(56)
R, cy = 11, 30
def panel(cx):
    P = lambda r, d: (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.5)
    return P
def arc(P, r, d0, d1, role):
    pts = [P(r, d) for d in np.linspace(d0, d1, 30)]
    line(ax, pts[:-3], role, lw=1.1); arrow(ax, pts[-4], pts[-1], role, lw=1.1)
P = panel(14)
line(ax, [(14, cy), P(R, 0)], 'fixe', lw=1.0)
line(ax, [(14, cy), P(R, 30)], 'sujet', lw=1.2); line(ax, [(14, cy), P(R, 75)], 'resultat', lw=1.2)
arc(P, 6, 0, 30, 'varie'); arc(P, 8.5, 30, 75, 'autre')
text(ax, P(R + 3.5, 30)[0], P(R + 3.5, 30)[1] - 1, '30°', 'sujet', 's')
text(ax, P(R + 3.5, 75)[0], P(R + 3.5, 75)[1], '75°', 'resultat', 's')
text(ax, 14, 11, '30° puis 45°\nfait 75°', 'encre', 's')
P = panel(43)
line(ax, [(43, cy), P(R, 0)], 'sujet', lw=1.2)
disc(ax, *P(R, 0), 1.0, 'sujet')
text(ax, 43 + R + 3.5, cy + 3, '0°', 'sujet', 's')
text(ax, 43, 11, '0° ne change\nrien', 'encre', 's')
P = panel(70)
line(ax, [(70, cy), P(R, 0)], 'fixe', lw=1.0); line(ax, [(70, cy), P(R, 30)], 'sujet', lw=1.2)
arc(P, 6, 0, 30, 'varie'); arc(P, 8.5, 30, 0, 'autre')
text(ax, P(R + 3, 30)[0], P(R + 3, 30)[1], '30°', 'sujet', 's')
text(ax, 70, 11, '+30° puis −30°\nramène au départ', 'encre', 's')
text(ax, 44, 51, r'$SO(2)$ : les rotations du plan', 'sujet', 'm')
save(fig, '34-182')
