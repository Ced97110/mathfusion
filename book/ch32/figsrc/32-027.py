import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
data = [(52, r'$\sin\,\theta=0{,}5$', 'rien autour de l’angle'), (32, r'$2\cos\,3x=1$', 'un facteur 3 dans l’angle'),
        (12, r'$\cos^2 x+2\cos x+1=0$', 'un carré et une somme')]
for y, eq, tg in data:
    box(ax, 2, y, 44, 14, 'sujet', label=eq, size='m'); box(ax, 49, y, 37, 14, 'varie', label=tg, size='s')
text(ax, 44, 5, 'inconnue dans sin ou cos', 'resultat', 's')
save(fig, '32-027')
