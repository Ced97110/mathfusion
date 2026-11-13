import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
y0 = 14; k = 40
for x, a, v, role, lab in [(14, '40°', 0.8391, 'sujet', '0,8391 < 1'), (37, '45°', 1.0, 'fixe', '1'), (60, '50°', 1.1918, 'varie', '1,1918 > 1')]:
    box(ax, x, y0, 14, v * k, role, r=0.3)
    text(ax, x + 7, y0 - 4, a, role, 'm')
    text(ax, x + 7, y0 + v * k + 4, lab, role, 's')
line(ax, [(4, y0 + k), (84, y0 + k)], 'fixe', dash=True)
text(ax, 2, y0 + k + 3.5, 'tan = 1', 'fixe', 's', ha='left') if False else None
save(fig, '25-093')
