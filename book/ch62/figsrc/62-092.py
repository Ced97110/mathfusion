import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(44, r'$5x^3$', r'$15x^2$', r'3 passe devant ; $3-1=2$'),
        (24, r'$7x$', r'$7$', r'1 passe devant ; $1-1=0$'),
        (4, r'$9$', r'$0$', r'exposant 0 : facteur 0')]
for y, a, b, lab in rows:
    box(ax, 2, y, 20, 11, 'sujet', label=a)
    arrow(ax, (24, y + 5.5), (64, y + 5.5), 'varie')
    text(ax, 44, y + 9.5, lab, 'varie', 's')
    box(ax, 66, y, 20, 11, 'resultat', label=b)
save(fig, '62-092')
