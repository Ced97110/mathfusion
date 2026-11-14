import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(52)
y = 20
f = numberline(ax, 8, 70, y, -3, 2, arrow_right=False)
b = -1.125
ax.add_patch(Rectangle((8, y + 2), f(b) - 8, 11, ec=COL['limite'], fc=FILL['limite'], lw=0.6, zorder=1))
ax.add_patch(Rectangle((f(b), y + 2), 70 - f(b), 11, ec=COL['resultat'], fc=FILL['resultat'], lw=0.6, zorder=1))
text(ax, (8 + f(b)) / 2, y + 7.5, 'à gauche : faux', 'limite', 's')
text(ax, (f(b) + 70) / 2, y + 7.5, 'à droite : vrai', 'resultat', 's')
pt(ax, f(b), y, False, 'sujet'); pt(ax, f(-2), y, True, 'limite', 1.2); pt(ax, f(0), y, True, 'resultat', 1.2)
text(ax, f(b), y + 17, 'bord', 'sujet', 's')
text(ax, f(-2), y - 10, 'test faux', 'limite', 's'); text(ax, f(0), y - 10, 'test vrai', 'resultat', 's')
save(fig, '17-092')
