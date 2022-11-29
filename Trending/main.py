from module.Calculate_Elo import Calculate_Elo
import pandas as pd

if __name__ == "__main__":
    Elo_Score = pd.read_csv('fakeData.csv')
    New_data_sort_by_Elo = Calculate_Elo(Elo_Score.copy(), TieuChiChinh=['Home_Work_Score', 'Attendance_Score', 'Rate'], TieuChiPhu=['Time'], K=12)
    print(New_data_sort_by_Elo.Calculate())