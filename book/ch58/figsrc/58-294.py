import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, 'famille génératrice : la base', 'sujet', 's')
box(ax, 16, 64, 26, 10, 'sujet', label='(1, 0)')
box(ax, 46, 64, 26, 10, 'sujet', label='(0, 1)')
brace(ax, 16, 72, 64, 'sujet', label='2 vecteurs')
text(ax, 44, 47, 'indépendante ≤ génératrice', 'fixe', 's')
text(ax, 44, 41, 'famille de trois vecteurs', 'autre', 's')
for i, lab in enumerate(['(1, 2)', '(3, 1)', '(2, 5)']):
    box(ax, 4 + i * 28.5, 27, 26, 10, 'autre', label=lab)
brace(ax, 4, 87, 27, 'autre', label='3 vecteurs')
box(ax, 14, 3, 60, 10, 'varie', label='3 > 2 : famille liée')
save(fig, '58-294')
