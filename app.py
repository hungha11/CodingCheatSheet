import  streamlit as st


# Initial page config
st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

#Home page section
def Homepage():
    Home_sidebar()
    Home_body()

def Home_sidebar():
    st.sidebar.write('This is side bar')

def Home_body():
    st.write('This is home body')




# Streamlit section
def Streamlit():
    Streamlit_sidebar()
    Streamlit_body()

    return None

def Streamlit_sidebar():
    st.sidebar.write('This is Streamlit sidebar')

def Streamlit_body():
    st.write('This is Streamlit body')
    col1, col2, col3 = st.columns(3)
    col1.subheader('Frequently used funtions')
    col1.code('''
    #Add the html 
    HtmlFile = open("html/indexChart.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=600, width=1000, )
    ''')


# Algo Trade section
def AlgoTrade():
    Algo_sidebar()
    Algo_body()

    return None

def Algo_sidebar():

    st.sidebar.header("Sidebar")
    st.sidebar.markdown("""
    ## Important packages
    - vnquant: for stock price data
    - investpy: for stock price data
    - pandas: for dataframe
    - numpy: for data manipulation
    - streamlit: for UI
    - scipy: for math
    - matplotlib: for plotting
    - mplfinance: for candlestick
    """)
    st.sidebar.markdown("""
    ## Sidebar
    This is a sidebar
    """)

    return None

def Algo_body():
    col1, col2, col3 = st.columns(3)
    # Display text
    col1.subheader('Symbol collection')
    col1.code('''
    def collect_symbol(index):
        symbol_strings = []
        if index == 'VN30':
            stocks = pd.read_csv('VN30.csv')
            symbol_groups = list(stocks['Ticker'])
            for i in range(0, len(symbol_groups)):
                symbol_strings.append(symbol_groups[i])
                # print(symbol_strings[i])
        elif index == 'VN100':
            stocks = pd.read_csv('VN100.csv')
            symbol_groups = list(stocks['Ticker'])
            for i in range(0, len(symbol_groups)):
                symbol_strings.append(symbol_groups[i])
                # print(symbol_strings[i])
        else:
            print('Wrong index.\nPlease try again.')
        ''')
    col1.subheader('Close Price data')
    col1.code('''
    import vnquant.DataLoader as dl
    start = '2010-01-01'
    now  = datetime.now()
    end = now.strftime("%Y-%m-%d")
    loader = dl.DataLoader(collect_symbol(index), start,end, data_source='VND', minimal=True)
    data = loader.download()
    close_data = data['close'].dropna()
        ''')
    # Display data
    col1.subheader('Display data')
    col1.code('''
    st.dataframe(my_dataframe)
    st.table(data.iloc[0:10])
    st.json({'foo':'bar','fu':'ba'})
    st.metric(label="Temp", value="273 K", delta="1.2 K")
        ''')

    col2.subheader('Risk analysis')
    col2.code('''
    #Data preparation
    import investpy
    import pandas as pd
    def get_data_stock(stock_name, start_date):
        start_date = start_date
        end_date = datetime.datetime.today().strftime('%Y-%m-%d')
        loader = dl.DataLoader(stock_name , start_date, end_date, data_source='VND', minimal=True)
        data = loader.download()
        return data

    def get_index_data(index_name, start_date):
        start_date = datetime.datetime.strptime(start_date,'%Y-%m-%d').strftime('%d/%m/%Y')
        end_date = datetime.datetime.today().strftime('%d/%m/%Y')
        index = investpy.get_index_historical_data(index_name,country='vietnam',from_date=start_date,to_date=end_date)
        return index

    def data_collection():
        # Get index data
        index = get_index_data(index_name, start_date)
        index_data = index.reset_index()
        index_data = index_data.rename(columns={'Date':'date','Open':'open' ,'Close':'close','High':'high','Low':'low','Volume':'volume'})
        index_data['date'] = pd.to_datetime(index_data['date'])
        index_data = index_data.set_index('date')
        index_data = index_data.drop('Currency', axis=1)
        index_data['pctchange'] = index_data['close'].pct_change()
        index_data.dropna(inplace=True)

        # Get stock data
        stock = get_data_stock(self.stock_name, self.start_date)
        stock_data = stock.reset_index()
        stock_data = stock_data.rename(columns={'Date':'date', 'Close':'close'})
        stock_data['date'] = pd.to_datetime(stock_data['date'])
        stock_data = stock_data.set_index('date')
        stock_data = stock_data[['open','high','low','close','volume']]
        stock_data['pctchange'] = stock_data['close'].pct_change()
        stock_data.dropna(inplace=True)

        return index_data, stock_data
    ''')

    col2.subheader('Alpha and Beta calculation')
    col2.code('''
        def calculate_alpha():
            index_data, stock_data = data_collection()
            def beta(data, data_index):
                return np.cov(data, data_index)[0, 1] / np.var(data_index)
            # Calculate alpha
            def alpha(data, data_index):
                return np.mean(data) - beta(data, data_index) * np.mean(data_index)
            alpha_stock = alpha(stock_data['pctchange'], index_data['pctchange'])
            alpha_stock = round(alpha_stock,5) *100
            stock_alpha = 'Alpha: ' + str(alpha_stock).format('.2f') + '%'
            return stock_alpha
    ''')


    #col3 section
    col3.subheader('Frequently used functions')
    col3.code('''
    #Indexing Class
    class ETF_builder():
        def __init__(self, index):
            self.index = index
    
        def get_index(self):
            if self.index == 'VN30':
                stock_list = pd.read_csv('index/VN30.csv')
                stock_list = stock_list['Ticker'].tolist()
                return stock_list
    
    
            elif self.index == 'VN100':
                stock_list = pd.read_csv('index/VN100.csv')
                stock_list = stock_list['Ticker'].tolist()
                return stock_list
    
    
        def indexing(self):
            company_list = self.get_index()
    
            my_columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Weight' ,'Number of Shares to Buy', ]
            company_dataframe = pd.DataFrame(columns=  my_columns)
    
            for company in company_list:
                now = dt.datetime.now().strftime("%d/%m/%Y")
                start = '01/02/2022'
                stock = investpy.get_stock_historical_data(company, country='vietnam', from_date=start, to_date=now)
                lastestPrice = stock['Close'][-1]
    
                market_cap = investpy.get_stock_information(company, country='vietnam')
                market_cap = market_cap['Market Cap'][0]
                market_cap = round(market_cap, 1)
                company_dataframe = company_dataframe.append(
                    pd.Series(
                    [company,
                    lastestPrice,
                    market_cap,
                    'n/a',
                    'n/a'], index= my_columns
                    ),ignore_index=True
                )
            for i in range(0,len(company_dataframe.index)):
                company_dataframe.loc[i,'Weight'] = company_dataframe.loc[i,'Market Capitalization']/company_dataframe['Market Capitalization'].sum()
                company_dataframe.loc[i,'Weight'] = round(company_dataframe.loc[i,'Weight'] * 100 ,2)
                company_dataframe.loc[i,'Weight'] = str(company_dataframe.loc[i,'Weight']) + '%'
    
    
            return company_dataframe
    
    ''')



    return None



