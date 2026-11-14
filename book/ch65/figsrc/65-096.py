import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, 'trois sortes de lettres', 'encre', 'm')
rows = [('fixe', 'fixe', True, '2 et 1/3 : valeur connue'),
        ('varie', 'varie', False, r'$x-5=0$ : valeur à trouver'),
        ('sujet', 'sujet', False, r'$t_1,\ t_2$ : ni l’une ni l’autre')]
for j, (role, grole, solid, lab) in enumerate(rows):
    y = 50 - j * 15
    disc(ax, 9, y + 5, 3.2, grole, fill=solid)
    box(ax, 17, y, 69, 10, role, label=lab, size='s')
box(ax, 8, 4, 72, 11, 'resultat', label=r'$(t_1^2+1)/t_2$ est dans $F(t_1, t_2)$', size='s')
arrow(ax, (44, 19), (44, 16), 'varie')
save(fig, '65-096')
