import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for j in range(4):
    box(ax, 14 + j * 15, 24, 15, 10, 'sujet' if j < 3 else 'fixe', r=0.3)
brace(ax, 14, 59, 36, 'autre', '0,75 (calculatrice)', down=False, size='m')
brace(ax, 14, 59, 24, 'sujet', '3/4 de tablette', down=True, size='m')
text(ax, 44, 8, 'une part, deux écritures', 'encre')
save(fig, '06-005')
