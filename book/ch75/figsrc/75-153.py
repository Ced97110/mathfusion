import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 4.0; x = 8; yb = 12
text(ax, 44, 47, r'$x=(3,\,4i)$, matrice identité', 'encre', 'm')
for side, role, lab, bot in [(3, 'sujet', '9', r'$|3|^2$'), (4, 'varie', '16', r'$|4i|^2$'), (5, 'resultat', '25', 'somme')]:
    a = side * u
    box(ax, x, yb, a, a, role, label=lab, size='l', weight='bold', r=0.5)
    text(ax, x + a / 2, yb - 5, bot, role, 's')
    if side == 3: text(ax, x + a + 3.5, yb + a / 2, '+', 'encre', 'l')
    if side == 4: text(ax, x + a + 3.5, yb + a / 2, '=', 'encre', 'l')
    x += a + 7
save(fig, '75-153')
