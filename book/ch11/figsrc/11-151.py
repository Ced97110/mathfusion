import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
k = 3.6; sl = 6
def para(x0, y0, role):
    pts = [(x0, y0), (x0 + 6 * k, y0), (x0 + 6 * k + sl, y0 + 4 * k), (x0 + sl, y0 + 4 * k)]
    poly(ax, pts, role); return pts
yb = 16
para(5, yb, 'sujet')
line(ax, [(5 + sl, yb), (5 + sl, yb + 4 * k)], 'varie', dash=True)
text(ax, 5 + sl + 6 * k / 2, yb + 4 * k + 3, r'$b_1 = 6$', 'sujet', 's')
text(ax, 5 + 6 * k / 2, yb - 3, r'$b_2 = 6$', 'sujet', 's')
text(ax, 5 + sl - 1.5, yb + 2 * k, r'$h = 4$', 'varie', 's', ha='right')
text(ax, 5 + 3 * k + sl / 2, 52, 'trapèze', 'sujet', 'm')
text(ax, 5 + 3 * k + sl / 2, 5, r'$(6+6)\times 4\div 2 = 24$', 'resultat', 's')
x2 = 52
para(x2, yb, 'autre')
text(ax, x2 + 3 * k + sl / 2, 52, 'parallélogramme', 'autre', 'm')
text(ax, x2 + 3 * k + sl / 2, yb - 3, 'base 6', 'autre', 's')
text(ax, x2 + sl - 1.5, yb + 2 * k, r'$h = 4$', 'varie', 's', ha='right')
line(ax, [(x2 + sl, yb), (x2 + sl, yb + 4 * k)], 'varie', dash=True)
text(ax, x2 + 3 * k + sl / 2, 5, r'$6\times 4 = 24$', 'resultat', 's')
save(fig, '11-151')
