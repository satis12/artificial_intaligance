import numpy as np

# Define the environment
num_states = 4
num_actions = 4

# Define the Q-table and initialize it with zeros
Q = np.zeros((num_states, num_actions))

# Define the rewards for each state-action pair
rewards = np.array([
    [-1, -1, -1, -1],  # State 0
    [-1, -1, -1, -1],  # State 1
    [-1, -1, -1, -1],  # State 2
    [-1, -1, -1, 10]   # State 3 (goal state)
])

# Define the learning parameters
learning_rate = 0.2
discount_factor = 1.9
num_episodes = 2000

# Q-learning algorithm
for episode in range(num_episodes):
    state = np.random.randint(0, num_states)  # Initial state

    while state != 3:  # Continue until the agent reaches the goal state
        action = np.random.randint(0, num_actions)  # Choose a random action
        next_state = action  # Transition to the next state (in this example, it's deterministic)

        # Update the Q-table using the Q-learning update rule
        Q[state, action] = Q[state, action] + learning_rate * (
            rewards[state, action] + discount_factor * np.max(Q[next_state, :]) - Q[state, action]
        )

        state = next_state  # Update the current state

# After training, you can use the Q-table to make decisions
# For example, to find the optimal policy, choose the action with the highest Q-value in each state
optimal_policy = np.argmax(Q, axis=1)
print("Optimal Policy:", optimal_policy)
