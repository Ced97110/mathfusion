import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,3,38,38,20,'sujet'); text(ax,22,53,'V','sujet','l',weight='bold'); text(ax,22,44,'listes de 2 nombres','sujet','s')
box(ax,47,38,38,20,'autre'); text(ax,66,53,'B','autre','l',weight='bold'); text(ax,66,44,'règle de mesure','autre','s')
arrow(ax,(22,37),(36,22),'resultat'); arrow(ax,(66,37),(52,22),'resultat')
box(ax,24,8,40,14,'resultat',label=r'$(V,\,B)$',size='l',weight='bold')
text(ax,44,3,'les deux vont ensemble','resultat','s')
save(fig,'72-078')
