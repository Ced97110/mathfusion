import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
vals = ['8', '4', '2', '1', r'$\frac{1}{2}$']; pw = [r'$2^{3}$', r'$2^{2}$', r'$2^{1}$', r'$2^{0}$', r'$2^{-1}$']
bw, gap = 12, 5.5
for i in range(5):
    x = 3 + i * (bw + gap); role = 'sujet' if i < 3 else 'resultat'
    box(ax, x, 18, bw, 11, role, label=vals[i], size='l', dash=i >= 3)
    text(ax, x + bw / 2, 34, pw[i], role, 'm')
    if i < 4:
        arrow(ax, (x + bw + 0.5, 23.5), (x + bw + gap - 0.5, 23.5), 'varie')
        text(ax, x + bw + gap / 2, 14.5, '÷2', 'varie', 's')
brace(ax, 3, 85, 11, 'varie', 'même règle : elle décide 1 et ½')
save(fig, '14-011')
