# Class Demand, contains all the information about the demand

class Demand:
    horizonLength = 0
    demand_t = []

    def __init__(self, df):
        self.horizonLength = df.iat[1,1]

        for i in range(4, len(df)):
            self.demand_t.append(df.iat[i, 1])

    def get_horizon_length(self):
        return self.horizonLength

    def get_demand(self):
        return self.demand_t

    def set_horizon_length(self, df):
        self.horizonLength = df.iat[1,1]

    def set_demand(self, df):
        for i in range(4, len(df)):
            self.demand_t.append(df.iat[i, 1])
