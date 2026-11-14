import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 4.5; x0 = 12; y = 24; h = 9
vals = [(1, r'$1^2$'), (4, r'$(-2)^2$'), (9, r'$3^2$')]
x = x0
for v, cap in vals:
    box(ax, x, y, v * u, h, 'sujet', label=str(v), r=0.4)
    text(ax, x + v * u / 2, y + h + 4, cap, 'sujet', 's')
    x += v * u
line(ax, [(x0, y - 2), (x0, y + h + 1)], 'fixe', lw=1.0)
text(ax, x0, y - 5, '0', 'fixe', 's')
brace(ax, x0, x, y - 1, 'resultat', label=r'$1+4+9=14$', down=True)
text(ax, 44, 4, 'positif, donc pas 0', 'resultat', 's')
save(fig, '69-033')
