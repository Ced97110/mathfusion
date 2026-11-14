import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(76)
text(ax, 44, 72, r"$H$ ne contient pas $K$ : $G=S_3$", 'encre', 's', weight='bold')
line(ax, [(44, 14), (44, 66)], 'fixe', dash=True)
text(ax, 23, 62, r'dans $G$', 'sujet', 's'); text(ax, 66, 62, r'dans $G/K$', 'autre', 's')
for x, lab, role in [(10, 'e', 'sujet'), (22, r'$t_1$', 'sujet'), (34, r'$t_2$', 'fixe')]:
    disc(ax, x, 44, 4.2, role, label=lab, size='s')
ax.add_patch(FancyBboxPatch((6, 38.5), 20, 11, boxstyle='round,pad=1', ec=COL['limite'], fc='none', ls='--', lw=1.1, zorder=3))
text(ax, 9, 56, r'$H$', 'limite', 's', weight='bold')
arrow(ax, (22, 49), (34, 49), 'varie', curve=-0.7); text(ax, 30, 58, 'conjugué', 'varie', 's')
text(ax, 23, 24, r'$H$ pas normal', 'limite', 's', weight='bold')
box(ax, 48, 38, 16, 12, 'sujet', r'$K$', 's'); box(ax, 68, 38, 18, 12, 'fixe', 'autre', 's')
text(ax, 66, 24, r'$H/K=G/K$ : normal', 'resultat', 's', weight='bold')
save(fig, '48-092')
