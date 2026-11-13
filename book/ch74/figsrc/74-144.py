import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = ['F  F  F  F  F  F', 'b  p  b  p  b  p', 'V  V  V  V  V  V', 'D  D  D  D  D  D',
        'N  N  N  N  N  N', 'H  H  H  H  H  H', 'V  Λ  V  Λ  V  Λ']
for k, s in enumerate(rows):
    y = 71 - k*10.2
    box(ax, 3, y-4, 62, 8, 'sujet')
    text(ax, 34, y, s, 'sujet', 'm')
line(ax, [(68, 75), (70, 75), (70, 7), (68, 7)], 'resultat', lw=1.0)
text(ax, 79, 46, '7', 'resultat', 'xl', weight='bold')
text(ax, 79, 38, 'groupes', 'resultat', 's')
save(fig, '74-144')
