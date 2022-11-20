from qlearn import qlearn

class maze():
    agent: list #Agent's position [0,0]
    flags = [] #Flags' positions [[0,1],...]
    target: list #Target's positions [1,1]
    blocks = [] #blocks positions [[1,0],...]
    obstacles = [] #obsticales' positions [[2,1],...]
    flag_num: int #number of flags
    env: list #maze [[W,B,W,W],[W,F,T,O],...]
    env_0: int #maze y size
    env_1: int #maze x size
    env_size: int #maze's size
    env_lose: int #lose points
    visited: list #visited points is set 1
    
    def __init__(self, env, agent):
        self.env = env
        self.agent = agent

        for i in self.env:
            for j in self.env[0]:
                if self.env[i][j]=="B": blocks.append([i,j])
                elif self.env[i][j]=="O": obstacles.append([i,j])
                elif self.env[i][j]=="F": flags.append([i,j])
                
        self.flag_num = len(self.flags)
        
        self.env_0 = len(self.env)
        self.env_1 = len(self.env[0])
        self.env_size = self.env_0*self.env_1

        self.visited = [[0 for _ in range(self.env_1)] for _ in range(self.env_0)]

        self.env_lose = -1*self.env_size
      
    def reward(self,action):
        """
        actions: [L: left,
                  U: up,
                  R: right,
                   D: down
        """

        new_agent = self.find_position(action)
            
        if self.env[new_agent[0],new_agent[1]]=="B":
            return self.env_lose*2
        elif self.env[new_agent[0],new_agent[1]]=="O":
            return 0
        elif self.env[new_agent[0],new_agent[1]]=="F":
            return 0.1*(self.env_size/self.flag_num)
        elif self.env[new_agent[0],new_agent[1]]=="T":
            return self.env_size
        elif self.visited[new_agent[0],new_agent[1]]>=2:
            return -4/self.env_size
        elif self.visited[new_agent[0],new_agent[1]]>=2:
            return -1.1/self.env_size
        else:
            return -1.0/self.env_size

    def take_an_action(self):
        action_set = ["L","U","R","D"]

        if self.agent[0] == 0: action_set.remove("L")
        if self.agent[0] == self.env_0: action_set.remove("R")
        if self.agent[1] == 0: action_set.remove("U")
        if self.agent[1] == self.env_1: action_set.remove("D")


        #policy and action

        self.agent = self.find_position(action)

    def find_position(self,action):
        if   action=="L": return [self.agent[0],self.agent[1]-1]
        elif action=="U": return [self.agent[0]+1,self.agent[1]]
        elif action=="R": return [self.agent[0],self.agent[1]+1]
        elif action=="D": return [self.agent[0]-1,self.agent[1]]

        
    def set_table(self,landa,alpha):
        self.qtable = qlearn(self.env_0,self.env_1,landa,alpha)
