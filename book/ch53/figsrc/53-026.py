import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 22, 46, 'avant : en phrase', 'fixe', 'm', weight='bold')
text(ax, 66, 46, r'avec le signe $f$', 'sujet', 'm', weight='bold')
rows = [(30, 'chiffré de 11 : 14', r'$f(11)=14$'), (10, 'chiffré de 0 : 3', r'$f(0)=3$')]
for y, a, b in rows:
    box(ax, 2, y, 40, 9, 'fixe', label=a)
    box(ax, 56, y, 30, 9, 'sujet', label=b, size='l')
    arrow(ax, (42, y + 4.5), (56, y + 4.5), 'varie')
save(fig, '53-026')
