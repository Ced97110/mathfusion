import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(52)
O=(44,13); R=30
a1=1.0; a3=3.0
pt=lambda a,r=R:(O[0]+r*math.cos(a),O[1]+r*math.sin(a))
line(ax,arc(O,R,0,math.pi,80),'fixe')
line(ax,[O,pt(0)],'fixe',lw=1.2); line(ax,[O,pt(a1)],'varie',lw=1.2); line(ax,[O,pt(a3)],'resultat',lw=1.6)
line(ax,arc(O,12,0,a1),'varie',lw=1.3); line(ax,arc(O,17,a1,a3),'varie',lw=1.3)
disc(ax,O[0],O[1],1.0,'fixe')
text(ax,pt(0)[0]+6,O[1],'départ','fixe','s')
text(ax,O[0]+19,O[1]+8,'1 rad','varie','s')
text(ax,O[0]-13,O[1]+19,'+ 2 rad','varie','s') if False else None
text(ax,O[0]+2,O[1]+20,'+ 2 rad','varie','s')
text(ax,pt(a3)[0]-1,pt(a3)[1]+4,'1 + 2 = 3 rad','resultat','s')
text(ax,44,4.5,r'un tour : $2\pi\approx 6{,}283$ rad : retour au départ','fixe','s')
save(fig,'29-141')
