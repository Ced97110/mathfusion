import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,'même reste 5 par 12','resultat','m')
f=numberline(ax,6,76,24,0,36,step=12,arrow_right=False)
for v in (5,17,29): disc(ax,f(v),24,3,'sujet',label=str(v),size='s')
for a,b in ((5,17),(17,29)):
    arrow(ax,(f(a),27.5),(f(b),27.5),'varie',curve=-0.5)
    text(ax,(f(a)+f(b))/2,35,'+12','varie','s')
text(ax,44,8,r'$29\equiv17\equiv5\ (\mathrm{mod}\ 12)$','sujet','l')
save(fig,'52-092')
