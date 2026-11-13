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

fig, ax = canvas(66)
text(ax, 44, 61, 'sous-algèbre engendrée par S', 'sujet', 's', weight='bold')
box(ax, 2, 12, 84, 42, 'sujet')
mat(ax, 13, 44, (0, 1, 0, 0), 'varie', 'm'); text(ax, 24, 44, r'$S=\{e_{12}\}$', 'varie', 's', ha='left')
mat(ax, 13, 22, (1, 0, 0, 1), 'autre', 'm'); text(ax, 24, 22, 'unité ajoutée', 'autre', 's', ha='left')
arrow(ax, (44, 44), (55, 37), 'varie'); arrow(ax, (44, 22), (55, 30), 'autre')
mat(ax, 71, 34, ('a', 'b', 0, 'a'), 'resultat', 'm'); text(ax, 71, 25, r'$a\cdot1+b\,e_{12}$', 'resultat', 's')
text(ax, 71, 47.5, r'$e_{12}e_{12}=0$' + '\nla liste s’arrête', 'fixe', 's')
text(ax, 44, 5.5, 'la plus petite contenant S', 'sujet', 's', weight='bold')
save(fig, '76-045')
