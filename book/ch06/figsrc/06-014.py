import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for r in range(4):
    y = 14 + r * 6.4
    for c in range(3):
        box(ax, 6 + c * 6.2, y, 5.6, 5.6, 'sujet', r=0.3)
    text(ax, 26, y + 2.8, '3/4', 'sujet', 's', ha='left')
text(ax, 40, 26, '=', 'encre', 'l')
for r in range(3):
    for c in range(4):
        box(ax, 50 + c * 6.2, 17.2 + r * 6.4, 5.6, 5.6, 'sujet', r=0.3)
text(ax, 18, 45, '4 fois 3/4', 'sujet')
text(ax, 63, 45, '3 tablettes', 'sujet')
text(ax, 44, 6, '12 quarts des deux côtés', 'resultat')
save(fig, '06-014')
