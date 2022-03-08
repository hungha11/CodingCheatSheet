import streamlit as st


def Autotrader():
    main()
    sidebar()

def main():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.code("""
        Structure of the project:
    your_trading_project/
    |- run_script.py                      # Run script to deploy trading bots
    |- config/
    |    |- GLOBAL.yaml                   # Global configuration file
    |    |- your_strategy1_config.yaml    # Strategy-specific configuration file
    |    |- your_strategy2_config.yaml    # Strategy-specific configuration file
    |- strategies/
    |    |- your_strategy1.py             # Strategy 1 module, containing strategy logic
    |    |- your_strategy2.py             # Strategy 1 module, containing strategy logic
        """)

    with col2:
        st.code("""
        Simple strategy:
        # Import packages

class SimpleMACD:
    def __init__(self, params, data, instrument):
        ''' Initialise the strategy here '''
        ...

    def generate_signal(self, i, current_position):
        ''' Define the trading strategy to determine entry signals '''
        ...
        return signal_dict
    
    def generate_exit_levels(self, signal, i):
        ''' Function to determine stop loss and take profit levels '''
        ...
        return exit_dict
        """)
        st.write('More explicit code:')

        st.code("""
        # Import packages
from finta import TA
from autotrader.lib import indicators

class SimpleMACD:

    def __init__(self, params, data, pair):
        ''' Define all indicators used in the strategy '''
        self.name   = "Simple MACD Trend Strategy"
        self.data   = data
        self.params = params
        
        # 200EMA
        self.ema    = TA.EMA(data, params['ema_period'])
        
        # MACD
        self.MACD = TA.MACD(data, self.params['MACD_fast'], 
                            self.params['MACD_slow'], self.params['MACD_smoothing'])
        self.MACD_CO        = indicators.crossover(self.MACD.MACD, self.MACD.SIGNAL)
        self.MACD_CO_vals   = indicators.cross_values(self.MACD.MACD, 
                                                      self.MACD.SIGNAL,
                                                      self.MACD_CO)
        # Construct indicators dict for plotting
        self.indicators = {'MACD (12/26/9)': {'type': 'MACD',
                                              'macd': self.MACD.MACD,
                                              'signal': self.MACD.SIGNAL},
                           'EMA (200)': {'type': 'MA',
                                         'data': self.ema}}
        
        # Price swings
        self.swings     = indicators.find_swings(data)
        """)

        st.code("""
        def generate_signal(self, i, current_position):
        ''' Define strategy to determine entry signals '''
        
        order_type  = 'market'
        signal_dict = {}
        related_orders  = None
        
        if self.data.Close.values[i] > self.ema[i] and \    # Price is above 200 EMA
            self.MACD_CO[i] == 1 and \                      # MACD cross above signal line
            self.MACD_CO_vals[i] < 0:                       # MACD cross occured below zero
                # Long entry signal
                signal = 1
                
        elif self.data.Close.values[i] < self.ema[i] and \  # Price is below 200 EMA
            self.MACD_CO[i] == -1 and \                     # MACD cross below signal line
            self.MACD_CO_vals[i] > 0:                       # MACD cross occured above zero 
                # short entry signal
                signal = -1

        else:
            # No signal
            signal = 0
        
        # Calculate exit targets
        exit_dict = self.generate_exit_levels(signal, i)
        
        # Construct signal dictionary
        signal_dict["order_type"]   = order_type
        signal_dict["direction"]    = signal
        signal_dict["stop_loss"]    = exit_dict["stop_loss"]
        signal_dict["stop_type"]    = exit_dict["stop_type"]
        signal_dict["take_profit"]  = exit_dict["take_profit"]
        
        return signal_dict
        
                """)
        st.code("""
         def generate_exit_levels(self, signal, i):
        ''' Function to determine stop loss and take profit levels '''
        
        stop_type   = 'limit'
        RR          = self.params['RR']
        
        if signal == 0:
            stop    = None
            take    = None
        else:
            if signal == 1:
                stop    = self.swings.Lows[i]
                take    = self.data.Close[i] + RR*(self.data.Close[i] - stop)
            else:
                stop    = self.swings.Highs[i]
                take    = self.data.Close[i] - RR*(stop - self.data.Close[i])
                
        
        exit_dict   = {'stop_loss'    : stop, 
                       'stop_type'    : stop_type,
                       'take_profit'  : take}
        
        return exit_dict
                """)

    with col3:
        st.code("""
    Configuration file:
        NAME: 'Simple_macd_strategy'
        MODULE: 'macd'
        CLASS: 'SimpleMACD'
        INTERVAL: '1h'
        SIZING: 'risk'
        RISK_PC: 1.5
        PARAMETERS:
          ema_period: 200
          MACD_fast: 12
          MACD_slow: 26
          MACD_smoothing: 9
          
          # Exit level parameters
          RR: 1.5
        
        WATCHLIST: ['EURUSD=X']    
        """)


def sidebar():
    st.sidebar.write('Autotrader is a financial python package. Which is really useful for backtesting, optimising and '
                     'connecting to broker.')
    st.sidebar.write('This is mostly used code from this package.')


