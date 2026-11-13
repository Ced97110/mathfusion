import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

fig, ax = canvas(108)
box(ax, 24, 96, 40, 10, 'sujet', label=r'$(1+i)^{10}$', size='m')
# voie polaire (gauche)
text(ax, 22, 90, 'voie polaire', 'varie', 's')
box(ax, 2, 74, 40, 12, 'varie', label=r'$1+i=\sqrt{2}\ \mathrm{cis}\,45°$', size='s')
box(ax, 2, 52, 40, 16, 'varie', label=r'module : $(\sqrt{2})^{10}=32$' + '\n' + r'car $(\sqrt{2})^2=2$', size='s')
box(ax, 2, 30, 40, 16, 'varie', label=r'angle : $10\times 45°=450°$' + '\n' + '450° = 1 tour + 90°', size='s')
box(ax, 2, 12, 40, 12, 'varie', label=r'$32\ \mathrm{cis}\,90°$', size='s')
# voie de contrôle (droite)
text(ax, 66, 90, 'voie de contrôle', 'autre', 's')
box(ax, 46, 74, 40, 12, 'autre', label=r'$(1+i)^2=2i$', size='s')
box(ax, 46, 52, 40, 16, 'autre', label=r'$(2i)^5=32\,i^5$' + '\n' + r'$i^4=1$, donc $i^5=i$', size='s')
arrow(ax, (38, 96), (22, 87.5), 'varie', lw=1.0)
arrow(ax, (50, 96), (66, 87.5), 'autre', lw=1.0)
for x, y0, y1, role in [(22, 74, 69, 'varie'), (22, 52, 47, 'varie'), (22, 30, 25, 'varie'), (66, 74, 69, 'autre')]:
    arrow(ax, (x, y0), (x, y1), role, lw=1.0)
box(ax, 24, 0, 40, 9, 'resultat', label=r'$(1+i)^{10}=32\,i$', size='m')
arrow(ax, (22, 12), (30, 10), 'varie', lw=1.0)
arrow(ax, (66, 52), (58, 10), 'autre', lw=1.0)
save(fig, '39-113')
