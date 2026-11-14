import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
box(ax, 4, 82, 38, 9, 'fixe', label='3 planches de 2,35 m', size='s'); box(ax, 46, 82, 38, 9, 'fixe', label='4,20 euros le mètre', size='s')
rows = [(62, 'longueur (m)', r'$3\times2{,}35=7{,}05$', 'sujet'), (40, 'prix (euros)', r'$7{,}05\times4{,}20=29{,}61$', 'varie'),
        (18, 'monnaie (euros)', r'$50-29{,}61=20{,}39$', 'resultat')]
for y, lab, calc, r in rows:
    text(ax, 3, y + 5, lab, r, 's', ha='left')
    box(ax, 30, y, 54, 10, r, label=calc, size='m')
for y in (52, 30):
    arrow(ax, (57, y - 0.5 + 0.5), (57, y - 10.5 + 0.5 + 10 - 10 + 0), r) if False else None
arrow(ax, (57, 80), (57, 73), 'fixe')
arrow(ax, (57, 61), (57, 51), 'fixe'); arrow(ax, (57, 39), (57, 29), 'fixe')
save(fig, '08-063')
