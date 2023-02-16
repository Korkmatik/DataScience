import agentpy as ap


class MyAgent(ap.Agent):

    def setup(self):
        self.my_attribute = self.p.my_parameter

    def agent_method(self):
        pass


class MyModel(ap.Model):

    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, MyAgent)

    def step(self):
        self.agents.agent_method()

    def update(self):
        self.agents.record("my_attribute")

    def end(self):
        self.report("my_measure", 1)


if __name__ == "__main__":
    # parameters = {
    #     "my_parameter": 123,
    #     "agents": 10,
    #     "steps": 10,
    # }

    # model = MyModel(parameters)
    # results = model.run()

    parameters = {
        "my_parameter": 42,
        "agents": ap.IntRange(10, 20),
        "steps": ap.IntRange(10, 20),
    }

    sample = ap.Sample(parameters, n=5)
    exp = ap.Experiment(MyModel, sample, iterations=2, record=True)
    results = exp.run()

    print(results)
