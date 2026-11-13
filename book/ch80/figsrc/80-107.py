import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
box(ax,3,6,82,56,'sujet',label=None,dash=True); text(ax,44,57,'applications semi-linéaires','sujet','m')
box(ax,8,16,34,32,'resultat',label=None); text(ax,25,43,'linéaires','resultat','m'); text(ax,25,34,r'$\sigma$ = identité','resultat','s'); text(ax,25,24,r'$\sigma(a)=a$','resultat','s')
box(ax,48,16,34,32,'varie',label=None); text(ax,65,43,'conjugaison','varie','m'); text(ax,65,34,r'$\sigma\neq$ identité','varie','s'); text(ax,65,24,r'$\sigma(a+bi)=a-bi$','varie','s')
save(fig,'80-107')
