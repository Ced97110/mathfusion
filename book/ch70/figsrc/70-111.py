import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
steps = [('sujet', r'1. $y$ remplacé par $s=x^2-1$'), ('fixe', r'2. $(x^2-1)^2=x^4-2x^2+1$'),
         ('fixe', r'3. ajouter $x^2-4$'), ('resultat', r'$x^4-x^2-3$')]
for i, (role, t) in enumerate(steps):
    y = 74 - 21 * i
    box(ax, 10, y, 68, 12, role, label=t, size='s' if i < 3 else 'm')
    if i < 3:
        arrow(ax, (44, y - 0.5), (44, y - 8.5), 'varie', lw=1.1)
text(ax, 44, 4, r'$e=1$ : $2e-3=-1$, $e^2-4e=-3$', 'fixe', 's')
save(fig, '70-111')
