import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 14, 48, r'$a$', 'sujet', 'm'); text(ax, 74, 48, r'$a^{\prime}=1+a$', 'resultat', 'm')
for k, (a, b) in enumerate(((0, 1), (1, 0))):
    y = 30 - k * 18
    box(ax, 6, y - 6, 16, 12, 'sujet', label=str(a), size='l')
    arrow(ax, (22, y), (62, y), 'varie')
    text(ax, 42, y + 3, r'$+\ 1$', 'varie', 'm')
    box(ax, 62, y - 6, 16, 12, 'resultat', label=str(b), size='l')
text(ax, 44, 4, '0 et 1 sont échangés', 'resultat', 'm')
save(fig, '80-210')
