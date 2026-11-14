import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, r'$h=H(u,v)$, et $H(w,w)=0$ pour tout $w$', 'encre', 's')
box(ax, 2, 66, 84, 16, 'sujet'); text(ax, 44, 78, '1. développer $H(u+v,\\,u+v)=0$', 'sujet', 's'); text(ax, 44, 70.5, r'$h+\bar h=0$', 'sujet', 'm')
box(ax, 2, 40, 84, 20, 'varie', lw=1.8); text(ax, 44, 55, r'2. remplacer $u$ par $iu$ : l’étape clé', 'varie', 's', weight='bold'); text(ax, 44, 46, r'$ih-i\bar h=0$, donc $h=\bar h$', 'varie', 'm')
box(ax, 2, 18, 84, 16, 'resultat'); text(ax, 44, 30, '3. les deux ensemble', 'resultat', 's'); text(ax, 44, 22.5, r'$2h=0$, donc $h=0$', 'resultat', 'm')
arrow(ax, (44, 65), (44, 61), 'fixe'); arrow(ax, (44, 39), (44, 35), 'fixe')
box(ax, 2, 2, 84, 11, 'limite', fill=False, dash=True, label=r'sans l’étape 2 : $h=i$ passerait', size='s')
save(fig, '75-158')
