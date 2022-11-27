# Qlearn-Maze
A Qlearn approach to solve maze problem with Reinforcement Learning


# Reinforcement Learning:

Reinforcement learning (RL) refers to a sub-field of Artificial Intelligence and also Machine Learning in which the machine – or the agent -- tries to learn a policy function that maximizes its rewards while taking action. In other words, the reward function that the agent tries to maximize is determined by the state of the agent and the action that it decides to take. Policy function, though, determines what action the agent should take based on its state and its previous knowledge of rewards. [1]
 
r(s, a)  r
δ(s, a)  s’

Reinforcement Learning is different from Supervised Learning in which the machine generalizes pre-labeled training data and Unsupervised Learning which typically works with unlabeled data. In the Reinforcement Learning problems, the agent finds the hidden structures of its environment by taking actions and being signaled by a reward. Therefore, RL is considered the third branch of machine learning. [1]

# Q-Learning:
Many approaches have been taken to implement Reinforcement Learning in order to have an agent obtain a policy function that maximizes its reward in each pair of states and actions. One of which is Q-Learning. In this approach, the agent tries to learn from its environment by relaying on its previous experiences from the reward function. Having a learning rate as (alpha) and something else as (landa) the previous experiences are updated by taking new actions and precepting the reward function.
Q(s, a)  Q(s, a) + α[r + γ max Q(s’, a’) – Q(s, a)]
In other words, a table is generated for each state and action pair and then, each register is initialized with zero – for now just consider the reward function non-positive – and would be updated throughout the training phase of the algorithm’s implementation. 

For more information on Reinforcement Learning or precise information about Q-Learning Algorithm follow the citations. 
The problem: Maze
The objective of the maze problem -- or rat in a maze – is to find a path for the rat to the cheese while the path is not blocked by any obstacle. In the RL version, we consider the rat as the agent, and then we define the reward function in a way that the agent gets able to determine the fastest path to the finishing point – or in this terminology, the target. Below is a 5*5 maze with the agent and the target locating at [0,0], and [4,4], respectively. 

We, then, integrate the problem by defining flags that are supposed to be collected by the agent before arriving at the target. Therefore, an amendment to the previous reward function is necessary. The objective, though, reminds the same: approaching the target in the fastest way. Below is the introduced 5*5 maze with two flags locating at [1,1], and [2,3], respectively.

# States
States are defined as the registers on the maze – including the obstacles, etc. We can consider that agent can take any action in the set, {left, up, right, down}, and then we would impose the agent high punishment if it is off-the-board to secure staying in the maze. Another approach, though, is to decrease the number of actions that the agent can take when it is adjacent to the edges – it is clear that obstacles cannot be considered edges. 

# Reward Function:
The Reward Function must satisfy two things: first, the agent is arriving at the target, and second, the agent takes the fastest path. Thus, we want to prevent our agent from wandering around back and forth between a couple of states. Therefore, we try to punish the agent when it is visiting a visited state. Though we do not want to restrict the agent from exploring so, re-visiting a state just one time would not matter.  The reward function is introduced below; note how the agent is punished according to the number of visits to a state.
//
Moreover, the agent should be rewarded when it completes the task. Therefore, a huge amount of reward is allocated when the target is approached.
//
In addition, the game is eliminated when the agent approaches the target or when the agent cannot estimate a valuable future reward – more than -1.  
//
In the following the simple introduced 5*5 maze is solved by the algorithm and the reward function.
//

# Adding Flags
We change the reward function in order to integrate flags into the game. Firstly, winning the game is changed: now the agent must approach the target while all flags are achieved. Secondly, when the agent enters the state where its flag is not achieved, the reward function allocates more rewards to the agent. In this way, the agent is forced to obtain flags on its way to the target state.
//
Then, the agent is trained in the previously introduced maze as follows: 
//

# What’s next?
Movable obstacles are introduced which are moved by the agent when they move toward them. These objects are two sides of a sword; they can be used to open a path or block it fully. Thus, the reward function should be determined precisely.   
