import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.metrics import confusion_matrix, classification_report
import xgboost as xgb
from xgboost import plot_importance
from sklearn.linear_model import LogisticRegression
from datetime import datetime
from typing import List

class DelayModel:

    def __init__(self):
        self._model = None

    def preprocess(self, data: pd.DataFrame, target_column: str = None) -> pd.DataFrame:
        data['period_day'] = data['Fecha-I'].apply(self.get_period_day)
        data['high_season'] = data['Fecha-I'].apply(self.is_high_season)
        data['min_diff'] = data.apply(self.get_min_diff, axis=1)
        data['delay'] = np.where(data['min_diff'] > 15, 1, 0)
        return data

    def get_period_day(self, date):
        date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').time()
        morning_min = datetime.strptime("05:00", '%H:%M').time()
        morning_max = datetime.strptime("11:59", '%H:%M').time()
        afternoon_min = datetime.strptime("12:00", '%H:%M').time()
        afternoon_max = datetime.strptime("18:59", '%H:%M').time()
        evening_min = datetime.strptime("19:00", '%H:%M').time()
        evening_max = datetime.strptime("23:59", '%H:%M').time()
        night_min = datetime.strptime("00:00", '%H:%M').time()
        night_max = datetime.strptime("04:59", '%H:%M').time()

        if morning_min <= date_time <= morning_max:
            return 'morning'
        elif afternoon_min <= date_time <= afternoon_max:
            return 'afternoon'
        elif evening_min <= date_time <= evening_max:
            return 'evening'
        else:
            return 'night'

    def is_high_season(self, fecha):
        fecha_año = int(fecha.split('-')[0])
        fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        range1_min = datetime.strptime('15-Dec', '%d-%b').replace(year=fecha_año)
        range1_max = datetime.strptime('31-Dec', '%d-%b').replace(year=fecha_año)
        range2_min = datetime.strptime('1-Jan', '%d-%b').replace(year=fecha_año)
        range2_max = datetime.strptime('3-Mar', '%d-%b').replace(year=fecha_año)
        range3_min = datetime.strptime('15-Jul', '%d-%b').replace(year=fecha_año)
        range3_max = datetime.strptime('31-Jul', '%d-%b').replace(year=fecha_año)
        range4_min = datetime.strptime('11-Sep', '%d-%b').replace(year=fecha_año)
        range4_max = datetime.strptime('30-Sep', '%d-%b').replace(year=fecha_año)

        if (
            (range1_min <= fecha <= range1_max)
            or (range2_min <= fecha <= range2_max)
            or (range3_min <= fecha <= range3_max)
            or (range4_min <= fecha <= range4_max)
        ):
            return 1
        else:
            return 0

    def get_min_diff(self, data):
        fecha_o = datetime.strptime(data['Fecha-O'], '%Y-%m-%d %H:%M:%S')
        fecha_i = datetime.strptime(data['Fecha-I'], '%Y-%m-%d %H:%M:%S')
        min_diff = ((fecha_o - fecha_i).total_seconds()) / 60
        return min_diff

    def evaluate_model(self, features, target):
        y_preds = self._model.predict(features)
        y_preds = [1 if y_pred > 0.5 else 0 for y_pred in y_preds]
        return confusion_matrix(target, y_preds), classification_report(target, y_preds)

    def train_model(self, data):
        training_data = shuffle(data[['OPERA', 'MES', 'TIPOVUELO', 'SIGLADES', 'DIANOM', 'delay']], random_state=111)
        features = pd.concat([
            pd.get_dummies(data['OPERA'], prefix='OPERA'),
            pd.get_dummies(data['TIPOVUELO'], prefix='TIPOVUELO'),
            pd.get_dummies(data['MES'], prefix='MES')],
            axis=1
        )
        target = data['delay']
        x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.33, random_state=42)

        xgb_model = xgb.XGBClassifier(random_state=1, learning_rate=0.01)
        xgb_model.fit(x_train, y_train)
        confusion_xgb, report_xgb = self.evaluate_model(x_test, y_test)

        reg_model = LogisticRegression()
        reg_model.fit(x_train, y_train)
        confusion_reg, report_reg = self.evaluate_model(x_test, y_test)

        return confusion_xgb, report_xgb, confusion_reg, report_reg
    
    def predict(self, features: pd.DataFrame) -> List[int]:
        if self._model is None:
            raise ValueError("Model not trained. Call train_model() first.")
        predicted_probs = self._model.predict_proba(features)
        predicted_labels = [1 if prob[1] > 0.5 else 0 for prob in predicted_probs]
        
        return predicted_labels
    
if __name__ == "__main__":
    model = DelayModel()
    data = pd.read_csv('../data/data.csv')
    preprocessed_data = model.preprocess(data)

    confusion_xgb, report_xgb, confusion_reg, report_reg = model.train_model(preprocessed_data)
    print("XGBoost Confusion Matrix:\n", confusion_xgb)
    print("XGBoost Classification Report:\n", report_xgb)
    print("Logistic Regression Confusion Matrix:\n", confusion_reg)
    print("Logistic Regression Classification Report:\n", report_reg)
