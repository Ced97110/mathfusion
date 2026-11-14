import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 2, 2, 84, 54, 'resultat', r=1.2)
text(ax, 5, 52, 'constructibles', 'resultat', 's', ha='left', weight='bold')
box(ax, 6, 6, 32, 34, 'sujet', r=1.2)
text(ax, 9, 36, 'rationnels ℚ', 'sujet', 's', ha='left', weight='bold')
text(ax, 22, 20, 'fractions', 'sujet', 's')
for yy, t in [(40, '√2 ≈ 1,414 : degré 2'), (22, 'cos 72° ≈ 0,309 : degré 2')]:
    disc(ax, 46, yy, 1.4, 'varie')
    text(ax, 49, yy, t, 'varie', 's', ha='left')
save(fig, '66-113')
