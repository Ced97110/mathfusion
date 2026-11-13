import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def cell(x, y, t, role): box(ax, x, y, 7, 8, role, label=t, size='l', r=0.4)
box(ax, 4, 54, 5, 5, 'sujet', r=0.3); text(ax, 11, 56.5, 'chiffre significatif : connu', 'sujet', 's', ha='left')
box(ax, 4, 46, 5, 5, 'fixe', r=0.3); text(ax, 11, 48.5, 'zéro : on ne sait pas', 'fixe', 's', ha='left')
y = 32
for i, d in enumerate('4000'): cell(4 + 8 * i, y, d, 'sujet' if i == 0 else 'fixe')
text(ax, 42, y + 4, 'combien sont connus ?', 'limite', 's', ha='left')
y = 18
cell(4, y, '4', 'sujet'); box(ax, 12, y, 18, 8, 'varie', label=r'$\times\,10^3$', size='m', r=0.4)
text(ax, 42, y + 4, '1 chiffre significatif', 'resultat', 's', ha='left')
y = 4
cell(4, y, '4', 'sujet'); cell(12, y, '3', 'sujet'); box(ax, 20, y, 18, 8, 'varie', label=r'$\times\,10^3$', size='m', r=0.4)
text(ax, 42, y + 4, '2 chiffres significatifs', 'resultat', 's', ha='left')
save(fig, '10-094')
