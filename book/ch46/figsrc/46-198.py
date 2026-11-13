import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [12, 32, 52, 72]
rows = [(36, ['1', '2', '2', '2']), (10, ['2', '1', '3', '3'])]
heads = ['(1 2)', '(1 3)', '(1 4)']
for k, h in enumerate(heads):
    text(ax, (cx[k] + cx[k + 1]) / 2, 58, h, 'varie', 'm')
for y, v in rows:
    for k in range(4):
        if k == 0: r = 'sujet'
        elif k == 3: r = 'resultat'
        else: r = 'varie' if v[k] != v[k - 1] else 'fixe'
        box(ax, cx[k] - 6, y, 12, 9, r, label=v[k], size='l')
    for k in range(3):
        a, b = (cx[k] + 6.5, y + 4.5), (cx[k + 1] - 6.5, y + 4.5)
        if v[k] != v[k + 1]: arrow(ax, a, b, 'varie')
        else: line(ax, [a, b], 'fixe', dash=True)
text(ax, 4, 51, 'ligne 1 : on suit le nombre 1', 'sujet', 's', ha='left')
text(ax, 4, 26, 'ligne 2 : on suit le nombre 2', 'sujet', 's', ha='left')
text(ax, 60, 32, 'pointillés : plus touché', 'fixe', 's', ha='right')
text(ax, 84, 4, 'vert : arrivée', 'resultat', 's', ha='right')
save(fig, '46-198')