def MachineLearning():
    ML_sidebar()
    ML_body()

def ML_sidebar():
    st.sidebar.write("""***""")

    st.sidebar.write("""
    ### Some of the inportant resources:
    - #### Vietnamese sources:
        - [Pham Dinh Khanh](https://phamdinhkhanh.github.io/deepai-book/intro.html)
        - [Machine learning co ban](https://machinelearningcoban.com)
        
    - #### English sources:
        - [Machine learning mastery](https://machinelearningmastery.com)
        - [100 days of  ML code] (https://github.com/Avik-Jain/100-Days-Of-ML-Code)
    """)
    st.sidebar.write("""***""")
    st.sidebar.write("""
    ### Hosting platform
    - [Google Collab](https://colab.research.google.com/notebooks/welcome.ipynb)
    """)


def ML_body():
    st.write('Machine Learning')
    st.write('Still working on it')



if __name__ == "__main__":



    st.markdown(f'''
                <style>
                    section[data-testid="stSidebar"] .css-ng1t4o {{width: 16rem;}}
                    section[data-testid="stSidebar"] .css-1d391kg {{width: 16rem;}}
                </style>
            ''', unsafe_allow_html=True)


    page = st.sidebar.selectbox('Choose a page',
                                ['Home', 'Streamlit' ,'Algorithmic Trading','Machine learning'])
    #page title
    st.markdown("<h1 style='text-align: center; color: orange;'>Coding cheat sheet</h1>", unsafe_allow_html=True)

    #background colot

    if page == 'Home':
        st.title('Home')
        st.markdown('This is a home page')
        Homepage()
    if page == 'Streamlit':
        Streamlit()
    if page == 'Algorithmic Trading':
        st.title('Algorithmic Trading')
        AlgoTrade()

    if page == 'Machine learning':
        st.title('Machine learning')
        MachineLearning()