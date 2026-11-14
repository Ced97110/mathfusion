import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
top, bl, br = (44, 48), (22, 12), (66, 12)
import math
for a, b in [(top, bl), (top, br)]:
    d = math.hypot(b[0] - a[0], b[1] - a[1]); ux, uy = (b[0] - a[0]) / d, (b[1] - a[1]) / d
    line(ax, [(a[0] + ux * 6.5, a[1] + uy * 6.5), (b[0] - ux * 6.5, b[1] - uy * 6.5)], 'fixe')
line(ax, [(44, 41), (44, 4)], 'fixe', dash=True)
arrow(ax, (bl[0] + 6.5, 12), (br[0] - 6.5, 12), 'varie', both=True)
disc(ax, *top, 6, role='sujet', label='jr')
disc(ax, *bl, 6, role='varie', label='r')
disc(ax, *br, 6, role='varie', label='j²r')
text(ax, 44, 17.5, 'échange', 'varie', 's')
text(ax, 44, 3, 'axe de σ²τ', 'fixe', 's')
text(ax, 52, 48, 'jr ne bouge pas', 'sujet', 's', ha='left')
text(ax, 44, 59.5, 'Inv⟨σ²τ⟩ = ℚ(jr)', 'resultat', 'm', weight='bold')
save(fig, '63-151')
