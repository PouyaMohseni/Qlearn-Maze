class qlearn:
    env: list
    landa: int
    alpha: int

    def __init__(self,env_0,env_1,landa,alpha):
        self.landa = landa
        self.alpha = alpha
        env = [[0 for _ in range(env_1)] for _ in range(env_0)]

    def set_reward(self,y,x,reward):
        self.env[y][x]==reward

    def reward(self,y,x):
        return self.env[y][x]
