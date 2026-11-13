import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s = 20; x0, y0 = 14, 20
for i in range(2):
    for j in range(2):
        box(ax, x0 + i * s, y0 + j * s, s, s, 'sujet', label=r'$a^2$', size='l', r=0.3)
brace(ax, x0, x0 + 2 * s, y0 + 2 * s + 1, 'varie', r'côté $2a = 6$', down=False)
text(ax, 62, 50, r'$(2a)^2 = 36$', 'varie', 'm', ha='left')
text(ax, 62, 40, r'4 carrés $a^2$', 'sujet', 'm', ha='left')
text(ax, 62, 33, r'$4 \times 9 = 36$', 'resultat', 'm', ha='left')
text(ax, 44, 10, r'$(2a)^2 = 4a^2$ pour $a = 3$', 'resultat', 'm')
text(ax, 44, 3, r'sert dans $b^2 - 4ac$', 'fixe', 's')
save(fig, '14-100')
