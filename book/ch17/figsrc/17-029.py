import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
f = numberline(ax, 8, 70, 22, 7, 10, step=0.5, labels=False)
text(ax, 44, 46, r'$2y - 1 \leq 16$', 'sujet', 'l', weight='bold')
text(ax, 2, 34, r'$2y - 1$ :', 'encre', 's', ha='left')
for v, val, ok in ((8, 15, True), (8.5, 16, True), (9, 17, False)):
    role = 'resultat' if ok else 'limite'
    dot(f(v), 22, role, r=2)
    text(ax, f(v), 16.5, f'{v:g}'.replace('.', ','), role, 's')
    text(ax, f(v), 34, str(val), role, 's')
    text(ax, f(v), 28, 'vrai' if ok else 'faux', role, 's')
brace(ax, f(8), f(9), 12, 'varie', label='le passage est entre 8 et 9', down=True)
save(fig, '17-029')
