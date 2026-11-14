import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cy = 38
for h in range(12):
    a = math.radians(90 - 30 * h)
    disc(ax, 15 + 9 * math.cos(a), cy + 9 * math.sin(a), 1.7, 'sujet')
def grid(x0, n, m, cw, ch):
    for i in range(n):
        for j in range(m):
            box(ax, x0 + j * cw + 0.25, cy - n * ch / 2 + i * ch + 0.25, cw - 0.5, ch - 0.5, 'sujet', r=0.4)
grid(44 - 8.25, 4, 3, 5.5, 5.5)
grid(73 - 12.6, 2, 6, 4.2, 4.2)
for x, lab in ((15, 'horloge'), (44, 'grille 4 × 3'), (73, 'grille 2 × 6')):
    text(ax, x, 21, '12', 'sujet', 'xl', weight='bold'); text(ax, x, 14, lab, 'encre', 's')
text(ax, 44, 5, '12, 12, 12 : même comptage', 'varie', 's')
save(fig, '60-011')
