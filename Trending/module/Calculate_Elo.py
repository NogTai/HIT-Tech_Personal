import numpy as np
import pandas as pd

class Calculate_Elo:
    def __init__(self, Dataframe_Elo_Score, TieuChiChinh, TieuChiPhu, K=32):
        self.Dataframe_Elo_Score = Dataframe_Elo_Score
        self.TieuChiChinh = TieuChiChinh
        self.TieuChiPhu = TieuChiPhu
        self.All_Score_Tieu_ChiChinh = None
        self.Dataframe_Elo_Score_sorted = None
        self.K = K


    def Calculate_Score_from_Tieu_Chi_chinh(self):
        self.Dataframe_Elo_Score["TieuChiChinh_Score"] = self.Dataframe_Elo_Score[self.TieuChiChinh].sum(axis=1)
        self.All_Score_Tieu_ChiChinh = self.Dataframe_Elo_Score["TieuChiChinh_Score"].values


    def score_d(self, elo_num, data):
        lst =  elo_num - data
        lst = [ 0.5 if item == 0  else  0 if item < 0 else 1 for item in lst]
        return np.array(lst).sum()


    def Probability(self, elo_num, data):
        list_pow = (elo_num - data) / 400.0
        list_pow = np.array([10**item for item in list_pow])
        return np.sum(1.0/(1+list_pow))


    def soc_iter(self, Elo_row, data, k = 12):
        d = self.score_d(Elo_row, data)
        Q = self.Probability(Elo_row, data)
        return Elo_row + k * (d-Q)
    

    def Calculate(self):
        self.Calculate_Score_from_Tieu_Chi_chinh()
        self.Dataframe_Elo_Score['Elo_After'] = self.Dataframe_Elo_Score.apply(lambda row: self.soc_iter(row['Elo'], self.All_Score_Tieu_ChiChinh, self.K), axis=1)
        
        # Sort data by Elo_After, then by TieuChiPhu
        self.Dataframe_Elo_Score_sorted = self.Dataframe_Elo_Score.sort_values(by=['Elo_After', *self.TieuChiPhu], ascending=False)
        return self.Dataframe_Elo_Score_sorted
