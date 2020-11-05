import math

class HermiteCurve():
	#	arg[Start value,End value]
	def __init__(self, x,y,vx,vy):
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy

	def Xt(self,t):
		self.x1=(2*self.x[0]-2*self.x[1]+self.vx[0]+self.vx[1])*(t**3)
		self.x2=(-3*self.x[0]+3*self.x[1]-2*self.vx[0]-self.vx[1])*(t**2)
		self.x3=self.vx[0]*t+self.x[0]

		return self.x1+self.x2+self.x3

	def Yt(self,t):
		self.y1=(2*self.y[0]-2*self.y[1]+self.vy[0]+self.vy[1])*(t**3)
		self.y2=(-3*self.y[0]+3*self.y[1]-2*self.vy[0]-self.vy[1])*(t**2)
		self.y3=self.vy[0]*t+self.y[0]
		
		return self.y1+self.y2+self.y3

	def Vxt(self,t):
		self.vx_ref1=(2*self.x[0]-2*self.x[1]+self.vx[0]+self.vx[1])*(t**2)
		self.vx_ref2=(-3*self.x[0]+3*self.x[1]-2*self.vx[0]-self.vx[1])*t
		self.vx_ref3=self.vx[0]
		self.vx_ref=self.vx_ref1+self.vx_ref2+self.vx_ref3

		return self.vx_ref

	def Vyt(self,t):
		self.vy_ref1=(2*self.y[0]-2*self.y[1]+self.vy[0]+self.vy[1])*(t**2)
		self.vy_ref2=(-3*self.y[0]+3*self.y[1]-2*self.vy[0]-self.vy[1])*t
		self.vy_ref3=self.vy[0]
		self.vy_ref=self.vy_ref1+self.vy_ref2+self.vy_ref3

		return self.vy_ref

	def Vt(self,t):
		self.Vxt(t)
		self.Vyt(t)
		self.vx_b=self.vx_ref
		self.vy_b=self.vy_ref
		self.v2=(self.vx_b**2)+(self.vy_b**2)
		return math.sqrt(self.v2)

	def Tht(self,t):
		self.Vxt(t)
		self.Vyt(t)

		return math.atan2(self.vy_ref,self.vx_ref)

	def Wt(self,t,dt):
		return self.Tht(t+dt)-self.Tht(t)
