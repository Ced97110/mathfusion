import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 1, 2, 41, 74, 'sujet', fill=False, dash=True)
box(ax, 46, 2, 41, 74, 'autre', fill=False, dash=True)
text(ax, 21.5, 70, 'ann $x$ = 0', 'sujet', 'm', weight='bold')
text(ax, 46 + 20.5, 70, r'ann $x$ = $n$ℤ, ici $n$ = 3', 'autre', 's', weight='bold')
text(ax, 21.5, 63, 'couples, $x$ = (2 ; 1)', 'sujet', 's')
text(ax, 66.5, 63, 'horloge, $x$ = 4 h', 'autre', 's')
# gauche : les multiples de x ne reviennent jamais à 0
for i, t in enumerate(['(0 ; 0)', '(2 ; 1)', '(4 ; 2)']):
    y = 51 - i * 9
    disc(ax, 15, y, 3.3, 'sujet')
    text(ax, 15 + 5, y, t, 'sujet', 's', ha='left')
    if i: arrow(ax, (15, y + 5.6), (15, y + 3.5), 'varie', lw=0.9)
text(ax, 15, 24, '⋮', 'sujet', 'm')
# droite : les multiples de x font le tour et reviennent à 0
cx, cy, r = 66.5, 42, 11
for k, t in enumerate(['0', '4 h', '8 h']):
    a = math.radians(90 - 120 * k)
    disc(ax, cx + r * math.cos(a), cy + r * math.sin(a), 3.6, 'autre', label=t, size='s')
for k in range(3):
    a0 = math.radians(90 - 120 * k); a1 = math.radians(90 - 120 * (k + 1))
    arrow(ax, (cx + r * math.cos(a0 - math.radians(24)), cy + r * math.sin(a0 - math.radians(24))),
          (cx + r * math.cos(a1 + math.radians(24)), cy + r * math.sin(a1 + math.radians(24))), 'varie', lw=0.9, curve=-0.2)
# conséquences
arrow(ax, (21.5, 20), (21.5, 15.5), 'varie', lw=1.1)
arrow(ax, (66.5, 24.5), (66.5, 15.5), 'varie', lw=1.1)
box(ax, 5, 3.5, 33, 12, 'resultat', label='infini : comme ℤ', size='s', weight='bold')
box(ax, 50, 3.5, 33, 12, 'resultat', label='3 éléments : ℤ/3ℤ', size='s', weight='bold')
save(fig, '57-169')
