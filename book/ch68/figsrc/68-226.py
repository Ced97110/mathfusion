import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'le compte suffit-il ?', 'encre', 'm', weight='bold')
text(ax, 58, 50, 'compte juste', 'fixe', 's')
text(ax, 78, 50, 'mots existent', 'fixe', 's')
rows = [(38, r'7 bits : 16 mots, $d=3$', True), (26, r'23 bits : $2^{12}$ mots, $d=7$', False),
        (14, r'90 bits : $2^{78}$ mots, $d=5$', False)]
for y, lab, ok in rows:
    text(ax, 3, y, lab, 'encre', 's', ha='left')
    disc(ax, 58, y, 4.2, 'resultat', label=r'$\checkmark$', size='m')
    if ok: disc(ax, 78, y, 4.2, 'resultat', label=r'$\checkmark$', size='m')
    else: disc(ax, 78, y, 4.2, 'varie', label='?', size='m')
save(fig, '68-226')
