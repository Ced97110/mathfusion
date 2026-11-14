import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
vals = ['3', '4', '0', '1', '2', '3']
w, gap, x0, y = 10, 4, 4, 22
cx = []
for i, v in enumerate(vals):
    x = x0 + i * (w + gap)
    box(ax, x, y, w, 10, 'sujet' if i not in (0, 5) else 'limite', label=v)
    cx.append(x + w / 2)
    if i < 5:
        text(ax, x + w + gap / 2, y + 5, '<', 'encre', 's')
for i in range(5):
    arrow(ax, (cx[i], y - 0.5), (cx[i + 1], y - 0.5), 'varie', curve=0.8)
text(ax, 44, 4, '+1 à chaque pas', 'varie', 's')
arrow(ax, (cx[0], y + 10.5), (cx[5], y + 10.5), 'limite', curve=-0.3, both=True)
text(ax, 44, 52, r'$3<3$ : impossible', 'limite', 'm')
save(fig, '69-036')
