import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
f = numberline(ax, 6, 68, 18, -6, 8, labels=False)
for a, b in ((-5, -1), (3, 7)):
    dot(f(a), 18, 'sujet', r=2); dot(f(b), 18, 'autre', r=2)
    text(ax, f(a), 12.5, '−%d' % -a if a < 0 else str(a), 'sujet', 's')
    text(ax, f(b), 12.5, '−%d' % -b if b < 0 else str(b), 'autre', 's')
    arrow(ax, (f(a), 22), (f(b), 22), 'resultat', curve=-0.4)
text(ax, f(-3), 33, r'$-5 < -1$', 'resultat', 'm')
text(ax, f(5), 33, r'$3 < 7$', 'resultat', 'm')
text(ax, 44, 48, r'$a < b$ : $a$ à gauche de $b$', 'sujet', 'l', weight='bold')
save(fig, '17-022')
