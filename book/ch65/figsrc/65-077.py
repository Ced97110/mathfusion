import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, 'ordre : multiple de 4 qui divise 24', 'encre', 's')
rows = [(r'$S_4$', 24, 'sujet'), (r'$A_4$', 12, 'sujet'), (r'$D$', 8, 'sujet'), (r'$V$', 4, 'autre'), (r'$C$', 4, 'autre')]
y = 54
for name, n, role in rows:
    text(ax, 6, y + 4, name, role, 'm')
    box(ax, 14, y, n * 2.2, 8, role, r=0.6)
    text(ax, 14 + n * 2.2 + 3, y + 4, f'{n} éléments', role, 's', ha='left')
    y -= 12
save(fig, '65-077')
