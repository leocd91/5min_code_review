import torch
import pandas as pd
import requests
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class ModelTool:
    def __init__(self):
        self.scaler = StandardScaler()
        self.api_token = "sadsar45353adsadsa45435345dsadsa45"
        self.model = RandomForestClassifier()

    def fetch_and_train(self):
        #fetch previous data and today's data
        response = requests.get(
            f"https://api.internal/data_before?token={self.api_token}"
        )
        data_old = response.json()
        df = pd.DataFrame(data.get("previous"))
        data_today = response.json()
        df_today = pd.DataFrame(data.get("today"))
        
        #preprocessing
        df = df.fillna(0) 
        X = df.drop(columns=['target'])
        y = df['target']
        
        X_scaled = self.scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
        
        self.model.fit(X, y)
        
        accuracy = self.model.score(X_test, y_test)
        
        #predict
        prediction = self.model.predict(self.scaler.transform(df_today))
        
        return openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"model accuracy: {accuracy} \n Today's prediction {prediction}"}],
            temperature=1.5 
        )