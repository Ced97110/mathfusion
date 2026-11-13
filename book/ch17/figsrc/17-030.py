import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
f = numberline(ax, 8, 70, 28, -4, 4, labels=False, arrow_right=False)
line(ax, [(f(-2), 28), (f(2), 28)], 'resultat', lw=2.2)
for v in (-2, 2):
    dot(f(v), 28, 'limite', full=False, r=2); text(ax, f(v), 22, ('−%d' % -v) if v < 0 else str(v), 'limite', 's')
for v, ok in ((-3, False), (-1, True), (1, True), (3, False)):
    role = 'resultat' if ok else 'limite'
    dot(f(v), 28, role, r=2)
    text(ax, f(v), 22, ('−%d' % -v) if v < 0 else str(v), role, 's')
    text(ax, f(v), 35, str(v * v), role, 's')
text(ax, 2, 41, r'$x^2$ :', 'encre', 's', ha='left')
text(ax, 44, 52, r'$x^2 < 4$', 'sujet', 'l', weight='bold')
brace(ax, f(-2), f(2), 17, 'resultat', label='deux bouts : pas une demi-droite', down=True)
save(fig, '17-030')
