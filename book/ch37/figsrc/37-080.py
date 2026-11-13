import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
for i in range(3):
    for j in range(3):
        box(ax, 8 + 9*i, 10 + 9*j, 9, 9, 'sujet', r=0.3)
text(ax, 21.5, 23.5, 'aire 9', 'sujet', 'l', weight='bold')
brace(ax, 8, 35, 10, 'sujet', label='3')
arrow(ax, (39, 10), (39, 37), 'sujet', both=True)
text(ax, 42.5, 23.5, '3', 'sujet', 'l')
text(ax, 68, 38, r'$\sqrt{9}=3$', 'resultat', 'l')
text(ax, 68, 31, 'car 3 × 3 = 9', 'encre', 'm')
text(ax, 68, 21, 'dans le champ :', 'fixe', 'm')
text(ax, 68, 14, r'$\sqrt{984\,375}\approx 992{,}2$', 'resultat', 'm')
save(fig, '37-080')
