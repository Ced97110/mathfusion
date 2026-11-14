import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=3.5))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(54)
y = 28
f = numberline(ax, 8, 80, y, -4, 4, labels=False, arrow_right=False)
for v, role, lab in [(3, 'sujet', '3'), (2, 'autre', '2'), (-2, 'autre', '−2'), (-3, 'sujet', '−3')]:
    disc(ax, f(v), y, 2.6, role, label=lab, size='s')
arrow(ax, (f(3), y + 3), (f(-3), y + 3), 'varie', curve=0.35)
arrow(ax, (f(2), y + 3), (f(-2), y + 3), 'varie', curve=0.35)
text(ax, f(0), 46, 'les opposés échangent l’ordre', 'varie', 'm')
text(ax, f(0), 22.5, '0', 'fixe', 's')
brace(ax, f(-3), f(-2), 23, 'resultat', label='(−2) − (−3) = 1 ∈ P')
text(ax, (f(-3) + f(-2)) / 2, 11, '−3 < −2', 'resultat', 'm')
text(ax, (f(2) + f(3)) / 2, 11, '3 > 2', 'sujet', 'm')
save(fig, '69-029')
