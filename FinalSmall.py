w='ERRSOCKET CONNECTION ERROR'
v='red'
u='csv-colors'
t='config'
s='run.json'
r='resources/ico.png'
q='low'
p='high'
k='*'
j='a'
i='ERR'
h='csv'
g='r'
f='NO DATA'
e='multiplex'
d='bar-color'
c=range
b=isinstance
Z='{DEG}'
Y='ext'
X=Exception
W=chr
V=print
U=str
S='offset'
R='ico-size'
Q='max'
P=open
O=max
G=''
N=len
M=int
L=min
J='ico'
I=float
K=True
H='white'
F='pos'
E=None
D=False
C='size'
import serial as x,pygame as A,json,os,datetime as l,socket as B,threading
from cryptography.fernet import Fernet as y
from cryptography.hazmat.primitives.ciphers.aead import AESGCM as z
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization as m,hashes as n
from cryptography.hazmat.primitives.asymmetric import padding as o
import json,os
A.init()
def T(mult_list,val):A=[A*val for A in mult_list];return A
def a(list1,list2):A=[A+B for(A,B)in zip(list1,list2)];return A
def A7(self,param,info):
	V=param;G=self;B=info;P=A.image.load(B[J])if b(B[J],U)else B[J];P=A.transform.scale(P,(B[C][0]/B[R][0],B[C][1]/B[R][1]));B[J]=P;K=P.get_rect(center=(B[F][0]+B[C][0]/2+G.offset,B[F][1]+B[C][1]/2-B[C][1]/5));c=A.rect.Rect((0,0),A.display.get_surface().get_size())
	if c.contains(K):
		G.display.blit(P,K);K=A.Rect(B[F][0]+B[C][0]/10+G.offset,B[F][1]+B[C][1]/2+B[C][1]/16,B[C][0]/1.25,B[C][1]/6);A.draw.rect(G.display,B[d],K,border_radius=10)
		if B.get(S)is not E and G.data.get(V)is not E:N=I(G.data.get(V))+B[S]
		else:N=G.data.get(V)
		if N is not E:g=T(B[p],L(O(M(255*I(N))/B[Q],0),255));h=T(B[q],L(O(255-M(255*I(N)/B[Q]),0),255));i=a(g,h);K=A.Rect(B[F][0]+B[C][0]/10+G.offset,B[F][1]+B[C][1]/2+B[C][1]/16,O(L(B[C][0]/1.25*(I(N)*B[e])/B[Q],B[C][0]/1.25),0),B[C][1]/6);A.draw.rect(G.display,i,K,border_radius=10)
		X=G.font.render(f"{N}{B[Y].replace(Z,W(176))}"if G.data.get(V)is not E else f,D,H);K=X.get_rect(center=(B[F][0]+B[C][0]/2+G.offset,B[F][1]+B[C][1]/2+B[C][1]/3));G.display.blit(X,K)
	return B
def A8(self,param,info):
	V=param;G=self;B=info;P=A.image.load(B[J])if b(B[J],U)else B[J];P=A.transform.scale(P,(B[C][0]/B[R][0],B[C][1]/B[R][1]));B[J]=P;K=P.get_rect(center=(B[F][0]+B[C][0]/2+G.offset,B[F][1]+B[C][1]/2-B[C][1]/3.5));c=A.rect.Rect((0,0),A.display.get_surface().get_size())
	if c.contains(K):
		G.display.blit(P,K);K=A.Rect(B[F][0]+B[C][0]/3.75+B[C][0]/16+G.offset,B[F][1]+B[C][1]/2.8,B[C][0]/3,B[C][1]/2.5);A.draw.rect(G.display,B[d],K,border_radius=10)
		if B.get(S)is not E and G.data.get(V)is not E:N=I(G.data.get(V))+B[S]
		else:N=G.data.get(V)
		if N is not E:g=T(B[p],L(O(M(255*I(N))/B[Q],0),255));h=T(B[q],L(O(255-M(255*I(N)/B[Q]),0),255));i=a(g,h);K=A.Rect(B[F][0]+B[C][0]/3.75+B[C][0]/16+G.offset,B[F][1]+(B[C][1]/1.3-O(L(B[C][1]/2.5*(I(N)*B[e])/B[Q],B[C][1]/2.5),0)),B[C][0]/3,O(L(B[C][1]/2.5*(I(N)*B[e])/B[Q],B[C][1]/2.5),0));A.draw.rect(G.display,i,K,border_radius=10)
		X=G.font.render(f"{N}{B[Y].replace(Z,W(176))}"if N is not E else f,D,H);K=X.get_rect(center=(B[F][0]+B[C][0]/2+G.offset,B[F][1]+B[C][1]/2+B[C][1]/3));G.display.blit(X,K)
	return B
