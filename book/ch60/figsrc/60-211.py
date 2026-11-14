import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def colmat(fig, ax, cx, cy, cols, role, sz='l', gap=9):
    r = fig.canvas.get_renderer(); h = 0; n = len(cols); x0 = cx - (n - 1) * gap / 2
    for j, c in enumerate(cols):
        t = text(ax, x0 + j * gap, cy, '\n'.join(c), role, sz)
        h = max(h, t.get_window_extent(r).height * 25.4 / fig.dpi)
    hw = (n - 1) * gap / 2 + gap * 0.55; hh = h / 2 + 1
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.5, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.5, cy - hh)], 'fixe')

fig, ax = canvas(62)
colmat(fig, ax, 22, 34, [['−2', '−1', '−1'], ['−2', '−1', '−1'], ['6', '3', '3']], 'sujet')
text(ax, 22, 12, r'$A-1\neq0$', 'sujet', 'm')
arrow(ax, (40, 34), (52, 34), 'varie')
text(ax, 46, 40, 'au carré', 'varie', 's')
colmat(fig, ax, 70, 34, [['0', '0', '0']] * 3, 'resultat')
text(ax, 70, 12, r'$(A-1)^2=0$', 'resultat', 'm')
save(fig, '60-211')
