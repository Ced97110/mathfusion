import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(62)
text(ax,23,56,"droite oblique","sujet"); text(ax,66,56,"droite verticale","sujet")
line(ax,[(6,16),(40,36)],"sujet",lw=1.1); line(ax,[(6,16),(40,16)],"fixe",lw=0.9); line(ax,[(40,16),(40,36)],"varie",lw=0.9)
text(ax,23,12,"avancée","fixe"); text(ax,43,26,"montée","varie",ha="left")
line(ax,[(66,16),(66,50)],"sujet",lw=1.1)
arrow(ax,(66,16),(66,36),"varie"); disc(ax,66,16,1.2,"sujet")
text(ax,69,26,"montée 1","varie",ha="left"); text(ax,66,11,"avancée 0","varie")
text(ax,44,4,"pente = montée ÷ avancée","encre")
save(fig,"28-136")
