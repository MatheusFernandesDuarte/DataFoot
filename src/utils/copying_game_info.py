import pandas as pd

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pandas import DataFrame

class ExtractingGameInfos():
    def __init__(self, driver) -> None:
        self.driver = driver
        
        self.stats_df = self.copy_text()
        
    def copy_text(self):
        """Extrai estatísticas da página do jogo e retorna um DataFrame formatado."""
        match_overview = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]/div[1]/div[6]/div/div[2]/div[2]/div/div[1]/div[2]'))).text
        
        shot_stats_list = []

        i = 2
        while i < 9:
                try:
                    shot_stats = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/div[1]/div[1]/div[6]/div/div[2]/div[2]/div/div[2]/div[2]/div[{i}]'))).text
                    shot_stats_list.append(shot_stats)
                    i += 1
                except:
                    break

        all_stats = match_overview + '\n' + '\n'.join(shot_stats_list)
                
        return self.parse_stats(all_stats)
    
    def parse_stats(self, stats_text: str):
        """Transforma o texto extraído em um DataFrame estruturado."""
        lines = stats_text.strip().split('\n')

        stats = {}

        i = 0

        while i < len(lines):
            if i + 2 < len(lines):
                home_value = lines[i].strip()
                stat_name = lines[i+1].strip()
                away_value = lines[i+2].strip()

                stats[stat_name] = [home_value, away_value]

                i += 3
            else:
                break

        stats_df = pd.DataFrame.from_dict(stats, orient='index', columns=['Home', 'Away'])
        stats_df = stats_df.reset_index().rename(columns={'index': 'Stats'})
        print(stats_df)
        return stats_df

    def get_dataframe(self) -> DataFrame:
        """ Retorna o DataFrame já processado """
        return self.stats_df
    