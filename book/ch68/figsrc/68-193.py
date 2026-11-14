import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 91, r'$g = 1 + x$', 'sujet', 'm', weight='bold')
w = '1100000'
assert w.count('1') % 2 == 0
cw, x0 = 6, 23
text(ax, 2, 80, r'ex. $1 + x$', 'sujet', 's', ha='left')
for i, c in enumerate(w):
    box(ax, x0 + i * cw, 77, cw, 6.5, 'sujet' if c == '1' else 'fixe', label=c, r=0.5, size='s')
steps = [('un multiple de $g$ s’annule en $x = 1$', 'sujet'),
         ('somme des coefficients = 0', 'resultat'),
         ('nombre pair de 1', 'resultat'),
         ('c’est le code du bit de parité', 'resultat')]
for k, (s, r) in enumerate(steps):
    y = 56 - 17 * k
    box(ax, 8, y, 72, 9, r, label=s, size='s')
    if k < 3:
        arrow(ax, (44, y - 0.5), (44, y - 7.5), 'varie')
arrow(ax, (44, 76), (44, 66.5), 'varie')
text(ax, 62, 71.5, 'en $x = 1$ : $1 + 1 = 0$', 'resultat', 's')
save(fig, '68-193')
