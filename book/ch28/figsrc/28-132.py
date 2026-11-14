import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(80); ox,oy,R=12,10,62
line(ax,[(ox,oy),(ox+R+2,oy)],"fixe",lw=0.6); line(ax,[(ox,oy),(ox,oy+R+2)],"fixe",lw=0.6)
line(ax,[(ox,oy),(ox+R*0.707,oy+R*0.707+0)],"fixe",lw=0.7,dash=True)
text(ax,ox+R*0.707+1,oy+R*0.707+3,"miroir","fixe","s",ha="left")
p30=pt(ox,oy,R,30); p60=pt(ox,oy,R,60)
line(ax,[(ox,oy),p30],"sujet",lw=0.8); line(ax,[(ox,oy),p60],"autre",lw=0.8)
disc(ax,*p30,1.5,"sujet"); disc(ax,*p60,1.5,"autre")
for p,r in [(p30,"sujet"),(p60,"autre")]:
    line(ax,[p,(p[0],oy)],"fixe",lw=0.6,dash=True); line(ax,[p,(ox,p[1])],"fixe",lw=0.6,dash=True)
text(ax,p30[0],oy-3,r"$c$","sujet"); text(ax,p60[0],oy-3,r"$a$","autre")
text(ax,ox-3,p30[1],r"$a$","sujet"); text(ax,ox-3,p60[1],r"$c$","autre")
text(ax,p30[0]+2.6,p30[1]+3,r"$(c,\ a)$"+"\n30°","sujet",ha="left")
text(ax,p60[0]+2.6,p60[1]+4,r"$(a,\ c)$"+"\n60°","autre",ha="left")
arrow(ax,(p30[0]-2,p30[1]+3),(p60[0]+2,p60[1]-3),"varie",curve=0.35,both=True)
text(ax,52,44,"échange","varie","m")
save(fig,"28-132")
