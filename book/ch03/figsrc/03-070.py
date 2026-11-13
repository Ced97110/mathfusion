import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(96)
def wm(s,size):
    t=ax.text(0,0,s,fontsize=SIZE[size]); fig.canvas.draw(); b=t.get_window_extent(fig.canvas.get_renderer()); t.remove()
    return b.width/fig.dpi*25.4
def expr(cx,y,s,grp,first,lab,by,role='sujet'):
    text(ax,cx,y,s,role,'l'); W=wm(s,'l'); g=wm(grp,'l')
    if first: x0=cx-W/2; x1=x0+g
    else: x1=cx+W/2; x0=x1-g
    brace(ax,x0,x1,by,'varie',label=lab)
text(ax,44,91,'multiplication','encre','s')
expr(22,80,'(8 × 3) × 14','(8 × 3)',True,'24',76)
expr(66,80,'8 × (3 × 14)','(3 × 14)',False,'42',76)
box(ax,9,59.5,26,7,'resultat',label='24 × 14 = 336',size='s'); box(ax,53,59.5,26,7,'resultat',label='8 × 42 = 336',size='s')
line(ax,[(35,63),(53,63)],'resultat')
line(ax,[(4,55),(84,55)],'fixe')
text(ax,44,50,'division','autre','s')
expr(22,38,'(24 ÷ 4) ÷ 2','(24 ÷ 4)',True,'6',34,'autre')
expr(66,38,'24 ÷ (4 ÷ 2)','(4 ÷ 2)',False,'2',34,'autre')
box(ax,10,17.5,24,7,'limite',label='6 ÷ 2 = 3',size='s'); box(ax,54,17.5,24,7,'limite',label='24 ÷ 2 = 12',size='s')
line(ax,[(35,21),(53,21)],'limite')
line(ax,[(42.6,19.6),(45.4,22.4)],'limite'); line(ax,[(42.6,22.4),(45.4,19.6)],'limite')
save(fig,'03-070')
