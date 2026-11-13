import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s = 5.0; g = 0.8
names = [('ℝ', 1), ('ℂ', 2), ('ℍ', 4), ('𝕆', 8)]
for k, (n, d) in enumerate(names):
    y = 6 + k * 17
    role = 'sujet' if n == '𝕆' else 'fixe'
    text(ax, 6, y + s/2, n, role, 'xl' if n == '𝕆' else 'l')
    x0 = 18
    for i in range(d):
        off = 3 if (n == '𝕆' and i >= 4) else 0
        box(ax, x0 + i * (s + g) + off, y, s, s, role, r=0.4)
    text(ax, 86, y + s/2, f'{d} nombre' + ('s' if d > 1 else ''), role, 's', ha='right')
    if k < 3:
        arrow(ax, (10, y + s + 1.5), (10, y + 17 - 1.5), 'varie'); text(ax, 15, y + s + 6, r'$\times2$', 'varie', 's')
text(ax, 44, 76, 'deux ℍ côte à côte', 'sujet', 's')
save(fig, '78-102')
