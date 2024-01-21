import json
import pandas as pd
    
def insert_tables(file='src/lib/data/INSE_2021_escolas.csv'):
    df = pd.read_csv(file, sep=';')
    federativo = {
        "CO_UF": "codigo_uf", 
        "SG_UF": "sigla_uf", 
        "NO_UF": "nome_uf"
        }

    municipio = {
        "CO_UF": "federativa_codigo_uf", 
        "CO_MUNICIPIO": "codigo_m", 
        "NO_MUNICIPIO": "nome_m",
        }

    escola = {
        "CO_MUNICIPIO": "municipio_codigo_m", 
        "ID_ESCOLA": "codigo_e", 
        "NO_ESCOLA": "nome_e", 
        "TP_TIPO_REDE": "tipo_rede", 
        "TP_LOCALIZACAO": "tipo_localizacao", 
        "TP_CAPITAL": "tipo_capital", 
        "QTD_ALUNOS_INSE": "qtde_alunos",
        "MEDIA_INSE": "media_inse",
        "INSE_CLASSIFICACAO": "inse_classificacao"
        }

    percentual = {
        "CO_MUNICIPIO": "municipio_codigo_m", 
        "ID_ESCOLA": "escola_codigo_e", 
        "PC_NIVEL_1": "percentual_nivel_1", 
        "PC_NIVEL_2": "percentual_nivel_2", 
        "PC_NIVEL_3": "percentual_nivel_3", 
        "PC_NIVEL_4": "percentual_nivel_4", 
        "PC_NIVEL_5": "percentual_nivel_5",
        "PC_NIVEL_6": "percentual_nivel_6",
        "PC_NIVEL_7": "percentual_nivel_7",
        "PC_NIVEL_8": "percentual_nivel_8",
        }

    df_federativo = df[["CO_UF", "SG_UF", "NO_UF"]].drop_duplicates()

    df_federativo.rename(columns=federativo, inplace=True)
    df_federativo = df_federativo.to_json(orient='records')
    df_federativo_json = json.loads(df_federativo)

    with open('src/alembic/versions/federativo.json', 'w', encoding='utf-8') as f:
        json.dump(df_federativo_json, f, indent=4)

    df_municipio = df[["CO_UF", "CO_MUNICIPIO", "NO_MUNICIPIO"]].drop_duplicates()
    df_municipio.rename(columns=municipio, inplace=True)
    df_municipio = df_municipio.to_json(orient='records')
    df_municipio_json = json.loads(df_municipio)

    with open('src/alembic/versions/municipio.json', 'w', encoding='utf-8') as f:
        json.dump(df_municipio_json, f, indent=4)

    df_escolas = df[[
        "CO_MUNICIPIO", 
        "ID_ESCOLA", 
        "NO_ESCOLA", 
        "TP_TIPO_REDE", 
        "TP_LOCALIZACAO", 
        "TP_CAPITAL", 
        "QTD_ALUNOS_INSE",
        "MEDIA_INSE",
        "INSE_CLASSIFICACAO"
    ]].drop_duplicates()
    
    df_escolas['TP_TIPO_REDE'].replace(to_replace=[1, 2, 3], value=['Federal', 'Estadual', 'Municipal'], inplace=True)
    df_escolas['TP_LOCALIZACAO'].replace(to_replace=[1, 2], value=['Urbana', 'Rural'], inplace=True)
    df_escolas['TP_CAPITAL'].replace(to_replace=[1, 2], value=['Capital', 'Interior'], inplace=True)

    df_escolas.rename(columns=escola, inplace=True)
    df_escolas = df_escolas.to_json(orient='records')
    df_escolas_json = json.loads(df_escolas)

    with open('src/alembic/versions/escolas.json', 'w', encoding='utf-8') as f:
        json.dump(df_escolas_json, f, indent=4)

    df_percentual = df[[
        "CO_MUNICIPIO", 
        "ID_ESCOLA", 
        "PC_NIVEL_1", 
        "PC_NIVEL_2", 
        "PC_NIVEL_3", 
        "PC_NIVEL_4", 
        "PC_NIVEL_5",
        "PC_NIVEL_6",
        "PC_NIVEL_7",
        "PC_NIVEL_8"
    ]].drop_duplicates()
    df_percentual.rename(columns=percentual, inplace=True)
    df_percentual = df_percentual.to_json(orient='records')
    df_percentual_json = json.loads(df_percentual)

    with open('src/alembic/versions/percentual.json', 'w', encoding='utf-8') as f:
        json.dump(df_percentual_json, f, indent=4)

insert_tables()