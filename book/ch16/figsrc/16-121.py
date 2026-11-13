import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for cx, head, a, b, c in [(23, 'inconnue : largeur', r'$w$ = 3', r'longueur $w$ + 4 = 7', ''),
                          (65, 'inconnue : longueur', r'$x$ = 7', r'largeur $x$ − 4 = 3', '')]:
    text(ax, cx, 75, head, 'varie', 'm', weight='bold')
    box(ax, cx - 20, 52, 40, 12, 'sujet', label=(r'4$w$ + 8 = 20' if cx < 44 else r'4$x$ − 8 = 20'), size='m')
    arrow(ax, (cx, 52), (cx, 44), 'varie')
    box(ax, cx - 20, 32, 40, 11, 'sujet', label=a, size='m')
    arrow(ax, (cx, 32), (cx, 25), 'varie')
    text(ax, cx, 21, b, 'sujet', 's')
box(ax, 14, 3, 60, 10, 'resultat', label='même jardin : 7 m sur 3 m', size='m')
arrow(ax, (23, 19), (30, 13.5), 'resultat')
arrow(ax, (65, 19), (58, 13.5), 'resultat')
save(fig, '16-121')
