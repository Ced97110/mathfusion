import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
for i in range(12):
    box(ax, 8 + i * 6, 26, 6, 10, 'sujet' if i < 9 else 'fixe', r=0.3)
for k in range(1, 4):
    line(ax, [(8 + k * 18, 24.8), (8 + k * 18, 37.2)], 'encre', lw=1.4)
brace(ax, 8, 80, 36, 'fixe', r'$U$ = 1 : 12 carreaux', down=False, size='m')
for k in range(4):
    brace(ax, 9 + k * 18, 8 + (k + 1) * 18 - 1, 26, 'fixe', '3 carreaux')
brace(ax, 8, 62, 17, 'sujet', '3 parts : 9 carreaux sur 12', size='m')
save(fig, '06-006')
