import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(86); ox,oy,u=30,8,10; lx=ox+u
line(ax,[(ox-4,oy),(lx+4,oy)],"fixe",lw=0.6)
arrow(ax,(lx,oy),(lx,76),"sujet",lw=1.1)
for d,v in [(60,"1,73"),(80,"5,67")]:
    h=u*math.tan(math.radians(d)); line(ax,[(ox,oy),(lx,oy+h)],"varie",lw=0.9); disc(ax,lx,oy+h,1.3,"resultat")
    text(ax,lx+3,oy+h,f"{d}° : {v}","resultat","m",ha="left")
L=64; line(ax,[(ox,oy),(ox+L*math.tan(math.radians(1)),oy+L)],"varie",lw=0.9)
text(ax,lx+3,oy+L,"89° : 57,3","resultat","m",ha="left")
line(ax,[(ox,oy),(ox,78)],"fixe",lw=0.8,dash=True)
text(ax,ox-4,81,"90° : pas de T","fixe","m",ha="right")
text(ax,lx+2,4,r"$A$","sujet"); text(ax,ox-3,4,r"$O$","encre"); text(ax,lx+14,81,r"$x=1$","sujet")
save(fig,"28-139")
