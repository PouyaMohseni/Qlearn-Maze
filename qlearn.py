class qtable:
    env: list
    env_0: int
    env_1: int
    landa: int
    alpha: int
    dic = {"L":0,"U":1,"R":2,"D":3}
    
    def __init__(self,env_0,env_1,landa,alpha):
        self.env_0 = env_0
        self.env_1 = env_1
        self.landa = landa
        self.alpha = alpha
        self.env = [[[0 for _ in range(4)] for _ in range(env_1)] for _ in range(env_0)]
        #print(self.env)
    def set_q(self,y,x,a,reward):
        self.env[y][x][self.dic.get(a)]=reward

    def get_q(self,y,x,a):
        if x<0 or y<0 or x>=self.env_0 or y>=self.env_1: return -9e9 
        return self.env[y][x][self.dic.get(a)]
