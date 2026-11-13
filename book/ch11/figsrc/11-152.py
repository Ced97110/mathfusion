import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
k = 4.0; H = 4 * k; yb = 22
cases = [(6, 'sujet', '(6+6)×4÷2 = 24'), (3, 'sujet', '(6+3)×4÷2 = 18'), (0, 'resultat', '(6+0)×4÷2 = 12')]
for i, (b2, role, f) in enumerate(cases):
    x0 = 3 + i * 29.5
    cx = x0 + 12
    w2 = b2 * k
    poly(ax, [(x0, yb), (x0 + 24, yb), (cx + w2 / 2, yb + H), (cx - w2 / 2, yb + H)], role)
    text(ax, cx, yb + H + 4, rf'$b_2 = {b2}$', role, 's')
    text(ax, cx, yb - 4, f, role, 's')
arrow(ax, (14, 58), (72, 58), 'varie')
text(ax, 43, 53.5, r'$b_2$ diminue', 'varie', 's')
text(ax, 43, 8, r'$b_1 = 6$ et $h = 4$ ne changent pas', 'fixe', 's')
save(fig, '11-152')
