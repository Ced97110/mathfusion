import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, v, role='sujet', size='m'):
    """Matrice 2x2 : quatre nombres alignés, crochets."""
    a, b, c, d = [str(t) for t in v]
    w0, w1 = max(len(a), len(c)), max(len(b), len(d))
    p = lambda s, w: s.rjust(w, ' ')
    text(ax, cx, cy, f"{p(a, w0)}  {p(b, w1)}\n{p(c, w0)}  {p(d, w1)}", role, size)
    hw = ((w0 + w1) * 1.65 + 1.7) / 2 + 1.4; hh = 4.2
    for s in (-1, 1):
        line(ax, [(cx + s * (hw - 1.1), cy + hh), (cx + s * hw, cy + hh), (cx + s * hw, cy - hh), (cx + s * (hw - 1.1), cy - hh)], role, lw=0.8)

def eq(ax, x, y, w=3.6):
    line(ax, [(x - w / 2, y + 0.9), (x + w / 2, y + 0.9)], 'encre', lw=0.9)
    line(ax, [(x - w / 2, y - 0.9), (x + w / 2, y - 0.9)], 'encre', lw=0.9)
fig, ax = canvas(58)
text(ax, 44, 53, 'algèbre : tableaux diagonaux', 'fixe', 's')
mat(ax, 13, 34, (4, 0, 0, 0), 'sujet', 'l'); text(ax, 27, 34, r'$\times$', 'encre', 'l')
mat(ax, 41, 34, (3, 0, 0, 7), 'autre', 'l'); eq(ax, 56, 34)
mat(ax, 71, 34, (12, 0, 0, 0), 'resultat', 'l')
text(ax, 13, 22, 'dans l’idéal', 'sujet', 's'); text(ax, 41, 22, 'facteur quelconque', 'autre', 's')
text(ax, 71, 22, 'dans l’idéal', 'resultat', 's')
text(ax, 44, 9, 'seconde case nulle : elle le reste', 'resultat', 's', weight='bold')
save(fig, '76-046')
