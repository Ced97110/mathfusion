import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$g$ s’annule en 4 puissances', 'sujet', 'm', weight='bold')
for i, s in enumerate([r'$\omega$', r'$\omega^2$', r'$\omega^3$', r'$\omega^4$']):
    box(ax, 15 + i * 17, 50, 14, 8, 'sujet', label=s, size='l')
brace(ax, 15, 80, 49, 'sujet', 'racines consécutives')
# deux choix de g : même longueur de mot, partie contrôle (= degré) plus ou moins grande
text(ax, 44, 38.5, 'degré grand : peu de message', 'fixe', 's')
box(ax, 6, 28, 52, 7, 'varie', label='contrôle', size='s', r=0.4)
box(ax, 58, 28, 24, 7, 'resultat', label='message', size='s', r=0.4)
text(ax, 44, 20.5, 'degré petit : méthode BCH', 'sujet', 's', weight='bold')
box(ax, 6, 10, 26, 7, 'varie', label='contrôle', size='s', r=0.4)
box(ax, 32, 10, 50, 7, 'resultat', label='message', size='s', r=0.4)
text(ax, 44, 4, 'degré = bits de contrôle', 'fixe', 's')
save(fig, '68-209')
