import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, y0, sy = 14, 38, 18 / 13
f = numberline(ax, x0, 80, y0, 0, 1, step=0.5, arrow_right=False)
line(ax, [(x0, 16), (x0, 60)], 'fixe')
g = lambda t: (f(t), y0 + 13 * sy * math.sin(3 * math.pi * t))
line(ax, [g(i / 150) for i in range(151)], 'sujet', lw=1.6)
line(ax, [g(i / 150 * 2 / 3) for i in range(151)], 'varie', lw=2.0)
text(ax, 8, y0 + 13 * sy, '13', 'fixe', 's'); text(ax, 7, y0 - 13 * sy, '−13', 'fixe', 's')
text(ax, 84, y0, 't (s)', 'fixe', 's')
text(ax, 47, 66, r'$d = 13\,\sin(3\pi t)$', 'sujet', 'm')
brace(ax, x0, f(2 / 3), 17, 'varie', label='1 oscillation : 0,667 s')
save(fig, '30-169')
