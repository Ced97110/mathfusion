import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 14, 42, 60, 18, 'fixe')
text(ax, 44, 54, '1, 2, 3, 4', 'encre', 'm')
text(ax, 44, 47, 'aucune règle de produit', 'limite', 's')
arrow(ax, (44, 42), (44, 33), 'varie')
text(ax, 48, 37.5, r'avec $i$, $j$, $k$', 'varie', 's', ha='left')
box(ax, 4, 18, 80, 13, 'sujet')
parts = [('1 + 2', 'sujet'), (r'$i$', 'varie'), (' + 3', 'sujet'), (r'$j$', 'varie'), (' + 4', 'sujet'), (r'$k$', 'varie')]
r = fig.canvas.get_renderer()
ts = [text(ax, 0, 24.5, s, ro, 'l', ha='left') for s, ro in parts]
ws = [t.get_window_extent(r).width / fig.dpi * 25.4 for t in ts]
cur = (W - sum(ws) - 1.0 * (len(ws) - 1)) / 2
for t, wd in zip(ts, ws):
    t.set_x(cur); cur += wd + 1.0
text(ax, 44, 11, 'on peut développer', 'resultat', 'm')
save(fig, '51-170')
