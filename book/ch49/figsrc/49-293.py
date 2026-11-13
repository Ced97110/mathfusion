import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
xs = [8 + i * 18 for i in range(5)]
ys = [72, 46, 20]
names = ['avant', r'après $e$', r'après $g$']
for k, y in enumerate(ys):
    for x in xs:
        disc(ax, x, y, 3.4, 'sujet')
    text(ax, 35, y + 7.5, names[k], 'fixe', 's')
for x in xs:
    for k in range(2):
        line(ax, [(x, ys[k] - 3.4), (x, ys[k + 1] + 3.4)], 'fixe', lw=1.0)
text(ax, 44, 87, 'chaque élément laisse les 5 objets', 'encre', 's')
box(ax, 4, 2, 80, 9, 'resultat', label=r'$5+5=10$ ; $10 \div 2 = 5$ orbites', size='s')
save(fig, '49-293')
