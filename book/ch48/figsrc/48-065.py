import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(98)
text(ax, 20, 94, r'dans $G$', 'sujet'); text(ax, 66, 94, r'dans $G^{\prime}$', 'autre')
H, Hp = r'$f^{-1}(H^{\prime})$', r'$H^{\prime}$'
rows = [(70, 'sujet', 'autre', r'$h = 6$' + '\ndans ' + H, r'$f(h) = 2$' + '\ndans ' + Hp),
        (46, 'sujet', 'autre', r'$g\,h\,g^{-1}$' + '\n3 + 6 − 3', r'$f(g)\,f(h)\,f(g)^{-1}$' + '\n3 + 2 − 3'),
        (22, 'resultat', 'resultat', '= 6\ndans ' + H, '= 2\ndans ' + Hp)]
for y, ra, rb, a, b in rows:
    box(ax, 2, y, 36, 16, ra, a, 's'); box(ax, 46, y, 40, 16, rb, b, 's')
    arrow(ax, (38, y + 8), (46, y + 8), 'varie'); text(ax, 42, y + 12, r'$f$', 'varie', 's')
for y in (70, 46):
    arrow(ax, (20, y), (20, y - 8), 'fixe'); arrow(ax, (66, y), (66, y - 8), 'fixe')
text(ax, 44, 8, r"$H^{\prime}$ normal $\Rightarrow$ $f^{-1}(H^{\prime})$ normal", 'resultat', 's', weight='bold')
save(fig, '48-065')
