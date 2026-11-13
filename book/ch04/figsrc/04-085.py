import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,36,69,'3 ×','fixe','l')
text(ax,48,69,r'$x^{2}$','sujet','l')
brace(ax,44,52,65,'varie',label=r'$x^{2} = x \times x$, calculé d’abord',down=True,size='s')
text(ax,44,52,r'$x = 4$','sujet','m')
# trois carrés de 4 × 4 carreaux de 4 mm
for x in (14,36,58):
    poly(ax,[(x,24),(x+16,24),(x+16,40),(x,40)],'sujet')
    for i in (1,2,3):
        line(ax,[(x+4*i,24),(x+4*i,40)],'fixe',lw=0.3)
        line(ax,[(x,24+4*i),(x+16,24+4*i)],'fixe',lw=0.3)
    text(ax,x+8,44,r'$x^{2} = 16$','sujet','m')
brace(ax,14,74,22.5,'resultat',label='3 × 16 = 48',down=True,size='m')
text(ax,44,7,r'avec $x = 5$ : 3 × 25 = 75','autre','s')
save(fig,'04-085')
