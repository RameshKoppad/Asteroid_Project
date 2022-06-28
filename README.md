
## 🚀 Problem Statement 💡 :

### Predict the diameter of the asteroids from the given dataset.🌌


| Variable Name | Description |
|----|----|
| a | semi-major axis[au] |
| e | eccentricity|
| i | inclination wrt x-y ecliptic plane [deg] |
| om | longitude of the ascending node |
| w | argument of perihelion |
| q | perihelion distance [au] |
| ad | aphelion distance [au] |
| per_y | orbital period [years] |
| data_arc | data arc-span [d] |
| condition_code | orbit condition code |
| n_obs_use | number of observations used |
| H | absolute magnitude parameter |
| diameter | diameter of asteroid [km] |
| extent | object bi or tri-axial ellipsoid dimensions [km] |
| albedo | geometric albedo |
| rot_per | standard gravitational parameter [m×Gm×G] |
| bv | color index B-V magnitude difference |
| ub | color index U-B magnitude difference |
| IR |color index I-R magnitude difference |
| spec_B | spectral taxonomic type (SMASSII) |
| spec_T | spectral taxonomic type (Tholen) |
| neo | near earth object |
| pha | physically hazardous asteroid |
| moid | earth minimum orbit intersection distance [au] |

 ##  🚀 **Dataset** 👩‍💻 **:**
 [Click Here for the Dataset](https://www.kaggle.com/basu369victor/prediction-of-asteroid-diameter)

 ## **Process**
 ### 1. Feature Enginerring and EDA
 ### 2. Data Analysis and Visualization
 ### 3. Modelling and Error Analysis
 ### 4. Advanced Modelling and Feature Engineering
 ### 5. Deployment and Productionization

 ## 👨🏻‍💻 Solution 💯
 


### ✅ Basic Operations 💯
  
#### File Name -> Feature_Engineering_and_EDA.ipynb

Imported Necessary Liberaries, Imported Dataset, Checked for shape of dataset, Finding the Information about datatypes of features, Spliting the features accouring to their datatype.


### ✅ Feature Engineering and Exploratorty Data Analysis 💯

  
#### File Name -> 1. Project_58_Phase _2_Ramesh_D_Koppad_Feature_Engineering_and_EDA.ipynb

  
 
    1. Univeriate Analysis
 
  a) On Numeric Data
  
  Finding the mean, standard deviation, 25th percentile, 75th percentile, etc
  
  b) On Categorical Data
  
  Made a frequency graph of variables and concluded its outcome
  
 
    2. Biveriate Analysis
  
  a) On Numeric Data
  
  Finding Correlation between features using heatmap and some functions 
  
  Outcome : 4 Features are found to be heavily correlated with pearson correlation coeffcient greater then 0.97 or less the -0.97
   
  b) On Categorical Data
  
  Performed Chi-Square Test on crosstab for finding out the relationship between the features
  
  Outcome : Many Features have found to be related with p-value less than 0.05 (95% confidence)
  
  
    3. Handeling Missing Values
  
  a) On Categorical Data
  
  Found the percentage of NaN values for each feature. Eliminated those features whose NaN values are greater then Non-NaN values and filled the rest with Mode of Data. 
  
  b) On Numeric Data
  
  Found the percentage of NaN values for each feature. Eliminated those features whose NaN values are greater then Non-NaN values, Two features where having some values repeted many time in the data so filled the NaN values of this features with mean of top 10 most occuring values. Filled the remaining features missing value by mean of entire feature. As 'diameter' was the target variable so its missing values was needed to be droped. Then converted the 'diameter' to float type variable.
  

    4. Handeling Outliers

  Roughly estimated the number of outliers using box plot visualization. Then found the actual number of outliers greater then 4th Standard Deviation using Z-Score Method. Finally created a Upper Limit and Lower Limit of outliers using InterQunatile Range and used Capping method to treat this outliers(i.e Replacing the values greater then Upper limit with Upper limit and replacing the values lower then lower limit by lower limit.)
  
  Saved the Clean Dataset with name 'Clean_Dataset.csv'

