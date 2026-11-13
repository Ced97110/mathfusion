import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(56)
text(ax, 44, 51, r'$-1\leq x<4$', 'sujet', 'l')
y = 28
f = numberline(ax, 8, 70, y, -2, 5, arrow_right=True)
seg(ax, f(-1), f(4), y, 'resultat')
pt(ax, f(-1), y, True, 'resultat'); pt(ax, f(4), y, False, 'resultat')
text(ax, f(-1), y + 7, r'$a=-1$ : plein', 'resultat', 's'); text(ax, f(4), y + 7, r'$b=4$ : vide', 'resultat', 's')
brace(ax, f(-1), f(4), y - 7, 'varie', label='longueur 5')
save(fig, '17-085')
