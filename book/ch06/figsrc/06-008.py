import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 14, 46, 60, 7, 'sujet')
brace(ax, 14, 74, 53, 'sujet', r'$U$ = la barre entière (1)', down=False, size='m')
for j in range(4):
    box(ax, 14 + j * 15, 26, 15, 7, 'sujet', r=0.3)
brace(ax, 14, 74, 33, 'sujet', r'$U$ coupée en 4', down=False, size='m')
for j in range(8):
    box(ax, 14 + j * 7.5, 6, 7.5, 7, 'sujet', r=0.3)
brace(ax, 14, 74, 13, 'sujet', r'$U$ coupée en 8', down=False, size='m')
save(fig, '06-008')