### ✅ Data Analysis and Visualization 💯
  
  
#### File Name -> 2. Project_58_Phase _2_Ramesh_D_Koppad_Data_Visualisation.ipynb


  1. Imported 'Clean_Dataset.csv' dataset for visualization
  
  2. Designed a heatmap of correlation with annotation
  
  3. Designed a scatter plot for feature 'a' VS 'n'
  
  4. Designed a scatter plot for feature 'n' VS 'per_y'
  
  5. Designed a countour plot for categorical feature 'class'
  
  6. Designed a categorical scatter plot for features 'class' VS 'data_arc'
  
  7. Designed a categorical scatter plot for features 'ma' VS 'class'
  
  8. Designed a multi-categorical scatter plot for feature 'class' VS 'per' with hue as 'pha'
 
  9. Designed a box plot for feature 'class' VS 'Diameter'
  
  10. Designed a point plot for feature 'pha' VS 'Diameter'
  
  11. Designed a point plot for feature 'condition_code' VS 'Diameter'
  
  12. Designed a point plot for feature 'condition_code' VS 'a'
  
  13. Designed a kde plot of 'Diameter' VS 'Density'
  
  14. Designed a kde plot of 'Diameter' VS 'Density' with hue as 'class'
  
  15. Designed a Distribution Histogram for feature 'a'
  
  16. Designed a Distribution Histogram for feature 'i'

### ✅ Modelling and Error Analysis 💯
    
#### File Name -> 3. Project_58_Phase_3_Ramesh_D_Koppad_Modelling_and_Error_Analysis.ipynb

  1. Imported 'Clean_Dataset.csv' dataset for model formation.
 
  2. Converted Categorical Data into numeric using Dummy Variable Trap (Droping one dummy variable column as it can be predicted by other).
  
  3. Splited the Data into Training and Testing Data ( 80 % of Data is used for Training and Testing is performed on 20% of data).
  
  4. Scaled the Data between 0 and 1 using Standard Scaler.
  
  5. Designed a evaluation function which will return Mean Absolute Error, Mean Squared Error, Root Mean Squared Error, R-Squared Value of the Model.
  
  6. Algorithms and their R-Squared Values :

  
  Some of the regressor algorithms are tested here and their R-Squared values are :

  A) Random Forest :-> 0.9696
  
  B) K Nearest Neighbour :-> 0.9116
      
  C) Linear Regression :-> 0.8812

  D) Decision Tree :-> 0.9402
      
  E) XG Boost :-> 0.9703


### ✅ Advanced Modelling and Feature Engineering  💯
  

  
#### File Name -> 4. Project_58_Phase_4_Ramesh_D_Koppad_Advanced_Modeling_and_Feature_Engineering.ipynb

  To increase the accuracy of Model I have performed additional updates as followes :
  
  1. Checked for multi-collinearity in the data using variance inflation factor and eliminated such features having very high value.
  
  2. Used 85% of data for training and performed testing on 15% of data.
  
  3. Applied an additional Algorithm along with previous ones and Imporved R-Squared values where as follows : 
  
  A) Random Forest :-> 0.9696
  
  B) K Nearest Neighbour :-> 0.9116
      
  C) Linear Regression :-> 0.8812

  D) Decision Tree :-> 0.9402
      
  E) XG Boost :-> 0.9703
      
  F) Optimized XG Boost :-> 0.9709
      
  G) Artificial Neural Network :-> 0.9670   
      
  🌟 Conclusion After Update: Best Performing Model is Optimized XG Boost Regressor. 🌟 


### ✅ Advanced Modelling and Feature Engineering 💯
  
#### File Name -> 5. Project_58_Phase_5_Ramesh_D_Koppad_Advanced_Modeling_and_Feature_Engineering.ipynb

  To further increase the accuracy of Model I have performed additional updates as followes :
  
  1. Used MinMax Scaler instead of Standard Scaler.
  
  2. Increased the number of iterations on CatBoost Regressor.
  
  Imporved R-Squared values where as follows : 
  
  A) Random Forest :-> 0.9696
  
  B) K Nearest Neighbour :-> 0.9116
      
  C) Linear Regression :-> 0.8812

  D) Decision Tree :-> 0.9402
      
  E) XG Boost :-> 0.9703
      
  F) Optimized XG Boost :-> 0.9709
      
  G) Artificial Neural Network :-> 0.9670  

  H) Cat Boost Regressor :-> 0.9727
   
   🌟 Conclusion: Best Performing Model is Cat Boost Regressor. 🌟
   
Note: You can try out with another algorithms.



