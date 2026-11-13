import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$k=12$ : classes 1, 5, 7, 11','sujet','m')
text(ax,44,52,r'exposant $\varphi(12)=4$','varie','s')
for y,a,pw,q in [(32,5,625,52),(10,7,2401,200)]:
    box(ax,2,y,26,11,'sujet',label=rf'${a}^4={pw}$'.replace('625','625').replace('2401','2\\,401'),size='s')
    arrow(ax,(28,y+5.5),(36,y+5.5),'varie')
    box(ax,36,y,28,11,'fixe',label=rf'${q}\times12+1$',size='s')
    arrow(ax,(64,y+5.5),(70,y+5.5),'varie')
    box(ax,70,y,16,11,'resultat',label='reste 1',size='s')
save(fig,'52-091')