def A9(self,param,info):
	j='line-color';i='max-points';h='ico-offset';Q=param;P='max-val';K='points';G=self;B=info;T=A.image.load(B[J])if b(B[J],U)else B[J];T=A.transform.scale(T,(B[C][0]/B[R][0],B[C][1]/B[R][1]));B[J]=T;O=T.get_rect(center=(B[F][0]+B[C][0]/2+B[h][0]+G.offset,B[F][1]+B[C][1]/2-B[C][1]/5+B[h][1]));k=A.rect.Rect((0,0),A.display.get_surface().get_size())
	if k.contains(O):
		G.display.blit(T,O);e=G.font.render(f"{G.data.get(Q)}{B[Y].replace(Z,W(176))}"if G.data.get(Q)is not E else f,D,H);O=e.get_rect(center=(B[F][0]+B[C][0]/2+G.offset,B[F][1]+B[C][1]/2+B[C][1]/3));G.display.blit(e,O)
		if B.get(K)is E:B[K]=[]
		if B.get(S)is not E and G.data.get(Q)is not E:V=I(G.data.get(Q))+B[S]
		else:V=G.data.get(Q)
		if V is not E:B[K].append(M(I(V)))
		if N(B[K])>B[i]:B[K]=B[K][1:]
		O=A.Rect(B[F][0]+B[C][0]/20+G.offset,B[F][1]+B[C][1]/2.6,B[C][0]/1.1,B[C][1]/3);A.draw.rect(G.display,B[d],O,border_radius=10);g=B[C][0]/1.2/B[i];X=0;a=E
		for c in B[K]:
			if a is E:A.draw.circle(G.display,B[j],(B[F][0]+B[C][0]/12+G.offset,B[F][1]+B[C][1]/1.5-B[C][1]/4*L(c,B[P])/B[P]),3)
			else:A.draw.line(G.display,B[j],a,(B[F][0]+B[C][0]/12+g*X+G.offset,B[F][1]+B[C][1]/1.5-B[C][1]/4*L(c,B[P])/B[P]),5)
			a=B[F][0]+B[C][0]/12+g*X+G.offset,B[F][1]+B[C][1]/1.5-B[C][1]/4*L(c,B[P])/B[P];X+=1
	return B
def A0(color,incr):
	A=[]
	for B in color:A.append(L(B+incr,255))
	return A
def A1(surf,start,end,color):
	C=end;B=start;E=round((C[1]-B[1])/15)
	for D in c(E):V();F=B[1]+D*15+10 if B[1]+D*15+10<=C[1]else C[1];A.draw.line(surf,color,(B[0],B[1]+D*15),(B[0],F),3)
