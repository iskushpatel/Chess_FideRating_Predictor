# Chess Rating Predictor
## Project Overview
This project aims to predict FIDE Standard chess ratings based on a player's ratings on Chess.com (Blitz, Rapid, and Bullet). By leveraging machine learning techniques, we explore the relationship between online chess ratings and the official FIDE Standard rating.
## Data
The dataset used in this project is loaded from the CSV file [Chess.com-FIDE_Rating.csv](https://). It contains FIDE ratings (Standard, Rapid, and Blitz) and Chess.com ratings (Blitz, Rapid, and Bullet) for a collection of chess players.

## 📥 How Data Is Collected
This project combines player rating data from two major sources:
### 1. **FIDE Rating Data**
- **Source**: [FIDE (Fédération Internationale des Échecs)](https://ratings.fide.com/)
- **Data Includes**:
  - Player full names
  - FIDE IDs
  - Ratings across Standard, Blitz, and Rapid formats (when available)
- **Collection Method**:
  - Ratings were scraped or downloaded from the official FIDE website.
  - Only the **top 5000 players** by standard rating were selected to reduce noise and increase accuracy in name matching.
### 2. **Chess.com Rating Data**
- **Source**: [Chess.com Player Directory](https://www.chess.com/players)
- **Data Includes**:
  - Player usernames
  - Blitz, Rapid, and Bullet ratings
  - Display names (when available)
- **Collection Method**:
  - Data was collected via the public Chess.com player directory or API.
  - Usernames were paired with rating statistics to create a comprehensive database.
### 3. **Name Matching**
- **Library Used**: `RapidFuzz` (Python)
- **Matching Method**:
  - Player names from FIDE were normalized (case lowered, stripped of punctuation/whitespace).
  - Fuzzy matching (`token_sort_ratio`) was applied to find the closest matching names in the Chess.com dataset.
  - Matches with a score ≥ 85 were considered reliable.


## Data Preprocessing and Exploration

*   Initially, we loaded the data and performed some basic exploration using `data.head()` and `data.describe()` to understand the structure and summary statistics of the dataset.
*   We then dropped the 'FIDE_Name', 'FIDE_Rapid', and 'FIDE_Blitz' columns as they were not used as features for predicting the FIDE Standard rating in this project.
* A correlation heatmap was generated to visualize the relationships between the numerical features.
* Scatter plots were also created to show the relationship between 'FIDE_Standard' and each of the Chess.com rating types.





## Model Training and Evaluation
We trained and evaluated several regression models to predict the FIDE Standard rating:
1.  **Linear Regression:** A simple linear model to establish a baseline.
2.  **Decision Tree Regressor:** A tree-based model capable of capturing non-linear relationships.
3.  **Random Forest Regressor:** An ensemble method using multiple decision trees to improve robustness and accuracy. Hyperparameter tuning was performed using `GridSearchCV`.
4.  **XGBoost Regressor:** Another powerful gradient boosting model known for its performance. Hyperparameter tuning was also performed using `GridSearchCV`.

For each model, we used the **print_metrics** function to report the Mean Squared Error (MSE) and R-squared score on both the training and testing sets.
The features used for training the models were 'Chess.com_bullet', 'Chess.com_blitz', and 'Chess.com_rapid', while the target variable was 'FIDE_Standard'. The data was split into training and testing sets using `train_test_split`.
## Model Performance Comparison
The following R-squared scores were obtained for each model on the test set:
*   **Linear Regression** : `0.867`
*   **Decision Tree**:`0.842`
*   **Random Forest**: `0.907`
*   **XGBoost Test**: `0.897`
## Why XGBoost was choosen ?
**XGBoost was selected as the best model** due to its strong test performance (R² = 0.897) and superior generalization. While Random Forest had a slightly higher R² (0.907), it showed greater overfitting. XGBoost's closer train-test scores indicate better robustness for predicting FIDE Standard ratings.
## Feature Importance (Random Forest)
We also visualized the feature importances from the trained Random Forest model to understand which Chess.com rating types were most influential in predicting the FIDE Standard rating.
## Model Saving
The chosen XGBoost model was saved as a pickle file (`model.pkl`) using the `joblib` library 
## Tech Stack
* **Framework**: Streamlit
* **Deployed on**: HuggingFace
* **Source Code**: Google Collab
## Conclusion
This project is a part of SoM-25. In this project, I have demonstrated the skills that I learned in past 6-Weeks. I am thankful to all my seniors in AI/ML wing for their efforts in organising this programme.

## Live Demo
https://huggingface.co/spaces/kingkp132/Chess_Rating_Predictor
