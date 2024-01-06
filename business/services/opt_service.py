from business.objects.option import Option
from business.objects.person import Person
import pandas as pd
import numpy as np

class OptionsService:
    def get_options_data(self, option,person):
        """
        Get options data for a given symbol and time period.
        """
        if option.name=="APPLE":
            name="aapl"
        elif option.name=="AMAZON":
            name="amzn"
        elif option.name=="ALI BABA":
            name="baba"
        elif option.name=="GOOGLE":
            name="googl"
        elif option.name=="META":
            name="meta"
        elif option.name=="MICROSOFT":
            name="msft"
        elif option.name=="SONY":
            name="sony"
        elif option.name=="TESLA":
            name="tsla"
        
        df= pd.read_csv(f'data/ListAllOptions{name}.csv')
        df_filtered=df[df['Type']==person.type]
        return df_filtered
    
    def calculate_historical_volatility(self,option,person,window=252):
        """
        Calculate the annualized historical volatility of a stock.
        """
        df=self.get_options_data(option,person)
        prices = df['Last Price']
        log_returns = np.log(prices / prices.shift(1))
        daily_std = np.std(log_returns)
        annualized_std = daily_std * np.sqrt(window)
        return annualized_std


if __name__ == "__main__":
    P=Person('Call')
    O=Option('Microsoft', 100, 100, 1)
    opt_service=OptionsService()
    print("Options Data:")
    opt_service.get_options_data(O,P)
    print("Volatility:")
    print(opt_service.calculate_historical_volatility(O,P))
    