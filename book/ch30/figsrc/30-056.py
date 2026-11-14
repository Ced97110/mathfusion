import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 62, 'x = 30°', 'sujet', 'm'); text(ax, 66, 62, 'x + π', 'varie', 'm')
text(ax, 6, 48, 'sin', 'fixe', 's', ha='left'); text(ax, 6, 36, 'cos', 'fixe', 's', ha='left')
for xc, n, d, role in ((24, '0,5', '0,866', 'sujet'), (66, '−0,5', '−0,866', 'varie')):
    text(ax, xc, 48, n, role, 'm'); line(ax, [(xc - 9, 42), (xc + 9, 42)], role); text(ax, xc, 36, d, role, 'm')
    text(ax, xc, 24, '= 0,577', 'resultat', 'm')
arrow(ax, (38, 42), (50, 42), 'varie'); text(ax, 44, 47, '+ π', 'varie', 's')
text(ax, 66, 54, 'deux signes −', 'varie', 's')
text(ax, 44, 10, r'$(-a)/(-b)=a/b$', 'resultat', 'l')
save(fig, '30-056')