class A2:
	def __init__(B,display=E):
		F=display;B.shiftdelay=0
		if F is E:A.display.set_mode((1000,750),A.RESIZABLE);B.display=A.display.get_surface()
		else:B.display=F;B.shiftdelay=50
		A.display.set_caption('Visualizer');A.display.set_icon(A.image.load(r));B.csv={};B.open_csv=G;B.open_csv_name=G;B.offset=0;B.csv_active=D;B.csv_val=G;B.visualizer_active=D;B.activation_delay=0;B.font=A.font.Font(E,35);B.small_font=A.font.Font(E,20);B.mouse=A.math.Vector2();B.offset_scroll=0;B.visualizer_surf=A.Surface((800,600));B.visualizer_surf.fill((20,20,20));B.max_length=0;B.max_val=0;B.cutinstance=D;B.side_screen_value='   NO FILES OPEN'
		with P(s,g)as C:B.run_data=json.load(C);B.set_csvs=B.run_data[h];B.config=B.run_data[t];B.colors=B.run_data[u]
		B.possible_items=B.set_csvs
		for C in B.set_csvs:
			if os.path.exists(f"csv/{C}.csv"):
				with P(f"csv/{C}.csv",g)as H:I=H.readlines();B.csv[C]=[A.split(',')if not A.startswith('#')else A for A in I[1:]]
	def render_text(A,text,loc,color):B=A.font.render(text,D,color);A.display.blit(B,loc)
	def prepare(A):A.display.fill((20,20,20))
	def draw_gradient_rect(H,rect,top_color,bottom_color,vert=K):
		I,J,D,B=rect;E=A.Surface((D,B),A.SRCALPHA)
		for C in c(B):
			if vert:F=255*(1-C/B)
			else:F=255*(C/B)
			G=top_color.lerp(bottom_color,C/B);G.a=M(F);A.draw.line(E,G,(0,C),(D,C))
		H.display.blit(E,(I,J))
	def render(B):
		L=D;B.prepare()
		if not B.visualizer_active:
			F=0
			for I in B.open_csv:
				if 135+F*50-B.offset_scroll>B.display.get_height():break
				if type(I)is U:
					if 135+F*50-B.offset_scroll>100:B.render_text(I.strip(),(70+B.offset,135+F*50-B.offset_scroll),(0,200,150))
				else:
					O=0
					for M in c(N(I)):
						if 135+F*50-B.offset_scroll>100:B.render_text(I[M].strip(),(O+70+B.offset,135+F*50-B.offset_scroll),B.config[u][M])
						O+=B.font.size(I[M])[0]+B.config['csv-split']
				F+=1
			J=A.Rect(0,100,B.display.get_width(),10);A.draw.rect(B.display,(20,20,20),J);J=A.Rect(0,110,B.display.get_width(),25);B.draw_gradient_rect(J,A.Color(20,20,20,255),A.Color(20,20,20,0));J=A.Rect(0,B.display.get_height()-25,B.display.get_width(),25);B.draw_gradient_rect(J,A.Color(20,20,20,0),A.Color(20,20,20,255),vert=D)
		else:B.display.blit(B.visualizer_surf,(B.offset+50,175))
		P=B.font.render(B.side_screen_value[3:],D,v if B.side_screen_value.startswith(i)else H);B.side_screen_rect=P.get_rect(topright=(B.display.get_width()-75-B.offset,75));B.display.blit(P,B.side_screen_rect);B.offset=(B.display.get_width()-1000)/2;E=A.Rect(355+B.offset,65,50,40);C=60,60,60
		if B.visualizer_active:C=125,125,125
		if E.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
			if not B.visualizer_active:C=100,100,100
			if B.activation_delay<=0 and A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:B.visualizer_active=not B.visualizer_active;B.activation_delay=300
		B.activation_delay-=1;A.draw.rect(B.display,C,E,border_radius=10);B.render_text('V',(372+B.offset,75),H);E=A.Rect(425+B.offset,65,50,40);C=60,60,60
		if E.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
			C=100,100,100
			if B.open_csv!=G and B.activation_delay<=0 and A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:
				try:
					B.csv.pop(B.open_csv_name);B.open_csv=[];B.visualizer_surf.fill((20,20,20))
					if os.path.exists(f"csv/{B.open_csv_name}.csv"):os.remove(f"csv/{B.open_csv_name}.csv")
				except:pass
		B.activation_delay-=1;A.draw.rect(B.display,C,E,border_radius=10);B.render_text('C',(442+B.offset,75),H);E=A.Rect(55+B.offset,65,275,40);C=60,60,60
		if B.csv_active:C=75,75,75
		if E.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
			C=100,100,100
			if A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:L=K;B.csv_active=K
		if N(B.possible_items)==0 or not B.csv_active:A.draw.rect(B.display,C,E,border_radius=10)
		else:A.draw.rect(B.display,C,E,border_top_left_radius=10,border_top_right_radius=10)
		if B.csv_active:
			E=A.Rect(B.font.size(f"{B.csv_val}")[0]+78+B.offset,75,13,22);A.draw.rect(B.display,H,E);F=0
			for Q in B.possible_items:
				E=A.Rect(55+B.offset,105+40*F,275,40);C=60,60,60
				if B.csv_active:C=75,75,75
				if E.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
					C=100,100,100
					if A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:L=K;B.csv_active=D;B.csv_val=Q;B.load_file();B.search_csv()
				if F+1==N(B.possible_items):A.draw.rect(B.display,C,E,border_bottom_left_radius=10,border_bottom_right_radius=10)
				else:A.draw.rect(B.display,C,E)
				B.render_text(Q,(65+B.offset,110+40*F),H);F+=1
		B.render_text(B.csv_val,(70+B.offset,75),H);B.render_text('CSV',(70+B.offset,35),H);C=60,60,60;E=A.rect.Rect(-50+B.offset,65,50,40)
		if E.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
			if(A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2])and B.shiftdelay<0:B.cutinstance=K
			C=100,100,100
		A.draw.rect(B.display,C,E,border_radius=10);B.render_text(text=f"M",loc=(-35+B.offset,75),color=H)
		if not L and A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:B.csv_active=D
		A.display.update()
	def manage_events(C):
		for B in A.event.get():
			if B.type==A.QUIT or B.type==A.KEYDOWN and B.key==A.K_ESCAPE:A.quit();exit()
			elif B.type==A.KEYDOWN:C.manage_key(key=B.key,unicode=B.unicode)
	def load_file(B):
		P=' '
		try:
			B.open_csv_name=B.csv_val;B.offset_scroll=0;B.open_csv=B.csv[B.csv_val];J=B.config['display-data']
			try:R=B.config[B.csv_val+' multiplex']
			except:R=1
			B.max_length=0
			for C in B.open_csv:
				B.max_length+=1
				if N(C)>=J and C[J]!=P:
					F=M(I(C[J].strip().split(P)[0])*R)
					if F>B.max_val:B.max_val=F
			Y=K
			try:
				L=0;Q=E;O=800/B.max_length;S=500/B.max_val;Z=G;a=-10000000;b=0;B.visualizer_surf.fill((20,20,20))
				for C in B.open_csv:
					if C[0]=='#':
						Q=E
						if C.startswith('# ---- N'):
							F=C.split(',')[1].strip().split(P)[0]
							if F!=Z:
								Z=F;c=B.small_font.render(F,D,H);T=c.get_width();U=100+L*O-T/2
								if U-T/2>a-b/2:B.visualizer_surf.blit(c,(U,515));a=U;b=T
					elif N(C)>=J:
						if C[J]!=P:
							F=M(I(C[J].strip().split(P)[0])*R)
							if Q is E:A1(B.visualizer_surf,(100+L*O,500-S*F),(100+L*O,500),A0(B.colors[B.csv_val],50))
							else:A.draw.line(B.visualizer_surf,B.colors[B.csv_val],Q,(100+L*O,500-S*F),5)
							Q=100+L*O,500-S*F;L+=1
			except X as W:V(W);Y=D;B.side_screen_value='ERRVISUALIZATION ERROR'
			B.max_length*=50;B.max_length-=550
			if Y:B.side_screen_value=f"   FILE={B.csv_val}"
		except X as W:V(W);B.side_screen_value='ERRFILE NOT FOUND'
	def search_csv(A):
		B=[]
		for C in A.possible_items:
			if C.startswith(A.csv_val):B.append(C)
		A.possible_items=B
	def manage_key(B,key,unicode):
		if key==A.K_RETURN:B.load_file()
		elif B.csv_active:
			if key==A.K_BACKSPACE:
				B.csv_val=B.csv_val[:-1];C=[]
				for D in B.set_csvs:
					if D.startswith(B.csv_val):C.append(D)
				B.possible_items=C
			elif B.font.size(f"{B.csv_val}")[0]<225:B.csv_val+=unicode;B.search_csv()
	def manage_scroll(B):
		if not B.visualizer_active:
			C=A.key.get_pressed()
			if C[A.K_UP]:
				B.csv_active=D
				if B.offset_scroll>0:B.offset_scroll-=10
			elif C[A.K_DOWN]:
				B.csv_active=D
				if B.offset_scroll<B.max_length:B.offset_scroll+=10
	def run(B):
		while not B.cutinstance:
			try:B.shiftdelay-=1;B.render();B.manage_events();B.manage_scroll();B.mouse=A.mouse.get_pos()
			except X as C:V(f"CRITICAL ERROR: {C}")
		del B
