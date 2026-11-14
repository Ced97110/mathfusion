import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x, s, r in ((20, '12 =', 'encre'), (34, '2', 'sujet'), (41, '×', 'encre'), (48, '2', 'sujet'), (55, '×', 'encre'), (62, '3', 'autre')):
    text(ax, x, 58, s, r, 'xl', weight='bold')
brace(ax, 31, 51, 52, 'sujet', label='2² = 4')
brace(ax, 59.5, 64.5, 52, 'autre', label='3')
def clock(cx, cy, n, role):
    for h in range(n):
        a = math.radians(90 - 360 * h / n)
        disc(ax, cx + 6 * math.cos(a), cy + 6 * math.sin(a), 2.2, role)
clock(41, 28, 4, 'sujet'); clock(62, 28, 3, 'autre')
arrow(ax, (41, 43), (41, 37), 'fixe'); arrow(ax, (62, 43), (62, 37), 'fixe')
text(ax, 41, 14, 'ℤ/2²\n4 positions', 'sujet', 's'); text(ax, 62, 14, 'ℤ/3\n3 positions', 'autre', 's')
text(ax, 44, 3.5, 'chaque morceau : un seul premier', 'encre', 's')
save(fig, '60-028')
