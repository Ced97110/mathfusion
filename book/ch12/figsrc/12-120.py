import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
u = 4.0; y0 = 16; h = 4 * u
box(ax, 3, y0, 7 * u, h, 'fixe', r=0.2); text(ax, 3 + 3.5 * u, y0 + h / 2, '28', 'encre', 'xl')
text(ax, 3 + 3.5 * u, y0 - 5, r'$a(b+c)$', 'encre', 'm')
text(ax, 35.5, y0 + h / 2, r'$=$', 'resultat', 'xl')
box(ax, 40, y0, 5 * u, h, 'sujet', r=0.2); text(ax, 40 + 2.5 * u, y0 + h / 2, '20', 'sujet', 'xl')
text(ax, 40 + 2.5 * u, y0 - 5, r'$ab$', 'sujet', 'm')
text(ax, 64, y0 + h / 2, r'$+$', 'varie', 'xl')
box(ax, 68, y0, 2 * u, h, 'varie', r=0.2); text(ax, 68 + u, y0 + h / 2, '8', 'varie', 'xl')
text(ax, 68 + u, y0 - 5, r'$ac$', 'varie', 'm')
text(ax, 44, 50, 'coupé en deux : même aire', 'encre', 'm')
save(fig, '12-120')
