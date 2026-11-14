import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def cell(x, y, s, role, w=11):
    box(ax, x, y, w, 8, role, label=s, size='s')
def cancel(x, y1, y2, w=11):
    line(ax, [(x + 1, y1 + 1), (x + w - 1, y2 + 7)], 'limite', lw=1.2)
    line(ax, [(x + 1, y2 + 1), (x + w - 1, y1 + 7)], 'limite', lw=1.2)
# row 1 : 6/9 = (2 x 3) / (3 x 3)
yt, yb = 64, 50
x = [4, 18, 32]
cell(x[0], yt, '2', 'sujet'); text(ax, x[1] + 5.5, yt + 4, '×', 'encre', 'm'); cell(x[2], yt, '3', 'varie')
cell(x[0], yb, '3', 'sujet'); text(ax, x[1] + 5.5, yb + 4, '×', 'encre', 'm'); cell(x[2], yb, '3', 'varie')
line(ax, [(3, 60), (45, 60)], 'encre', lw=1.0)
cancel(x[2], yb, yt)
text(ax, 64, 58, r'$=\ \frac{2}{3}$', 'resultat', 'l')
# row 2 : 36 po x (1 pied / 12 po)
yt, yb = 28, 14
cell(4, yt, '36', 'sujet'); cell(18, yt, 'po', 'varie'); text(ax, 36, yt + 4, '×', 'encre', 'm'); cell(40, yt, '1 pied', 'sujet', w=16)
cell(4, yb, '12', 'sujet'); cell(18, yb, 'po', 'varie')
line(ax, [(3, 24), (58, 24)], 'encre', lw=1.0)
cancel(18, yb, yt)
text(ax, 73, 22, '= 3 pieds', 'resultat', 'm')
save(fig, '11-156')
