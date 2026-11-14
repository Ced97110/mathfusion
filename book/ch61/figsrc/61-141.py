import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(96)
box(ax,2,72,36,20,'sujet',label='$F$ algébriquement\nclos',size='s')
box(ax,50,72,36,20,'sujet',label='tout polynôme =\nfacteurs de degré 1',size='s')
arrow(ax,(38,82),(50,82),'fixe',both=True); text(ax,44,88,'⇔','fixe','m')
box(ax,2,42,36,20,'varie',label='racine $a$ : $x-a$\ndivise $f$',size='s')
box(ax,50,42,36,20,'varie',label='facteur $ax-b$ :\nracine $b/a$',size='s')
arrow(ax,(20,72),(20,62),'varie'); arrow(ax,(68,72),(68,62),'varie')
text(ax,44,38,'','encre','s') if False else None
box(ax,2,16,50,14,'resultat',label=r'ℂ : $x^2+1=(x-i)(x+i)$',size='s')
box(ax,58,16,28,14,'limite',label='ℝ : pas ainsi',size='s')
save(fig,'61-141')
