import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class copy_maze():
    def __init__(self):
        pass
    def copy(self,maze):
        self.agent = maze.agent
        self.flags = maze.flags
        self.target = maze.target
        self.blocks = maze.blocks 
        self.obstacles = maze. obstacles
        self.flag_num = maze.flag_num 
        self.env = maze.env
        #self.env_agent = maze.env_agent 
        self.env_0 = maze.env_0
        self.env_1 = maze.env_1 
        self.env_size = maze.env_size 
        self.env_lose = maze.env_lose
        self.visited = maze.visited
        self.lose = maze.lose
        self.win = maze.win
        
    def paste(self, maze):
        maze.agent = self.agent
        maze.flags = self.flags
        maze.target = self.target
        maze.blocks = self.blocks 
        maze.obstacles = self. obstacles
        maze.flag_num = self.flag_num 
        maze.env = self.env
        #maze.env_agent = self.env_agent 
        maze.env_0 = self.env_0
        maze.env_1 = self.env_1 
        maze.env_size = self.env_size 
        maze.env_lose = self.env_lose
        maze.visited = self.visited
        maze.lose = self.lose
        maze.win = self.win
        
class maze():
    agent: list #Agent's position [0,0]
    flags = [] #Flags' positions [[0,1],...]
    target: list #Target's positions [1,1]
    blocks = [] #blocks positions [[1,0],...]
    obstacles = [] #obsticales' positions [[2,1],...]
    flag_num: int #number of flags
    env: list #maze [[W,B,W,W],[W,F,T,O],...]
    env_agent: list #The env with agent and its path
    env_0: int #maze y size
    env_1: int #maze x size
    env_size: int #maze's size
    env_lose: int #lose points
    visited: list #visited points is set 1
    copy: copy_maze #maze attributes copy
    
    #lose_game = 0 #If it has lose the game
    #win_game = 0 #If it has win the game
    
    def __init__(self, env, agent, target):
        self.env = env
        self.agent = agent
        self.target = target
        
        for i in range(len(self.env)):
            for j in range(len(self.env[0])):
                if self.env[i][j]=="B": self.blocks.append([i,j])
                elif self.env[i][j]=="O": self.obstacles.append([i,j])
                elif self.env[i][j]=="F": self.flags.append([i,j])
                
        self.flag_num = len(self.flags)
        
        self.env_0 = len(self.env)
        self.env_1 = len(self.env[0])
        self.env_size = self.env_0*self.env_1

        self.visited = [[0 for _ in range(self.env_1)] for _ in range(self.env_0)]
        self.env_lose = -1 #?*self.env_size
      
        #Copy the maze
        self.copy = copy_maze()
        self.copy.copy(self)
        
    def reload(self):
        #Reload the maze
        self.copy.paste(self)
    
    def show_env(self):
        plt.grid('on')
        self.set_env_agent()
        cmap = ListedColormap(["white", "yellow","red","black","gray"])
        #cmap.set_bad("silver")
        plt.imshow([[{"W":0,"A":1,"T":2,"B":3,"V":4,"F":4,"O":5}.get(i) for i in item]  for item in self.env_agent],cmap=cmap)

        plt.show()
    
    def set_env_agent(self):
        self.env_agent = self.env
        
        self.env_agent[self.agent[0]][self.agent[1]]= "A"
        self.env_agent[self.target[0]][self.target[1]]= "T"
        
        for i in range(len(self.visited)):
            for j in range(len(self.visited[0])):
                if self.visited[i][j]==1: self.env_agent[i][j] = "V"
        
    
    def train(self,epochs,landa,alpha):
        self.set_table(landa,alpha)
        
        #epochs=2
        for epoch in range(epochs):
            
            self.train_epoch()
    
    def train_epoch(self):
        while not (self.win() or self.lose()):
            self.take_a_step()
            
        print(250*"-")
        self.eliminate_game()
        
    def take_a_step(self):
        action_set = {"L":0,"U":0,"R":0,"D":0}

        if self.agent[0] == 0: action_set.pop("U", None)
        if self.agent[0] == self.env_0-1: action_set.pop("D", None)
        if self.agent[1] == 0: action_set.pop("L", None)
        if self.agent[1] == self.env_1-1: action_set.pop("R",None)


        #policy and action
        for action in action_set:
            #print(action)
            action_reward = (1 - self.qtable.alpha) * self.qtable.get_q(self.agent[0],self.agent[1],action) +  self.qtable.alpha *  (self.reward(action) + self.qtable.alpha * self.q_max(self.find_position(action)))
            #print(action_reward)
            self.qtable.set_q(self.agent[0],self.agent[1],action,action_reward)
            action_set.update({action:action_reward})
        
        print(action_set)
        
        #Move agent
        self.visited[self.agent[0]][self.agent[1]] += 1
        action = max(action_set, key=action_set.get)
        print(">->",action)
        self.agent = self.find_position(action)
        
    def eliminate_game(self):
        return self.reload()
    
    def win(self):
        if len(self.flags)==0 and self.agent==self.target:
            return 1
        return 0
    
    def lose(self):
        if self.q_max(self.agent)<=self.env_lose:
            return 1
        return 0
    
    def reward(self,action):
        """
        actions: [L: left,
                  U: up,
                  R: right,
                   D: down
        """

        new_agent = self.find_position(action)
            
        if self.env[new_agent[0]][new_agent[1]]=="B":
            return self.env_lose*2
        elif self.env[new_agent[0]][new_agent[1]]=="O":
            return 0
        elif self.env[new_agent[0]][new_agent[1]]=="F":
            return 0.1*(self.env_size/self.flag_num)
        elif self.env[new_agent[0]][new_agent[1]]=="T":
            return self.env_size
        elif self.visited[new_agent[0]][new_agent[1]]>=2:
            return (-2*self.visited[new_agent[0]][new_agent[1]])/self.env_size
        elif self.visited[new_agent[0]][new_agent[1]]>=1:
            return -1.1/self.env_size
        else:
            return -1.0/self.env_size
    '''
    def take_an_action(self):
        action_set = ["L","U","R","D"]

        if self.agent[0] == 0: action_set.remove("L")
        if self.agent[0] == self.env_0: action_set.remove("R")
        if self.agent[1] == 0: action_set.remove("U")
        if self.agent[1] == self.env_1: action_set.remove("D")


        #policy and action

        self.agent = self.find_position(action)
    '''
                                                       
    def q_max(self,new_agent):
        all_q = []
        for action in ["L","U","R","D"]:
            all_q.append(self.qtable.get_q(self.find_position(action,new_agent)[0],self.find_position(action,new_agent)[1],action))
            #print(action,new_agent,all_q[-1])
        return max(all_q)
                                                       
    def find_position(self,action,agent=None):
        if agent==None:
            if   action=="L": return [self.agent[0],self.agent[1]-1]
            elif action=="U": return [self.agent[0]-1,self.agent[1]]
            elif action=="R": return [self.agent[0],self.agent[1]+1]
            elif action=="D": return [self.agent[0]+1,self.agent[1]]
        else:
            if   action=="L": return [agent[0],agent[1]-1]
            elif action=="U": return [agent[0]-1,agent[1]]
            elif action=="R": return [agent[0],agent[1]+1]
            elif action=="D": return [agent[0]+1,agent[1]]
            
    def set_table(self,landa,alpha):
        self.qtable = qtable(self.env_0,self.env_1,landa,alpha)

    