def T(mult_list,val):A=[A*val for A in mult_list];return A
def a(list1,list2):A=[A+B for(A,B)in zip(list1,list2)];return A
def A3(aesgcm,message,nonce):return aesgcm.encrypt(nonce,message.encode(),E)
def A4(aesgcm,message,nonce):return aesgcm.decrypt(nonce,message,E)
class A5:
	def __init__(B):
		B.private_key=rsa.generate_private_key(public_exponent=65537,key_size=2048);B.public_key=B.private_key.public_key();B.public_key_pem=B.public_key.public_bytes(encoding=m.Encoding.PEM,format=m.PublicFormat.SubjectPublicKeyInfo);A.init()
		with P(s,g)as C:B.run_data=json.load(C)
		B.app_info=B.run_data['data'];B.cvs=B.run_data[h];B.config=B.run_data[t];B.csv_delay=B.config['csv-timeout'];B.active_csv_delay=B.csv_delay
		for C in B.cvs:
			if not os.path.exists(f"csv/{C}.csv"):
				with P(f"csv/{C}.csv",'w')as F:F.write(f"{B.cvs[C]}\n")
			with P(f"csv/{C}.csv",j)as F:F.write(f"# ---- New Entry, {l.datetime.now()} ---- #\n")
		B.shiftdelay=0;A.display.set_mode((1000,750),A.RESIZABLE);B.display=A.display.get_surface();B.offset=0;A.display.set_caption('Tank Manager');A.display.set_icon(A.image.load(r));B.font=A.font.Font(E,35);B.data={};B.arduino=E;B.remote=D;B.locked=D;B.baud='9600';B.port='COM';B.password=G;B.side_screen_data='ERRNO CONNECTION';B.side_screen_rect=A.Rect(0,0,0,0);B.port_active=D;B.baud_active=D;B.password_active=D;B.delay=200;B.mouse=A.math.Vector2();B.cipher=E;B.cutinstance=D
	def connect(A):
		try:
			if A.baud.__contains__('.'):
				try:A.remote=K;A.arduino=B.socket(B.AF_INET,B.SOCK_STREAM);A.arduino.connect((A.baud,M(A.port)));A.locked=K;A.side_screen_data=f"   CONNECTED"
				except:A.arduino=E;A.side_screen_data=w
			else:A.remote=D;A.arduino=x.Serial(port=A.port,baudrate=M(A.baud),timeout=.1);A.side_screen_data=f"   CONNECTED"
			for C in A.cvs:
				with P(f"csv/{C}.csv",j)as F:F.write(f"# ---- Connection Opened, Port={A.port} Baud={A.baud} ---- #\n")
		except:A.side_screen_data='ERRCOM CONNECTION ERROR'
	def write_read(A):
		if A.remote:
			if not A.locked:B=A.cipher.decrypt(A.arduino.recv(1024)).decode()
			else:B=G
		else:B=A.arduino.readline().decode()
		return B
	def manage_events(C):
		for B in A.event.get():
			if B.type==A.QUIT or B.type==A.KEYDOWN and B.key==A.K_ESCAPE:
				A.quit()
				if C.arduino:C.arduino.close()
				exit()
			elif B.type==A.KEYDOWN:C.manage_key(key=B.key,unicode=B.unicode)
	def manage_key(B,key,unicode):
		F=unicode;C=key
		if C==A.K_RETURN:
			if B.password_active:
				try:
					B.arduino.send(B.public_key_pem);B.arduino.settimeout(3);J=B.arduino.recv(1024);K=B.private_key.decrypt(J,o.OAEP(mgf=o.MGF1(algorithm=n.SHA256()),algorithm=n.SHA256(),label=E));G=os.urandom(12);I=z(K);B.arduino.send(A3(I,B.password,G));B.arduino.send(G)
					try:H=B.arduino.recv(1024);H=A4(I,H,G);B.cipher=y(H);B.locked=D
					except:B.arduino=E;B.side_screen_data='ERRAUTHENTICATION ERROR'
				except:B.side_screen_data=w
			else:B.connect()
			if not B.side_screen_data.startswith(i):B.port_active=D;B.baud_active=D;B.password_active=D
		elif B.port_active:
			if C==A.K_BACKSPACE:B.port=B.port[:-1]
			elif B.font.size(f"{B.port}")[0]<125:B.port+=F
		elif B.baud_active:
			if C==A.K_BACKSPACE:B.baud=B.baud[:-1]
			elif B.font.size(f"{B.baud}")[0]<225:B.baud+=F
		elif B.password_active:
			if C==A.K_BACKSPACE:B.password=B.password[:-1]
			elif B.font.size(f"{N(B.password)*k}")[0]<125:B.password+=F
	def render_text(A,text,loc):B=A.font.render(text,D,H);A.display.blit(B,loc)
	def prepare(A):A.display.fill((20,20,20))
	def render(B):
		M='csv_delay';B.offset=(B.display.get_width()-1000)/2;O=D
		if B.arduino:
			if B.locked:
				I=60,60,60
				if B.baud_active:I=75,75,75
				G=A.Rect(55+B.offset,165,175,40)
				if G.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
					if A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:O=K;B.port_active=D;B.baud_active=D;B.password_active=K
					I=100,100,100
				A.draw.rect(B.display,I,G,border_radius=10)
				if B.password_active:G=A.Rect(B.font.size(f"{N(B.password)*k}")[0]+78+B.offset,175,13,22);A.draw.rect(B.display,H,G)
				B.render_text(text=f"{N(B.password)*k}",loc=(75+B.offset,175));B.render_text(text='Password',loc=(70+B.offset,135))
			else:
				for L in B.app_info:
					J=B.app_info[L];G=A.Rect(J[F][0]+B.offset,J[F][1],J[C][0],J[C][1]);I=J['background-color']
					if G.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):I=J['hover-color']
					A.draw.rect(B.display,I,G,border_radius=10);J=getattr(RenderMethods,J['visual'])(B,L,J)
					if J.get(M)is E:J[M]=B.csv_delay
					J[M]-=1
					if J[M]<=0:
						J[M]=B.csv_delay
						if B.data.get(L)is not E:
							with P(f"csv/{J[h]}.csv",j)as R:R.write(f"{U(l.datetime.now())},{f"{B.data.get(L)}{J[Y].replace(Z,W(176))}"}\n")
					B.app_info[L]=J
		Q=B.font.render(B.side_screen_data[3:],D,v if B.side_screen_data.startswith(i)else H);B.side_screen_rect=Q.get_rect(topright=(B.display.get_width()-75-B.offset,75));B.display.blit(Q,B.side_screen_rect);G=A.Rect(55+B.offset,65,175,40);I=60,60,60
		if B.port_active:I=75,75,75
		if G.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
			if A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:O=K;B.port_active=K;B.baud_active=D;B.password_active=D
			I=100,100,100
		A.draw.rect(B.display,I,G,border_radius=10)
		if B.port_active:G=A.Rect(B.font.size(f"{B.port}")[0]+78+B.offset,75,13,22);A.draw.rect(B.display,H,G)
		B.render_text(text=f"{B.port}",loc=(75+B.offset,75));B.render_text(text='Port',loc=(70+B.offset,35));I=60,60,60
		if B.baud_active:I=75,75,75
		G=A.Rect(250+B.offset,65,275,40)
		if G.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
			if A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:O=K;B.port_active=D;B.baud_active=K;B.password_active=D
			I=100,100,100
		A.draw.rect(B.display,I,G,border_radius=10)
		if B.baud_active:G=A.Rect(B.font.size(f"{B.baud}")[0]+278+B.offset,75,13,22);A.draw.rect(B.display,H,G)
		B.render_text(text=f"{B.baud}",loc=(275+B.offset,75));B.render_text(text='Baud/IP',loc=(265+B.offset,35))
		if not O and A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2]:B.port_active=D;B.baud_active=D;B.password_active=D
		I=60,60,60;G=A.rect.Rect(-50+B.offset,65,50,40)
		if G.contains(A.Rect(B.mouse[0],B.mouse[1],1,1)):
			if(A.mouse.get_pressed()[0]or A.mouse.get_pressed()[1]or A.mouse.get_pressed()[2])and B.shiftdelay<0:S=A2(display=B.display);S.run();B.shiftdelay=200
			I=100,100,100
		A.draw.rect(B.display,I,G,border_radius=10);B.render_text(text=f"V",loc=(-35+B.offset,75));A.display.update()
	def run(B):
		H='\r\n'
		while not B.cutinstance:
			try:
				B.shiftdelay-=1;B.prepare()
				try:
					D=B.write_read()
					if H in D:
						E={};F=D.split(H);F.reverse()
						for C in F:
							if E.get(C[0:3]):break
							E[C[0:3]]=K
							if C[3:]!=G:B.data[C[0:3]]=C[3:]
					else:B.data[D[0:3]]=D[3:-2]
				except:pass
				B.manage_events();B.render();B.mouse=A.mouse.get_pos()
			except X as I:V(f"CRITICAL ERROR: {I}")
if __name__=='__main__':A6=A5();A6.run()