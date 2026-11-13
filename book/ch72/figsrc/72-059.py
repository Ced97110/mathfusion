import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def mat(x, y, w, h, t, role, lab):
    line(ax, [(x + 1.5, y), (x, y), (x, y + h), (x + 1.5, y + h)], role, lw=1.0)
    line(ax, [(x + w - 1.5, y), (x + w, y), (x + w, y + h), (x + w - 1.5, y + h)], role, lw=1.0)
    text(ax, x + w / 2, y + h / 2, t, role, 'm')
    text(ax, x + w / 2, y + h + 4, lab, role, 'm')
w = 15; y = 14; hh = 16
t1 = '5/4   3/4\n3/4   5/4'; t2 = '1     0\n0   −1'
xs = [2, 25, 48, 71]
mat(xs[0], y, w, hh, t1, 'sujet', r'$h$'); mat(xs[1], y, w, hh, t2, 'fixe', r'$b$')
mat(xs[2], y, w, hh, t1, 'sujet', r'$h^t$'); mat(xs[3], y, w, hh, t2, 'resultat', r'$b$')
for x in (xs[0] + w + 3.5, xs[1] + w + 3.5): text(ax, x, y + hh / 2, '·', 'encre', 'xl', weight='bold')
text(ax, xs[2] + w + 3.5, y + hh / 2, '=', 'resultat', 'xl', weight='bold')
text(ax, 44, 45, r'$h\cdot b\cdot h^t=b$', 'encre', 'l')
text(ax, 44, 5, r'ici $h^t=h$ : on retrouve $b$', 'resultat', 's')
save(fig, '72-059')
