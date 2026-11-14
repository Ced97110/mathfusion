import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [['000'], ['100', '010', '001'], ['110', '101', '011'], ['111']]
ys = [62, 46, 30, 14]
poly(ax, [(24, 40), (82, 40), (82, 68), (24, 68)], 'sujet', fill=False, lw=1.0)
text(ax, 53, 73, r'$B(000,\,1)$ : distance $\leq 1$', 'sujet', 'm')
text(ax, 9, 73, 'distance', 'fixe', 's')
for r, (ws, y) in enumerate(zip(rows, ys)):
    text(ax, 9, y, str(r), 'varie', 'l')
    for i, w in enumerate(ws):
        cx = 53 + (i - (len(ws) - 1) / 2) * 18
        box(ax, cx - 7, y - 3.5, 14, 7, 'sujet' if r < 2 else 'fixe', label=w)
save(fig, '68-062')
