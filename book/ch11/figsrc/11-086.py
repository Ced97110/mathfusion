import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(58)
f = numberline(ax, 8, 80, 22, 0, 22, step=1, every=7, arrow_right=False)
for i in range(3):
    a, b = f(7 * i), f(7 * i + 7)
    arrow(ax, (a + 0.3, 30), (b - 0.3, 30), 'sujet', lw=1.2, both=True)
    text(ax, (a + b) / 2, 34, '7 cm', 'sujet', 's')
arrow(ax, (f(21) + 0.2, 30), (f(22) - 0.2, 30), 'varie', lw=1.2, both=True)
text(ax, f(21.5), 41, 'reste ≈ 1 cm', 'varie', 's')
arrow(ax, (f(21.5), 39), (f(21.5), 31.5), 'varie', lw=0.8)
text(ax, 44, 52, 'le diamètre tient 3 fois', 'encre', 's')
text(ax, 44, 8, 'tour déroulé (cm)', 'fixe', 's')
save(fig, '11-086')
