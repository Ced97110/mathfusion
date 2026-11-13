import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
f = numberline(ax, 8, 70, 24, -6, 3, labels=False)
line(ax, [(f(-3), 24), (75, 24)], 'resultat', lw=2.2)
text(ax, 44, 54, r'$x + 7 > 4$', 'sujet', 'l', weight='bold')
for v, ok in ((-5, False), (-3, False), (0, True), (1, True)):
    role = 'resultat' if ok else 'limite'
    dot(f(v), 24, role, full=(v != -3), r=2)
    text(ax, f(v), 17.5, ('−%d' % -v) if v < 0 else str(v), role, 's')
    text(ax, f(v), 31, str(v + 7), role, 's')
text(ax, 2, 31, r'$x + 7$ :', 'encre', 's', ha='left')
text(ax, f(-4), 40, 'faux', 'limite', 'm'); text(ax, f(0.5), 40, 'vrai', 'resultat', 'm')
save(fig, '17-025')
