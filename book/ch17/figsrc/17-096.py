import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(80)
text(ax, 44, 75, r'$-8x+5<14$', 'encre', 'm')
arrow(ax, (36, 71), (22, 61), 'sujet'); arrow(ax, (52, 71), (66, 61), 'autre')
box(ax, 4, 46, 36, 14, 'sujet', label=r'$x>-\frac{9}{8}$', size='m')
box(ax, 48, 46, 36, 14, 'autre', label=r'$-\frac{9}{8}<x$', size='m')
text(ax, 22, 41, r'$\div(-8)$, retourner', 'sujet', 's'); text(ax, 66, 41, r'$+8x$, sans retourner', 'autre', 's')
y = 16
f = numberline(ax, 8, 66, y, -3, 2, labels=False, arrow_right=False)
for v in (-2, -1, 0): text(ax, f(v), y - 4, f'{v}'.replace('-', '−'), 'fixe', 's')
seg(ax, f(-1.125), 70, y, 'resultat'); arrow(ax, (66, y), (75, y), 'resultat', lw=1.4)
pt(ax, f(-1.125), y, False, 'resultat')
arrow(ax, (22, 45), (f(-1.125) - 2, y + 4), 'sujet', curve=0.0); arrow(ax, (66, 45), (f(-1.125) + 4, y + 4), 'autre')
text(ax, 44, 30, 'même ensemble', 'resultat', 's')
save(fig, '17-096')
