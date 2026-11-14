import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
cols = [(24, 'resultat', 'exact', r'$1/12$', '4,76°'), (64, 'limite', 'arrondi d’abord', r'$0{,}08$', '4,57°')]
for cx, role, head, ratio, ang in cols:
    text(ax, cx, 72, head, role, 's')
    box(ax, cx - 14, 56, 28, 9, 'sujet' if role == 'resultat' else 'limite', label=ratio)
    arrow(ax, (cx, 55), (cx, 41), 'varie')
    text(ax, cx + 9, 48, 'arctan', 'varie', 's')
    box(ax, cx - 14, 31, 28, 9, role, label=ang)
f = numberline(ax, 10, 70, 14, 4.5, 4.8, step=0.1, role='fixe', arrow_right=False)
for v, role in ((4.57, 'limite'), (4.76, 'resultat')):
    disc(ax, f(v), 14, 1.6, role)
brace(ax, f(4.57), f(4.76), 18.5, 'fixe', label='écart', down=False)
save(fig, '33-098')
