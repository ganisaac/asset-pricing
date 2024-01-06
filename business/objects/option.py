class Option:
    def __init__(self,name, S0, K, T,r=0.05):
        self.name = name.upper()
        self.S0 = S0      # Underlying asset price
        self.K = K        # Option strike price
        self.T = T        # Time to expiration
        self.r = r        # Risk-free interest rate

