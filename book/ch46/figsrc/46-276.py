import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,8,68,38,-12,24,step=12,arrow_right=False,size='m',tick=1.4)
text(ax,80,38,r'$\mathbb{Z}$','encre','l')
for v in (-12,0,12,24):
    disc(ax,f(v),38,2.2,'varie')
    arrow(ax,(f(v),33.5),(44,19),'varie',curve=0.0)
disc(ax,44,13,5.5,'sujet',label='0 h')
text(ax,44,52,r'multiples de 12 : $12\mathbb{Z}$','varie','m')
text(ax,44,4,'même heure sur l’horloge','sujet','s')
save(fig,'46-276')
