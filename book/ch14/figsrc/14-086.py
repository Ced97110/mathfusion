import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
steps = [('fixe', r'1. $2^3 = 8$'), ('fixe', r'2. $24 \div 8 = 3$'), ('sujet', r'3. $a^7 / a^4 = a^3$'),
         ('autre', r'4. $b^9 / b^{-6} = b^{15}$'), ('resultat', r'5. $3\,a^3\,b^{15}$')]
ys = []
for i, (role, s) in enumerate(steps):
    y = 74 - i * 16; ys.append(y)
    box(ax, 3, y, 44, 12, role, label=s, size='m')
    if i < 4: arrow(ax, (25, y), (25, y - 4), 'varie')
box(ax, 56, 24, 28, 32, 'limite')
text(ax, 70, 51, 'étapes 3 et 4 :', 'limite', 's')
text(ax, 70, 45, r'$a = 0$ ou $b = 0$', 'limite', 's')
text(ax, 70, 39, r'$0^4 = 0$', 'limite', 'm')
text(ax, 70, 31, r'$\div\ 0$ : impossible', 'limite', 's')
arrow(ax, (56, 48), (47.5, 48), 'limite'); arrow(ax, (56, 32), (47.5, 32), 'limite')
save(fig, '14-086')
