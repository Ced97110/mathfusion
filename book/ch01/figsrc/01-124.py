import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s = 5
def sq(x, y, role): box(ax, x, y, s, s, role, r=0.3, lw=0.5)
for i in range(1, 5):
    for k in range(i): sq(4 + s * (i - 1), 14 + s * k, 'sujet')
text(ax, 14, 10, '1 + 2 + 3 + 4', 'sujet', 's')
for c, n in enumerate((4, 3, 2, 1)):
    for k in range(n): sq(26 + s * c, 39 - s * (k + 1), 'varie')
text(ax, 36, 10, 'copie retournée', 'varie', 's')
arrow(ax, (48, 26), (56, 26), 'varie')
for i in range(1, 5):
    x = 60 + s * (i - 1)
    for k in range(i): sq(x, 14 + s * k, 'sujet')
    for k in range(i, 5): sq(x, 14 + s * k, 'varie')
    text(ax, x + 2.5, 10 if i % 2 else 5.5, f'{i}+{5 - i}', 'sujet', 's')
line(ax, [(82, 14), (82, 39)], 'fixe'); line(ax, [(81, 14), (83, 14)], 'fixe'); line(ax, [(81, 39), (83, 39)], 'fixe')
text(ax, 85, 26.5, '5', 'fixe', 's')
brace(ax, 60, 80, 41, 'fixe', '4 colonnes', down=False)
text(ax, 70, 54, r'$4\times5=20$ carrés', 'resultat', 's')
save(fig, '01-124')
