import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# n = 3 : 3 x 2 x 1 = 6 carrés
text(ax, 2, 69, r'$S_3$ : $3\times2\times1=6$', 'sujet', 'm', ha='left')
for i in range(6):
    box(ax, 4 + i * 6.5, 56, 5, 8, 'sujet')
# n = 4 : 4 groupes de 6
text(ax, 2, 47, r'$S_4$ : $4\times6=24$', 'sujet', 'm', ha='left')
for g in range(4):
    for i in range(6):
        box(ax, 4 + g * 21 + i * 3.2, 34, 2.8, 8, 'sujet', r=0.3)
# n = 5 : 5 blocs de 24
text(ax, 2, 25, r'$S_5$ : $5\times24=120$', 'sujet', 'm', ha='left')
for g in range(5):
    box(ax, 4 + g * 16.5, 6, 14, 12, 'sujet', label='24', size='s')
save(fig, '65-028')
