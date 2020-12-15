class VW():
    def __init__(self,TurningData,d,translation_v):
        self.r=TurningData.Radius
        self.direction=TurningData.Direction
        self.d=d
        self.v=translation_v

        self.v_in  =self.v*((self.r+self.d)/self.r)
        self.v_out =self.v*((self.r-self.d)/self.r)

    def V_IN(self):
        return self.v_in

    def V_OUT(self):
        return self.v_out

    def W(self):
        if self.direction=="l":
            return (self.v_in-self.v_out)/(2*self.d)
        elif self.direction=="r":
            return (self.v_out-self.v_in)/(2*self.d)
