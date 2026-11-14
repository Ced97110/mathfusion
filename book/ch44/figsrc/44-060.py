import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, '« 3 est élément de ℕ »', 'encre', 'm', weight='bold')
disc(ax, 14, 31, 6, 'sujet', label='3', size='l')
text(ax, 14, 19, 'objet', 'sujet', 's')
text(ax, 34, 31, '∈', 'varie', 'xl', weight='bold')
box(ax, 46, 16, 40, 30, 'fixe', fill=False, dash=True)
text(ax, 66, 41, 'ℕ', 'fixe', 'l', weight='bold')
for k, lab in enumerate(['0', '1', '2', '3']):
    disc(ax, 52 + 8*k, 29, 3.3, 'sujet' if lab == '3' else 'fixe', label=lab, size='s')
text(ax, 83, 29, '…', 'fixe', 'm')
text(ax, 66, 11, 'collection', 'fixe', 's')
save(fig, '44-060')
