import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cols = [(15, 'resultat', r'$e<0$', r'$u>0$', 0.5, '2 points en bas'),
        (44, 'varie', r'$e=0$', r'$u=0$', 0.0, '1 point double'),
        (73, 'fixe', r'$e>0$', r'$u<0$', -0.5, 'aucun point en bas')]
for cx, role, e, ut, uv, cnt in cols:
    text(ax, cx, 66, e, role, 'm')
    f = numberline(ax, cx - 11, cx + 11, 52, -1, 1, 1, labels=False, arrow_right=False)
    disc(ax, f(uv), 52, 1.4, role)
    text(ax, cx, 59, ut, role, 's')
    g = numberline(ax, cx - 11, cx + 11, 30, -1, 1, 1, labels=False, arrow_right=False)
    if uv > 0:
        for sx in (-1, 1):
            disc(ax, g(sx * uv ** 0.5), 30, 1.4, role)
    elif uv == 0:
        disc(ax, g(0), 30, 2.0, role, fill=False)
        disc(ax, g(0), 30, 1.2, role)
    text(ax, cx, 22, cnt, role, 's')
    arrow(ax, (cx, 48), (cx, 36), 'fixe', lw=0.6)
text(ax, 44, 8, 'frontière : $e=0$', 'varie', 'm')
save(fig, '70-116')
