# From official Mesa tutorial: https://mesa.readthedocs.io/en/stable/tutorials/intro_tutorial.html

import mesa

import numpy as np

import matplotlib.pyplot as plt


class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        #print(f"Hi, I am agent {self.unique_id}. My wealth is {self.wealth}.")

        # if self.wealth == 0:
        #     return
        
        #other_agent = self.random.choice(self.model.schedule.agents)
        #other_agent.wealth += 1

        #self.wealth -= 1

        self.move()
        if self.wealth > 0:
            self.give_money()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )

        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1

class MoneyModel(mesa.Model):
    """A model with some number of agents"""

    def __init__(self, N, width, height):
        self.num_agents = N
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(width, height, True)

        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.data_collector = mesa.DataCollector(
            model_reporters={"Gini": MoneyModel.compute_gini},
            agent_reporters={"Wealth": "wealth"}
        )

    def step(self):
        """Advance the model by one step"""
        self.data_collector.collect(self)
        self.schedule.step()

    @staticmethod
    def compute_gini(model):
        agent_wealths = [ agent.wealth for agent in model.schedule.agents ]
        x = sorted(agent_wealths)
        N = model.num_agents
        B = sum( xi * (N - i) for i, xi in enumerate(x) ) / (N * sum(x))
        return 1 + (1 / N) - 2 * B


if __name__ == "__main__":
    # all_wealth = []

    # for j in range(100):
    #     model = MoneyModel(10)

    #     for _ in range(10):
    #         model.step()

    #     for agent in model.schedule.agents:
    #         all_wealth.append(agent.wealth)

    #agent_wealth = [ a.wealth for a in model.schedule.agents ]
    #plt.hist(agent_wealth)

    # plt.hist(all_wealth, bins=range(max(all_wealth)  + 1))
    # plt.show()

    # model = MoneyModel(50, 10, 10)
    # for i in range(20):
    #     model.step()

    # agent_counts = np.zeros( (model.grid.width, model.grid.height) )
    # for cell in model.grid.coord_iter():
    #     cell_content, x, y = cell
    #     agent_count = len(cell_content)
    #     agent_counts[x][y] = agent_count

    # plt.imshow(agent_counts, interpolation="nearest")
    # plt.colorbar()
    # plt.show()

    model = MoneyModel(50, 10, 10)
    for i in range(100):
        model.step()

    gini = model.data_collector.get_model_vars_dataframe()
    gini.plot()
    plt.show()

    agent_wealth = model.data_collector.get_agent_vars_dataframe()
    print(agent_wealth)

    gini.to_csv("model_gini.csv")
    agent_wealth.to_csv("agent_wealth.csv")
