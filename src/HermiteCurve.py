class HermiteCurve():
	"""docstring for HermiteCurve"""
	def __init__(self, x,y,vx,vy):
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy

	def xt(self,t):
		self.x1=(2*self.x[0]-2*self.x[1]+self.vx[0]+self.vx[1])*(t**3)
		self.x2=(-3*self.x[0]+3*self.x[1]-2*self.vx[0]-self.vx[1])*(t**2)
		self.x3=self.vx[0]*t+self.x[0]

		return self.x1+self.x2+self.x3

	def yt(self,t):
		self.y1=(2*self.y[0]-2*self.y[1]+self.vy[0]+self.vy[1])*(t**3)
		self.y2=(-3*self.y[0]+3*self.y[1]-2*self.vy[0]-self.vy[1])*(t**2)
		self.y3=self.vy[0]*t+self.y[0]
		
		return self.y1+self.y2+self.y3

	def v(self,t):
		self.vx_ref1=(2*self.x[0]-2*self.x[1]+self.vx[0]+self.vx[1])*(t**2)
		self.vx_ref2=(-3*self.x[0]+3*self.x[1]-2*self.vx[0]-self.vx[1])*t
		self.vx_ref3=self.vx[0]

		self.vy_ref1=(2*self.y[0]-2*self.y[1]+self.vy[0]+self.vy[1])*(t**2)
		self.vy_ref2=(-3*self.y[0]+3*self.y[1]-2*self.vy[0]-self.vy[1])*t
		self.vy_ref3=self.vy[0]

		self.v2=((vx_ref1+vx_ref2+vx_ref3)**2)+((vy_ref1+vy_ref2+vy_ref3)**2)
		return