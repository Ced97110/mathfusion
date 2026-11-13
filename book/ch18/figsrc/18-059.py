import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 1.7; y0 = 14
def sq(x0, w, role, lab=None): box(ax, x0, y0, w * u, w * u, role, label=lab, r=0.2)
def sq2(x, y, w, role): box(ax, x, y, w * u, w * u, role, r=0.2)
for cx, b, head in ((15, 3, r'$(x+3)^2$'), (44, 5, r'$(x+5)^2$')):
    s = (10 + b) * u; x0 = cx - s / 2
    sq(x0, 10 + b, 'fixe'); sq2(x0, y0, 10, 'sujet'); sq2(x0 + 10 * u, y0 + 10 * u, b, 'varie')
    text(ax, x0 + 5 * u, y0 + 5 * u, r'$x^2$', 'sujet', 's')
    text(ax, cx, y0 + s + 6, head, 'encre', 'm', weight='bold')
    text(ax, cx, 7, f'{b * b} = {b} × {b}', 'varie', 's')
cx = 73; x0 = cx - 5 * u * 1.0 * 1.7 / 1.7
x0 = cx - 10 * u / 2
sq(x0, 10, 'fixe'); sq2(x0, y0 + 4 * u, 6, 'sujet'); sq2(x0 + 6 * u, y0, 4, 'varie')
text(ax, cx, y0 + 10 * u + 6, r'$(x-4)^2$', 'encre', 'm', weight='bold')
text(ax, cx, 7, '16 = 4 × 4', 'varie', 's')
text(ax, 44, 52, 'le dernier terme est un carré', 'varie', 'm', weight='bold')
save(fig, '18-059')
