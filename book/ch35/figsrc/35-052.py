import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
parts = [('cos(A', 'encre'), ('±', 'varie'), ('B) = cos A cos B', 'encre'), ('∓', 'varie'), ('sin A sin B', 'encre')]
r = fig.canvas.get_renderer()
gap = 1.6
ws = []
for s_, _ in parts:
    t = ax.text(0, 0, s_, fontsize=SIZE['l']); ws.append(t.get_window_extent(r).width / fig.dpi * 25.4); t.remove()
total = sum(ws) + gap * (len(parts) - 1)
x = (W - total) / 2 + 6
xs = []
for (s_, role), w in zip(parts, ws):
    text(ax, x, 42, s_, role, 'l', ha='left', weight='bold' if role == 'varie' else 'normal')
    xs.append(x + w / 2); x += w + gap
for (yy, a, b, role, lab) in [(28, '+', '−', 'sujet', 'somme'), (14, '−', '+', 'autre', 'différence')]:
    text(ax, 2, yy, lab, role, 's', ha='left')
    text(ax, xs[1], yy, a, role, 'xl', weight='bold')
    text(ax, xs[3], yy, b, role, 'xl', weight='bold')
    line(ax, [(xs[1] + 3.5, yy), (xs[3] - 3.5, yy)], role, lw=0.8, dash=True)
for k in (1, 3):
    arrow(ax, (xs[k], 38.5), (xs[k], 32.5), 'fixe', lw=0.8)
    arrow(ax, (xs[k], 24), (xs[k], 18.5), 'fixe', lw=0.8)
text(ax, 44, 3, 'on lit le haut des deux, ou le bas', 'fixe', 's')
save(fig, '35-052')
