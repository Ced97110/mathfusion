import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(38)
y = 14
box(ax, 2, y - 4.5, 18, 9, 'fixe', label=r'$m = 1001$')
arrow(ax, (21, y), (33, y), 'sujet', lw=1.3)
text(ax, 27, y + 3.8, r'$G$', 'sujet', 'l', weight='bold')
box(ax, 34, y - 4.5, 26, 9, 'sujet', label=r'$c = 0011001$')
arrow(ax, (61, y), (71, y), 'autre', lw=1.3)
text(ax, 66, y + 3.8, r'$H$', 'autre', 'l', weight='bold')
box(ax, 72, y - 4.5, 15, 9, 'resultat', label=r'$Hc = 0$')
brace(ax, 2, 60, y + 7, 'sujet', label='émission : G fabrique', down=False, depth=1.8)
brace(ax, 62, 87, y + 7, 'autre', label='H reconnaît', down=False, depth=1.8)
crop(fig, ax, 6.4, 29.1)
save(fig, '68-137')
