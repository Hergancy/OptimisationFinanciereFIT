# Class Parameters, contains all the information about parameters

class Parameters:
    # Set de paramètres
    unitProductPrice = 0
    unitInventoryCost_t = []
    unitProductionCost_t = []
    fixedSetupCost = 0
    unitRawMaterialCost = 0
    paymentDelayFromClient = 0
    paymentDelayToSupplier = 0
    discountRate_t = []
    interestRateForFinancialOWCR_t = []

    def __init__(self, df):
        self.unitProductPrice = df.iat[3, 1]
        for i in range(3, len(df)):
            self.unitInventoryCost_t.append(df.iat[i, 2])
        for i in range(3, len(df)):
            self.unitProductionCost_t.append(df.iat[i, 3])
        self.fixedSetupCost = df.iat[3, 4]
        self.unitRawMaterialCost = df.iat[3, 5]
        self.paymentDelayFromClient = df.iat[3, 6]
        self.paymentDelayToSupplier = df.iat[3, 7]
        for i in range(3, len(df)):
            self.discountRate_t.append(df.iat[i, 8])
        for i in range(3, len(df)):
            self.interestRateForFinancialOWCR_t.append(df.iat[i, 9])

    # getters
    def get_unitProductPrice(self):
        return self.unitProductPrice

    def get_unitInventoryCost_t(self):
        return self.unitInventoryCost_t

    def get_unitProductionCost_t(self):
        return self.unitProductionCost_t

    def get_fixedSetupCost(self):
        return self.fixedSetupCost

    def get_unitRawMaterialCost(self):
        return self.unitRawMaterialCost

    def get_paymentDelayFromClient(self):
        return self.paymentDelayFromClient

    def get_paymentDelayToSupplier(self):
        return self.paymentDelayToSupplier

    def get_discountRate_t(self):
        return self.discountRate_t

    def get_interestRateForFinancialOWCR_t(self):
        return self.interestRateForFinancialOWCR_t

    # setters
    def set_unitProductPrice(self, price):
        self.unitProductPrice = price

    def set_unitInventoryCost_t(self, cost):
        self.unitProductionCost_t = cost

    def set_unitProductionCost_t(self, cost):
        self.unitInventoryCost_t = cost

    def set_fixedSetupCost(self, cost):
        self.fixedSetupCost = cost

    def set_unitRawMaterialCost(self, cost):
        self.unitRawMaterialCost = cost

    def set_paymentDelayFromClient(self, delay):
        self.paymentDelayFromClient = delay

    def set_paymentDelayToSupplier(self, delay):
        self.paymentDelayToSupplier = delay

    def set_discountRate_t(self, rate):
        self.discountRate_t = rate

    def set_interestRateForFinancialOWCR_t(self, rate):
        self.interestRateForFinancialOWCR_t = rate
