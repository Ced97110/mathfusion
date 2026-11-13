import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
pw = [r'$2^{3}$', r'$2^{2}$', r'$2^{1}$', r'$2^{0}$', r'$2^{-1}$']
vals = [8, 4, 2, 1, 0.5]; txt = ['8', '4', '2', '1', r'$\frac{1}{2}$']
bw, gap = 13, 3.5
for i, v in enumerate(vals):
    x = 3 + i * (bw + gap); role = 'sujet' if i < 3 else 'varie'
    box(ax, x, 9, bw, max(v * 3.2, 1.6), role, r=0.4)
    text(ax, x + bw / 2, 4, txt[i], role, 'm')
    text(ax, x + bw / 2, 49, pw[i], role, 'l')
    if i < 4:
        arrow(ax, (x + bw / 2 + 1, 39), (x + bw / 2 + bw + gap - 1, 39), 'fixe')
        text(ax, x + bw / 2 + (bw + gap) / 2, 42.5, '÷ 2', 'fixe', 's')
save(fig, '14-006')
