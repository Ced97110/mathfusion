import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 4, 62, 80, 16, 'sujet', size='s',
    label=r'départ : module sur ℤ/6ℤ' + '\n' + r'$\bar{6}$ = 6 classes de 1, agit comme $6x$')
arrow(ax, (44, 61.5), (44, 55.5), 'fixe')
box(ax, 4, 41, 80, 14, 'varie', lw=1.8, size='m', weight='bold',
    label=r'étape décisive : $\bar{6}=\bar{0}$')
arrow(ax, (44, 40.5), (44, 34.5), 'fixe')
box(ax, 4, 20, 80, 14, 'resultat', size='m', weight='bold',
    label=r'$6x=\bar{6}x=\bar{0}x=0$ pour tout $x$')
line(ax, [(4, 15), (84, 15)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 10, r'réciproque : $\bar{4}=\overline{10}$ (écart 6)', 'fixe', 's')
text(ax, 44, 4, r'4·1 et 10·1 valent 1 modulo 3', 'fixe', 's')
save(fig, '57-207')
