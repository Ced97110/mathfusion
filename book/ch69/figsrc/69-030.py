import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=3.5))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(60)
y = 38
f = numberline(ax, 6, 80, y, 0, 20, labels=False, arrow_right=False, tick=0.8)
for v, role in [(3, 'autre'), (5, 'sujet'), (12, 'autre'), (20, 'sujet')]:
    disc(ax, f(v), y, 1.9, role, label=str(v), size='s')
arrow(ax, (f(3), y + 2.2), (f(12), y + 2.2), 'varie', curve=-0.4)
arrow(ax, (f(5), y + 2.2), (f(20), y + 2.2), 'varie', curve=-0.3)
text(ax, 50, 54, '× 4', 'varie', 'm')
brace(ax, f(3), f(5), 32, 'sujet', label='5 − 3 = 2')
brace(ax, f(12), f(20), 32, 'resultat', label='8 = 2 × 4')
box(ax, 34, 6, 52, 9, 'resultat', label='règle 3 : positif × positif')
arrow(ax, (f(16), 15.5), (f(16), 24), 'resultat')
save(fig, '69-030')
