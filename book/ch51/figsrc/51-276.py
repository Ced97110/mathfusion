import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, '$\\mathbb{Z}$ : on ne divise pas toujours', 'sujet', 'm')
f = numberline(ax, 12, 64, 38, 0, 2, 1, arrow_right=True, role='fixe', size='m')
for v in (0, 1, 2):
    disc(ax, f(v), 38, 1.8, 'sujet')
ax.add_patch(Circle((f(0.5), 38), 2.0, ec=COL['resultat'], fc=FILL['resultat'], lw=1.0, zorder=3))
text(ax, f(0.5), 50, '$\\frac{1}{2}$', 'resultat', 'l')
arrow(ax, (f(0.5), 46.5), (f(0.5), 41), 'resultat')
text(ax, 44, 22, '$1 \\div 2$ : hors de $\\mathbb{Z}$', 'limite', 'm')
box(ax, 6, 3, 76, 12, 'resultat', label='anneau intègre → corps de fractions', size='s')
save(fig, '51-276')
