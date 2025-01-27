import pandas as pd

from datetime import datetime

from src.utils.selenium import Selenium
from src.utils.accesses import AccessingURLs
from src.utils.copying_game_info import ExtractingGameInfos
from src.utils.copying_championship_info import ExtractingChampionshipInfos

def getting_data():
    selenium = Selenium()
    AccessingURLs(selenium.driver).join_championship()
    
    games_df = ExtractingChampionshipInfos(selenium.driver).get_dataframe()
    games_df['status'] = games_df['status'].astype(str)

    all_game_stats = {}

    for index, row in games_df.iterrows():
        print(f"Processando jogo {index}: status={row['status']}")

        if row['status'].strip().lower() != 'ft':
            print(f"Pulado: {index}, com status {row['status']}")
            continue
        
        game_url = row['url']
        selenium.driver.get(game_url)
        
        game_stats_df = ExtractingGameInfos(selenium.driver).get_dataframe()

        if isinstance(game_stats_df, str):
            raise ValueError(f"Erro: `copy_text()` retornou uma string ao invés de um DataFrame. Verifique a função `ExtractingGameInfos.copy_text()`.\nSaída: {game_stats_df}")

        game_stats = {}

        for _, stat_row in game_stats_df.iterrows():
            stat_name = stat_row["Stats"].lower().replace(" ", "_")
            game_stats[f"home_{stat_name}"] = stat_row["Home"]
            game_stats[f"away_{stat_name}"] = stat_row["Away"]

        all_game_stats[row["url"]] = game_stats
    
    stats_df = pd.DataFrame.from_dict(all_game_stats, orient="index").reset_index().rename(columns={"index": "url"})

    final_df = games_df.merge(stats_df, on="url", how="left")
    print('salvando csv')
    final_df.to_csv("jogos_com_estatisticas.csv", index=False)
    print('csv salvo')

getting_data()