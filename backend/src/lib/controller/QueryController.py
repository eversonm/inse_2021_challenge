import humps
from src.lib.models.Federativas import Federativas
from src.lib.models.Municipios import Municipios
from src.lib.models.Escolas import (
    Escolas, InseClassificacao, TipoCapital, TipoLocalizacao, TipoRede
)
from src.lib.models.PercentualMunicipioEscola import PercentualMunicipioEscola
from src.lib.database.connector_thread import db_session

class QueryController():
    def get_all(self, **args):
        
        query = db_session.query(Escolas).join(
            Municipios, 
            Escolas.municipio_codigo_m==Municipios.codigo_m
        ).join(
            Federativas,
            Municipios.federativa_codigo_uf==Federativas.codigo_uf
        )

        pages_quantity = query.count()/int(10)
        escolas = query.limit(10).offset(int(10)*(int(1)-1))
        return pages_quantity, [row.to_json() for row in escolas]
    

    def get_all_json(self, **args):
        filters = []
        page = 1
        if args["page"]!=1:
            page = args["page"]
        if args["federacao"]!=0:
            filters.append(Federativas.codigo_uf == args["federacao"])
        if args["municipio"]!=0:
            filters.append(Municipios.codigo_m == args["municipio"])
        if args["rede"]!=0:
            filters.append(
                Escolas.tipo_rede.in_(
                    [TipoRede(int(args["rede"]))]
                    )
            )
        if args["localizacao"]!=0:
            filters.append(
                Escolas.tipo_localizacao.in_(
                    [TipoLocalizacao(int(args["localizacao"]))]
                    )
            )
        if args["capital"]!=0:
            filters.append(
                Escolas.tipo_capital.in_(
                    [TipoCapital(int(args["capital"]))]
                    )
            )
        if args["classificacao"]!=0:
            filters.append(
                Escolas.inse_classificacao.in_(
                    [InseClassificacao(int(args["classificacao"]))]
                    )
            )
        if args["search"] != "":
            search = args["search"]
            filters.append(Escolas.nome_e.like(f"%{search}%"))

        query = db_session.query(Escolas, Federativas, Municipios).join(
            Municipios, 
            Escolas.municipio_codigo_m==Municipios.codigo_m
        ).join(
            Federativas,
            Municipios.federativa_codigo_uf==Federativas.codigo_uf
        ).with_entities(
            Escolas.codigo_e,
            Escolas.nome_e,
            Escolas.tipo_rede,
            Escolas.tipo_localizacao,
            Escolas.tipo_capital,
            Escolas.inse_classificacao,
            Escolas.qtde_alunos,
            Escolas.media_inse,
            Municipios.codigo_m,
            Municipios.nome_m,
            Federativas.codigo_uf,
            Federativas.sigla_uf,
            Federativas.nome_uf,
        ).filter(*filters)
        
        pages_quantity = query.count()/int(10)
        escolas = query.limit(10).offset(int(10)*(int(page)-1))
        list_ = []

        for row in escolas:
            list_.append(humps.camelize({
                "codigo_e": row[0],
                "nome_e": row[1],
                "tipo_rede": row[2].name,
                "tipo_localizacao": row[3].name,
                "tipo_capital": row[4].name,
                "inse_classificacao": row[5].name,
                "qtde_alunos": row[6],
                "media_inse": row[7],
                "codigo_m": row[8],
                "nome_m": row[9],
                "codigo_uf": row[10],
                "sigla_uf": row[11],
                "nome_uf": row[12],
            }))
        return pages_quantity, list_