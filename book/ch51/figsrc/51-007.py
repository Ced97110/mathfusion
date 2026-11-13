import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 14, 20, 34, 'sujet')
text(ax, 12, 38, 'une preuve', 'sujet', 's', weight='bold')
text(ax, 12, 30, 'à partir des', 'sujet', 's')
text(ax, 12, 24, 'huit règles', 'sujet', 's')
rows = [['entiers', 'fractions', 'réels', 'polynômes'], ['cadran 2 h', 'cadran 3 h', 'cadran 4 h', '…'], ['tableau 2 lignes', 'tableau 3 lignes', '…']]
for i, r in enumerate(rows):
    y = 46 - 17 * i
    arrow(ax, (22, 31), (26, y + 5.5), 'resultat')
    n = len(r)
    ws = [14.5] * 4 if i < 2 else [22, 22, 13]
    x = 27
    for lab, w in zip(r, ws):
        box(ax, x, y, w, 11, 'fixe' if lab == '…' else 'resultat', label=lab, size='s', dash=(lab == '…'))
        x += w + 0.7
save(fig, '51-007')
