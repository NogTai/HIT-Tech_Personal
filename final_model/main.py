from module.multielo import MultiElo
import pandas as pd
import numpy as np

if __name__ == "__main__":
    Elo_Score = pd.read_csv('fakeData.csv')
    Elo_Score["TieuChiChinh_Score"] = Elo_Score[['Home_Work_Score', 'Attendance_Score', 'Rate']].sum(axis=1)
    TieuChiChinh_Score_Decreased = sorted(Elo_Score["TieuChiChinh_Score"].unique())[::-1]
    TieuChiChinh_map_to_rank_numberic = dict(zip(TieuChiChinh_Score_Decreased, range(1, len(TieuChiChinh_Score_Decreased)+1)))

    map_to_rank_number = lambda x: TieuChiChinh_map_to_rank_numberic[x]
    Elo_Score["Rank"] = np.array(map(map_to_rank_number, Elo_Score["TieuChiChinh_Score"].values))
    
    # Tao 1 the hien cua lop MultiElo
    elo = MultiElo()
    new_Elo = elo.get_new_ratings(list(Elo_Score['Elo'].values), list(Elo_Score['Rank'].values))
    Elo_Score["new_Elo"] = new_Elo
    
    # Bảng kết quả có chứa cột new_Elo là điểm Elo sau khi được cập nhật
    print(Elo_Score)