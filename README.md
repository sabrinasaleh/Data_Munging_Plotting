Data Analysis & Visualization Bootcamp | UT-Austin McCombs | Fall 2020
# **Foreign Direct Investment (FDI) in USA**
![title](Images/image_title.jpg)

## Research Question
* Total stock of Inward-FDI in the USA in 2019: 4458.36 (billion USD) 
* Total stock of Inward-FDI in the USA in 2018: 4127.18 (billion USD)
    - Which countries invest more in the USA? 

## Hypotheses:       
1. Countries' economic level impacts their FDI in the USA. 
2. Countries' innovation & technology impacts their FDI in the USA.
3. Countries' business infrastructure impacts their FDI in the USA.

## Variables, Measures, & Dataset 
* Time of Analysis: Year 2018
   
* Dependent Variable: FDI in the USA
    - Measure: Total stock of FDI by countries in the USA (in million USD)
    - Dataset: Bureau of Economic Analysis; https://www.bea.gov
    
    
* Independent Variable (H1): Investing countries' state of economy
    - Measure: Gross Domestic Product (GDP) of investing countries (in million USD)
    - Dataset: World Bank API; https://pypi.org/project/world-bank-data/
    
    
* Independent Variable (H2): Investing countries' state of innovation & technology
    - Measure: High technology exports by investing countries (in million USD)
    - Dataset: World Bank; https://data.worldbank.org
    
    
* Independent Variable (H3): Investing countries' business infrastructure
    - Measure: Doing Business Indicator of investing countries (in score of 100)
    - Dataset: World Bank; https://data.worldbank.org

## Technologies for Data Analysis 
* pandas
* numpy
* world_bank_data, requests, & json
* scipy.stats
* LinearRegression from sklearn.linear_model
* plotly
* plotly.express
* mapbox_token

## Link of Notebook  
* [main.ipynb](https://github.com/sabrinasaleh/Project_FDI_USA/blob/master/main.ipynb): Notebook with all the codes for data cleaning, merging, analysis, and visualization.

## Sample Size & Basic Statistics: 180 Countries
![basic_stat](Images/stat_table_screen.PNG)

## Rank of Countries by Dependent Variable  
![FDI_Top](Images/FDI_USA_top25.png)

## Rank of Countries by Independent Variables  
![GDP_Top](Images/GDP_top25.png) 
![IT_Top](Images/innov_tech_top25.png)  
![DB_Top](Images/doing_busn_top25.png)

## Dependent Variable Mean by Regions 
![FDI_avg](Images/Mean_FDI_USA_region.png)

## Independent Variables Means by Regions
![GDP_avg](Images/Mean_GDP_region.png)
![IT_avg](Images/Mean_IT_region.png)
![DB_avg](Images/Mean_DB_region.png)

## Regional Rank of Countries for FDI in USA
![europe_fdi](europe/europe_top_10_fdi_bar.png)
![asia_fdi](Michael_Tasks/presentation/Top10AsiaFDI.png)
![latin_fdi](Images/latin_top_fdi.png)
![africa_fdi](Bruce_task/african_fdi_bar.png)

## H1: Countries' economic level impacts their FDI in the USA
* The correlation between FDI in USA and GDP by countries is 0.35
* The linear regression model for FDI in USA vs GDP by countries is y = 22874.11 + 0.02x with R-Square=0.13
![GDP_scatter](Images/GDP_scatter_screen.PNG)

## H2: Countries' innovation & technology impacts their FDI in the USA
* The correlation between FDI in USA and Innovation & Technology by countries is 0.23
* The linear regression model for FDI in USA vs Innovation & Technology by countries is y = 29450.14 + 0.29x with R-Square=0.05
![IT_scatter](Images/IT_scatter_screen.PNG)

## H3: Countries' business infrastructure impacts their FDI in the USA
* The correlation between FDI in USA and Doing Business Indicator by countries is 0.35
* The linear regression model for FDI in USA vs Doing Business Indicator by countries is y = -185483.5 + 3343.94x with R-Square=0.12
![DB_scatter](Images/DB_scatter_screen.PNG)

## Data Visualization in the Global Map
![FDI_map](Images/fdi_map_screen.PNG)
![GDP_map](Images/GDP_map_screen.PNG)
![IT_map](Images/IT_map_screen.PNG)
![DB_map](Images/DB_map.png)

## Analysis of Observations & Results
* The pilot/preliminary study indicates that the correlation and regression coefficients are positive for the three independent variables.
* For GDP and Innovation & Technology, the coefficients of regressions are relatively small. China plays a big role in causing the flatter slope. 
* For Doing Business Indicator, the coefficient of regression is very high. The steep slope suggests that the improvement of countries' business infrastructure has a large positive effect on increasing their FDI in the USA. 
* Europe is the largest FDI investor in the USA. One interesting outlier would be Luxembourg; as a small country with a relatively low GDP, innovation & technology, and doing business indicator, it ranks 4th regionally and 6th globally for FDI in USA.
* Asia shows interesting dynamics across the key variables. Japan ranks 1st regionally and 2nd globally for FDI in USA with relatively top scores for all - GDP, innovation & technology, and doing business indicator. China invests minusculely in the USA despite its top global ranking for GDP and high technology export.     
* In Latin America, GDP appears to have slightly more effect on the FDI in USA than innovation & technology and doing business indicator. Mexico and Bermuda appear in the list of top 25 investors in the USA.
* In Africa, with high score for all - GDP, innovation & technology, and doing business indicator, South Africa turns out to be highest regional investor in the USA. 
* Canada and Australia appear among the top 25 investors in the USA, where Canada ranks 4th and Australia ranks 11th in the list.  

## Limitations & Conclusion
* The scope of the pilot/preliminary study was limited by the small datatset. 
* The study conducted data analysis for a recent year (2018); however, the analysis was restricted within a single year.
* The stock of FDI was applied to measure the dependent variable; the findings are needed to be cross-checked with examining the alternative measures of FDI. 
* Extension of the pilot/preliminary study intends to collect data for multiple years; the future research will conduct data analysis for 10+ years.
* The extended time series analysis will provide us with insights for both the static and dynamic relationship among the key variables.
* Examining the alternative measures of FDI (e.g. financial transaction and income flow based FDI) will add value to the future research.

##### Group Members: Bruce Muckerson, Ed Yancik, Julie Gandre, Michael Donatucci, and Sabrina Saleh
