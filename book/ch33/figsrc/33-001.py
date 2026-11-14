import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, y0 = 8, 30
k = 70 / 12  # mm per metre
s = 1 / 12
poly(ax, [(x0, y0), (x0 + 12 * k, y0), (x0 + 12 * k, y0 + 12 * k * s)], 'autre')
poly(ax, [(x0, y0), (x0 + 6 * k, y0), (x0 + 6 * k, y0 + 6 * k * s)], 'sujet')
line(ax, [(x0, y0), (x0 + 12 * k, y0 + 12 * k * s)], 'encre', lw=1.0)
brace(ax, x0, x0 + 6 * k, y0 - 1, 'sujet', label='avance 6 m')
brace(ax, x0, x0 + 12 * k, y0 - 9, 'autre', label='avance 12 m')
text(ax, 24, y0 + 14, 'montée 0,5 m', 'sujet')
arrow(ax, (30, y0 + 11.5), (x0 + 6 * k, y0 + 1.2), 'sujet')
text(ax, 62, y0 + 17, 'montée 1 m', 'autre')
arrow(ax, (70, y0 + 14.5), (x0 + 12 * k, y0 + 3.5), 'autre')
box(ax, 8, 2, 72, 9, 'resultat', label=r'$0{,}5 \div 6 = 1 \div 12 = 1/12$')
text(ax, 44, 56, 'même inclinaison, même rapport', 'encre', 's')
save(fig, '33-001')
