import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x0 = 26
for i, b in enumerate('0110'):
    box(ax, x0 + i * 15, 44, 12, 9, 'sujet', label=b, size='l')
for i, b in enumerate('0010'):
    box(ax, x0 + i * 15, 12, 12, 9, 'varie' if i == 1 else 'fixe', label=b, size='l')
text(ax, 2, 48.5, 'Sonde\nenvoie', 'sujet', 'm', ha='left')
text(ax, 2, 16.5, 'Terre\nreçoit', 'encre', 'm', ha='left')
arrow(ax, (47, 43.5), (47, 21.8), 'varie', lw=1.4)
text(ax, 50, 33, 'parasite :\nle bruit', 'varie', 'm', ha='left')
text(ax, 47, 6, 'bit 2 inversé', 'varie', 's')
text(ax, 72, 6, 'autres bits : justes', 'fixe', 's')
save(fig, '68-001')
