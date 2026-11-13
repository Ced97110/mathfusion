import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
fig, ax = canvas(70)
text(ax, 44, 68, r'$-1\leq x<4$', 'sujet', 'l')
y = 57
f = numberline(ax, 8, 70, y, -2, 6, labels=False, arrow_right=True)
ax.plot([f(-1), f(4)], [y, y], color=COL['resultat'], lw=2.6, zorder=3, solid_capstyle='butt')
for v in (-1, 0, 4):
    pt(ax, f(v), y, v != 4, 'resultat' if v != 4 else 'limite')
text(ax, f(-1), y - 4, r'$-1$', 'encre', 's'); text(ax, f(4), y - 4, '4', 'encre', 's')
text(ax, 18, 46, 'test gauche', 'encre', 's'); text(ax, 52, 46, 'test droite', 'encre', 's')
cases = [(37, r'$-1\leq -1$', r'$-1<4$', True), (26, r'$-1\leq 0$', r'$0<4$', True), (15, r'$-1\leq 4$', r'$4<4$', False)]
for yc, l, r_, keep in cases:
    ok_r = keep
    box(ax, 2, yc - 4.5, 32, 9, 'resultat', label=l + ' : vrai' if False else l)
    box(ax, 36, yc - 4.5, 32, 9, 'resultat' if ok_r else 'limite', label=r_)
    box(ax, 70, yc - 4.5, 16, 9, 'resultat' if keep else 'limite', label='gardé' if keep else 'refusé', size='s')
save(fig, '17-082')
