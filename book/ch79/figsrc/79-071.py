import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
ys = [6, 22, 38, 54]
for yy, s in zip(ys, ['2', '4', '8', '16']):
    box(ax, 8, yy, 14, 9, 'sujet', label=s)
for yy in ys[:-1]: arrow(ax, (15, yy + 9), (15, yy + 16), 'fixe')
arrow(ax, (15, 63), (15, 66), 'fixe')
text(ax, 15, 70, '…', 'sujet', 'l')
arrow(ax, (15, 74), (15, 80), 'limite')
box(ax, 8, 80, 14, 11, 'limite', label='?')
text(ax, 27, 85, 'aucun multiple commun', 'limite', 's', ha='left')
text(ax, 15, 96, 'liste infinie', 'sujet', 's')
text(ax, 72, 70, 'toute paire a un sup', 'resultat', 's')
box(ax, 58, 48, 28, 11, 'resultat', label='PPCM de 4 et 8 : 8', size='s')
box(ax, 58, 30, 28, 11, 'resultat', label='PGCD de 4 et 8 : 4', size='s')
save(fig, '79-071')
