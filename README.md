# 911-Calls-Project
This project analyzes 911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert) as part of the **Python for Data Science and Machine Learning Bootcamp**.   The dataset contains emergency call records from Montgomery County, PA, with information about the type of call, location, and time.

## Dataset Fields
- **lat**: Latitude of the call (string)
- **lng**: Longitude of the call (string)
- **desc**: Description of the emergency call
- **zip**: Zipcode
- **title**: Title of the emergency call
- **timeStamp**: Time of the call in YYYY-MM-DD HH:MM:SS format
- **twp**: Township
- **addr**: Address
- **e**: Dummy variable (always 1)

## Objectives
- Explore and clean the dataset
- Analyze the frequency of different types of 911 calls
- Visualize patterns in call data over time
- Gain insights for emergency response optimization

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- PyCharm

## How to Run
1. Clone the repository:  
```bash
git clone <your-repo-url>
```
2. Install dependencies:
 ```bash
pip install -r requirements.txt
```
3. Run the main Python script:
 ```bash
python calls911.py
