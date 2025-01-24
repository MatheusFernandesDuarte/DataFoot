import pandas as pd

from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pandas import DataFrame

class ExtractingChampionshipInfos():
    def __init__(self, driver) -> None:
        self.driver = driver

        self.games_df = self.extracting_championship_games()
        self.manipulating_df(games_df=self.games_df)

    def extracting_championship_games(self) -> DataFrame:
        games = []

        while True:
            round = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By .XPATH, '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[1]/div/button/div/div'))).text
            today = datetime.today().date()

            for i in range(1, 9):
                date = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[2]/a[{i}]/div/div/div[2]/bdi'))).text
                status = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[2]/a[{i}]/div/div/div[2]/div'))).text
                home = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[2]/a[{i}]/div/div/div[4]/div/div[1]/div[1]'))).text
                away = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[2]/a[{i}]/div/div/div[4]/div/div[1]/div[2]'))).text
                if ':' in date:
                    match_date = today
                else:
                    match_date = datetime.strptime(date, "%d/%m/%y").date()

                if match_date >= today:
                    home_score = "N/A"
                    away_score = "N/A"
                else:
                    try:
                        home_score = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[2]/a[{i}]/div/div/div[4]/div/div[3]/div[1]'))).text
                    except:
                        home_score = 'N/A'
                    try:
                        away_score = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[2]/a[{i}]/div/div/div[4]/div/div[3]/div[2]'))).text
                    except:
                        away_score = 'N/A'

                url = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[2]/a[{i}]'))).get_attribute('href')
                
                games.append({
                    "round": round,
                    "game": f"Game {i}",
                    "date": date,
                    "status": status,
                    "home": home,
                    "away": away,
                    "home_score": home_score,
                    "away_score": away_score,
                    "url": url,
                })
            if round == 'Round 1':
                break
            else:
                changing_round = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[1]/button[1]')))
                self.driver.execute_script("arguments[0].click();", changing_round)
        
        return pd.DataFrame(games)

    def manipulating_df(self, games_df: DataFrame) -> DataFrame:
        """ Remove cartões ('x2', 'x3', etc) dos nomes dos times """
        games_df['home'] = games_df['home'].str.replace(r"x\d+", "", regex=True).str.strip()
        games_df['away'] = games_df['away'].str.replace(r"x\d+", "", regex=True).str.strip()

        print(games_df)
        return games_df
    
    def get_dataframe(self) -> DataFrame:
        """ Retorna o DataFrame já processado """
        return self.games_df