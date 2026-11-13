import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 44, 82, r'$x^3-3$ : le schéma de $x^3-2$', 'encre', 'm')
cx, cy, u = 24, 50, 12.5
rad = 3 ** (1 / 3) * u
arrow(ax, (3, cy), (47, cy), 'fixe', lw=0.9)
arrow(ax, (cx, 26), (cx, 74), 'fixe', lw=0.9)
ax.add_patch(Circle((cx, cy), rad, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
for k, (role, lab, dy) in enumerate([('sujet', r'$\sqrt[3]{3}$', 5.5), ('autre', r'$j\sqrt[3]{3}$', 5.5), ('autre', r'$j^2\sqrt[3]{3}$', -5.5)]):
    a = math.radians(120 * k)
    px, py = cx + rad * math.cos(a), cy + rad * math.sin(a)
    disc(ax, px, py, 2.2, role)
    text(ax, px, py + dy, lab, role, 'm')
text(ax, 36, cy - 4.5, '≈ 1,44', 'sujet', 's')
box(ax, 54, 58, 32, 12, 'resultat', label=r'$\mathbb{Q}(\sqrt[3]{3},\,j)$', size='s')
box(ax, 54, 38, 32, 12, 'sujet', label=r'$\mathbb{Q}(\sqrt[3]{3})$', size='s')
box(ax, 54, 18, 32, 12, 'fixe', label='ℚ', size='s')
arrow(ax, (70, 50), (70, 58), 'varie', lw=1.4)
arrow(ax, (70, 30), (70, 38), 'varie', lw=1.4)
text(ax, 73, 54, '×2', 'varie', 'm', ha='left')
text(ax, 73, 34, '×3', 'varie', 'm', ha='left')
box(ax, 20, 2, 48, 11, 'resultat', label=r'$3\times2=6$', size='l')
save(fig, '62-150')
