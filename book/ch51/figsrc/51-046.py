import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
disc(ax, 22, 31, 19, 'fixe')
text(ax, 22, 47, '$R$', 'fixe', 'l')
disc(ax, 13, 30, 4.2, 'sujet', label='$a$', size='m')
disc(ax, 30, 37, 4.2, 'fixe', label='$b$', size='m')
disc(ax, 28, 21, 4.2, 'fixe', label='$c$', size='m')
for y, s, role, cap in [(48, '$a$', 'sujet', 'l’élément'), (31, '∈', 'varie', 'est dans'), (14, '$R$', 'fixe', 'l’ensemble')]:
    box(ax, 48, y - 5, 12, 10, role, label=s, size='l')
    text(ax, 63, y, cap, role, 's', ha='left')
save(fig, '51-046')
