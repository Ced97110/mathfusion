import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'$\frac{1}{|G|}$', 'sujet', 'xl')
text(ax, 44, 46, r'$|G|$ = 4 éléments', 'sujet', 'm')
for i in range(4):
    disc(ax, 26 + i * 12, 38, 3.4, 'sujet')
text(ax, 44, 26.5, 'total : 12', 'fixe', 'm')
for g in range(4):
    for k in range(3):
        box(ax, 6 + g * 20 + k * 6, 14, 5, 7, 'resultat' if g == 0 else 'fixe', r=0.5)
brace(ax, 6, 22, 13, 'resultat', label='3', down=True)
text(ax, 62, 6, r'$\div$ 4 : une part de 3', 'varie', 's')
save(fig, '49-209')
