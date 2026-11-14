import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
sets = [r'$H=\{0,\,4,\,8\}$', r'$\{1,\,5,\,9\}$', r'$\{2,\,6,\,10\}$', r'$\{3,\,7,\,11\}$']
text(ax, 44, 86, '4 classes de 3 positions', 'encre', 'm')
for i, st in enumerate(sets):
    y = 66 - i * 14
    role = 'sujet' if i == 0 else 'varie'
    box(ax, 4, y - 5.5, 80, 11, role)
    for k in range(3): disc(ax, 13 + k * 10, y, 3.6, role)
    text(ax, 64, y, st, role, 'm')
text(ax, 44, 7, r'$4\times3=12$', 'resultat', 'l')
save(fig, '43-146')
