import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs = (3, 33, 63)
W_, H_ = 22, 13
text(ax, 44, 76, r'$S$ deux fois : $(x\,;\,y)\mapsto(x+2y\,;\,y)$', 'encre', 's', weight='bold')
for i, t in enumerate(('$(x\\,;\\,y)$\n(2 ; 3)', '$(x+y\\,;\\,y)$\n(5 ; 3)', '$(x+2y\\,;\\,y)$\n(8 ; 3)')):
    box(ax, xs[i], 50, W_, H_, 'sujet' if i < 2 else 'resultat', label=t, size='s')
for i in range(2):
    arrow(ax, (xs[i] + W_ + 0.8, 56.5), (xs[i + 1] - 0.8, 56.5), 'varie', lw=1.2)
    text(ax, xs[i] + W_ + 4, 60.5, '$S$', 'varie', 's')
text(ax, 44, 38, r'image moins départ : $S-1$', 'encre', 's', weight='bold')
for i, t in enumerate(('$(x\\,;\\,y)$\n(2 ; 3)', '$(y\\,;\\,0)$\n(3 ; 0)', '(0 ; 0)\n(0 ; 0)')):
    box(ax, xs[i], 14, W_, H_, 'sujet' if i < 2 else 'resultat', label=t, size='s')
for i in range(2):
    arrow(ax, (xs[i] + W_ + 0.8, 20.5), (xs[i + 1] - 0.8, 20.5), 'varie', lw=1.2)
    text(ax, xs[i] + W_ + 4, 24.5, '$S-1$', 'varie', 's')
text(ax, 44, 5, r'deux fois : $(S-1)^2=0$ pour tout couple', 'resultat', 's', weight='bold')
save(fig, '57-200')
