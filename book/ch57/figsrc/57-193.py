import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cx, cy, u = 22, 38, 8.0
O = (cx, cy)
Pt = lambda x, y: (cx + x * u, cy + y * u)
line(ax, [(cx - 16, cy), (cx + 16, cy)], 'fixe', lw=0.6)
line(ax, [(cx, cy - 20), (cx, cy + 20)], 'fixe', lw=0.6)
arrow(ax, O, Pt(-0.8, 2), 'varie', lw=1.5)
arrow(ax, O, Pt(0.8, -2), 'varie', lw=1.5)
text(ax, 15, 61, r'$Tv=(-0{,}8\,;\,2)$', 'varie', 's')
text(ax, 29, 14, r'$T^3v=(0{,}8\,;\,-2)$', 'varie', 's')
text(ax, 22, 5, 'leur somme : (0 ; 0)', 'resultat', 's')
# les multiples de x² + 1
text(ax, 66, 66, r'multiples de $x^2+1$', 'sujet', 's')
box(ax, 48, 50, 38, 9, 'sujet', label=r'$g=1$ : $x^2+1$', size='s')
box(ax, 48, 36, 38, 9, 'varie', label=r'$g=x$ : $x^3+x$', size='s')
box(ax, 48, 22, 38, 9, 'sujet', label=r'$g$ quelconque : $(x^2+1)g$', size='s')
text(ax, 67, 14, 'tous envoient v sur (0 ; 0)', 'resultat', 's')
save(fig, '57-193')
