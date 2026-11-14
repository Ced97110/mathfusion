import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [(66, 'sujet', r'$f_0=x^3-3x+1$'),
        (48, 'sujet', r"$f_1=f'=3x^2-3$"),
        (30, 'fixe', r'reste $r=-2x+1$'),
        (12, 'resultat', r'$f_2=-r=2x-1$')]
for y, role, lab in rows:
    box(ax, 14, y, 60, 10, role, label=lab)
steps = ['dériver', r'diviser $f_0$ par $f_1$', 'changer le signe']
for k, s in enumerate(steps):
    y = rows[k][0]
    arrow(ax, (44, y), (44, y - 8), 'varie')
    text(ax, 47, y - 4, s, 'varie', 's', ha='left')
save(fig, '69-070')
