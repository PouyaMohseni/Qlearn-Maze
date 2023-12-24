# Qlearn-Maze

## Overview

In this project we utilize Q-learning, a reinforcement learning technique, to solve maze problems.
For the complete report, including detailed explanations and implimentation,please refer to [Part 1](https://pouyamohseni.medium.com/the-maze-reinforcement-learning-part-1-2bf53e56c94b)
and [Part 2](https://pouyamohseni.medium.com/the-maze-reinforcement-learning-part-2-3f1fd8254e03).

### Reinforcement Learning

Reinforcement learning (RL) is a sub-field of Artificial Intelligence and Machine Learning. In RL, an agent aims to learn a policy function that maximizes its rewards while taking actions. The reward function depends on the agent's state and the action it chooses. Policy function, on the other hand, determines the action based on the state and past knowledge of rewards.

- **r(s, a) → r** (Reward)
- **δ(s, a) → s'** (Transition)

Reinforcement Learning differs from Supervised Learning, which uses pre-labeled data, and Unsupervised Learning, which typically works with unlabeled data. RL involves agents exploring their environment, taking actions, and receiving rewards, making it the third branch of machine learning.

### Q-Learning

Q-Learning is one approach to implement Reinforcement Learning. In Q-Learning, the agent learns from previous experiences based on the reward function. It uses a learning rate (alpha) and other parameters (lambda) to update its experiences by taking new actions and perceiving rewards. A table is created for each state-action pair, initialized with zero, and updated during training.

**Q(s, a) ← Q(s, a) + α[r + γ max Q(s', a') – Q(s, a)]**

For more information on Reinforcement Learning or precise details about the Q-Learning algorithm, refer to the citations.

## The Maze Problem

The maze problem, or "rat in a maze," involves finding a path from a starting point to a target while avoiding obstacles. In the RL version, the rat represents the agent, and the reward function is designed to guide the agent to find the fastest path to the target. Below is a 5x5 maze with the agent at [0,0] and the target at [4,4].

In this implementation, additional flags are introduced, which the agent must collect before reaching the target. The reward function is modified accordingly. The primary objective remains the same: reaching the target as quickly as possible. Below is the updated 5x5 maze with two flags at [1,1] and [2,3].

## States

States are represented as cells within the maze, including obstacles. The agent can take actions such as left, up, right, and down. To ensure that the agent stays within the maze, it is penalized if it moves off the board. Alternatively, the number of actions the agent can take when near the edges can be limited.

## Reward Function

The reward function serves two purposes: ensuring the agent reaches the target and encouraging the fastest path. The agent is penalized for revisiting states to prevent it from wandering back and forth. However, the agent is still allowed to explore by revisiting a state once. The reward function is designed to punish excessive revisits.

- When the agent completes the task, a substantial reward is given.
- The game ends if the agent reaches the target or cannot estimate a valuable future reward (greater than -1).

## Adding Flags

To add complexity to the game, flags are introduced. Winning the game now requires the agent to reach the target while collecting all flags. When the agent enters a state where a flag is not collected, the reward function offers higher rewards, motivating the agent to gather flags while heading to the target.

The agent is trained in the previously introduced maze with flags as part of the gameplay.

---
