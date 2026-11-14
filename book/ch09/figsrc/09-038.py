import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'taux : deux natures différentes', 'encre', 'm', weight='bold')
for y, a, b in [(36, '30 miles', '2 gallons'), (12, '12 litres', '3 minutes')]:
    box(ax, 6, y, 30, 12, 'sujet', label=a)
    text(ax, 44, y + 6, r'$\div$', 'fixe', 'l')
    box(ax, 52, y, 30, 12, 'autre', label=b)
save(fig, '09-038')
