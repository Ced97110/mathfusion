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

fig, ax = canvas(80)
text(ax, 4, 73, r'$x$', 'sujet', 'l', ha='left'); mat(ax, 18, 73, (1, 2, 0, 1), 'sujet', 'm')
text(ax, 29, 73, r'$\times$', 'encre', 'l'); text(ax, 36, 73, r'$y$', 'sujet', 'l', ha='left'); mat(ax, 50, 73, (1, 0, 3, 1), 'sujet', 'm')
text(ax, 76, 73, r'$a=5$ : nombre', 'varie', 's')
rows = [r'$a\,(x\,y)$', r'$(a\,x)\,y$', r'$x\,(a\,y)$']
for i, e in enumerate(rows):
    y = 49 - i * 19
    box(ax, 4, y - 7, 34, 14, 'fixe', label=e, size='l')
    arrow(ax, (40, y), (60, y), 'resultat')
    mat(ax, 73, y, (35, 10, 15, 5), 'resultat', 'm')
text(ax, 28, 63, r'$x$, $y$ : éléments', 'sujet', 's')
save(fig, '76-018')
