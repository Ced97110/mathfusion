import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [('on réduit 9215', r'$9215=94\times98+3$', 'sujet'),
        ('inverse de 3', r'$3\times33=99=98+1$', 'varie'),
        ('écart des restes', r'$30-46=-16\equiv82$', 'varie'),
        ('coefficient', r'$82\times33=2706$, reste $60$', 'varie'),
        ('résultat', r'$5044+60\times9215=557\,944$', 'resultat')]
for i, (cap, s, role) in enumerate(rows):
    y = 69 - i * 15
    text(ax, 2, y + 4.5, cap, 'fixe', 's', ha='left')
    box(ax, 30, y, 56, 9, role, label=s)
    if i < 4: arrow(ax, (58, y), (58, y - 6), 'fixe')
save(fig, '52-258')
