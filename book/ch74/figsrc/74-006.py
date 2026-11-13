import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 84, 'sept bandes, sept façons', 'sujet', 'l')
rows = ['F  F  F  F', 'H  H  H  H', 'N  N  N  N', 'V  V  V  V', 'D  D  D  D', 'b  p  b  p', 'V  Λ  V  Λ']
for i, s in enumerate(rows):
    y = 70 - i * 9.3
    box(ax, 12, y - 3.6, 64, 7.8, 'sujet' if i < 5 else 'autre')
    text(ax, 44, y + 0.3, s, 'sujet' if i < 5 else 'autre', 'l', weight='bold')
arrow(ax, (14, 2.5), (78, 2.5), 'varie', lw=1.2)
text(ax, 44, 6.8, 'direction de la bande', 'varie', 's')
save(fig, '74-006')
