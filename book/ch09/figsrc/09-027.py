import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 31, 80, 'même nature', 'sujet', 's', weight='bold'); text(ax, 69, 80, 'natures différentes', 'autre', 's', weight='bold')
text(ax, 4, 59, 'soustraction', 'encre', 's', rot=90); text(ax, 4, 22, 'division', 'encre', 's', rot=90)
for i in range(8):
    box(ax, 14 + i * 4, 60, 4, 6, 'varie' if i >= 5 else 'sujet', r=0.3, lw=0.6)
text(ax, 31, 53, '8 miles − 3 miles = 5', 'resultat', 's')
box(ax, 52, 50, 34, 18, 'limite')
text(ax, 69, 62, '8 miles − 5 gallons', 'limite', 's')
text(ax, 69, 55, 'impossible', 'limite', 's', weight='bold')
line(ax, [(8, 42), (86, 42)], 'fixe', lw=0.5)
for i in range(4):
    box(ax, 14 + i * 8, 26, 7, 6, 'sujet', r=0.3, lw=0.6)
text(ax, 31, 19, '8 miles ÷ 2 miles = 4', 'resultat', 's')
box(ax, 52, 8, 34, 28, 'resultat')
text(ax, 69, 29, '8 miles ÷ 5 gallons', 'resultat', 's')
text(ax, 69, 22, '= 1,6 mile par gallon', 'resultat', 's', weight='bold')
text(ax, 69, 14, 'possible', 'resultat', 's')
save(fig, '09-027')
