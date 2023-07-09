import gymnasium as gym


def theta_policy(obs):
    theta = obs[2]
    return 1 if theta > 0 else 0

def omega_policy(obs):
    omega = obs[3]
    return 1 if omega > 0 else 0

def theta_omega_policy(obs):
    theta, omega = obs[2], obs[3]
    if abs(theta) < 0.05:
        return 1 if omega > 0 else 0
    else:
        return 1 if theta > 0 else 0
    
class PDController:
    def __init__(self, kp, kd, goal):
        self.kp = kp
        self.kd = kd
        self.goal = goal
        self.last_error = 0

    def observe(self, x):
        error = self.goal - x
        d_error = error - self.last_error
        self.last_error = error
        
        control_signal = self.kp * error + self.kd * d_error
        return control_signal
    
    def reset(self):
        self.last_error = 0

class Controller:
    def __init__(self):
        self.cart = PDController(kp=1, kd=100, goal=0)
        self.pole = PDController(kp=5, kd=100, goal=0)

    def observe(self, cart_position, pole_angle):
        u_cart = self.cart.observe(cart_position)
        u_pole = self.pole.observe(pole_angle)
        action = 1 if u_cart + u_pole < 0 else 0
        return action
    
    def reset(self):
        self.cart.reset()
        self.pole.reset()

def run_game():
    env = gym.make("CartPole-v1", render_mode="human")
    policy = Controller()

    observation, info = env.reset()

    episode_reward = 0
    for _ in range(1000):
        action = policy.observe(observation[0], observation[2])
        observation, reward, terminated, truncated, info = env.step(action)
        episode_reward += reward

        if terminated or truncated:
            print(f"episode reward: {episode_reward}")
            episode_reward = 0

            observation, info = env.reset()
            policy.reset()

    env.close()


if __name__ == "__main__":
    run_game()
