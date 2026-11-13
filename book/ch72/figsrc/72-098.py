import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
b=14; base=14
def bar(x,y0,y1,role,lab,val):
    poly(ax,[(x,y0),(x+14,y0),(x+14,y1),(x+14*0,y1)],role)
    text(ax,x+7,(y0+y1)/2,val,role,'l')
    text(ax,x+7,base-5,lab,role,'s')
u=7
bar(6,base,base+5*u,'sujet',r'$B(x,x)$','5')
bar(26,base+u,base+5*u,'varie',r'$-2cB(x,u)$','−4')
bar(46,base+u,base+5*u,'varie',r'$+c^2B(u,u)$','+4')
bar(66,base,base+5*u,'resultat','résultat','5')
for xx in (20,40,60): line(ax,[(xx,base+5*u),(xx+6,base+5*u)],'fixe',dash=True)
line(ax,[(40,base+u),(46,base+u)],'fixe',dash=True)
brace(ax,26,60,base+5*u+1.5,'varie',down=False,label='égaux : ils s’annulent')
text(ax,13,base-10,'départ','sujet','s'); text(ax,73,base-10,'arrivée','resultat','s')
save(fig,'72-098')
