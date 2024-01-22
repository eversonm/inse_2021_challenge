import { Paper } from "@mui/material";
import React from "react";
import Plot from "react-plotly.js";

const Dashboard = () => {

  const values = [
    [21143935, 21246564, 13061526, 13007246, 16003179, 13087053, 13068407, 15557065, 15549550, 15029360],
    ['UNIDADE ESCOLAR GERONIMO DE LOURA', 'EM SARNEY FILHO', 'ESC MUN INDIGENA JERUSALEM', 'ESC MUN INDIGENA BOM JESUS', 'ESC EST MANOEL JOSE SANTOS DA SILVA', 'ESC MUN INDIGENA TUKANO YUPURI', 'ESCOLA MUNICIPAL INDIGENA EWARE', 'E M E F OSMAR MACIEL', 'E M E F SANTA LUZIA - RIO TAUAU', 'E M E F CASTRO ALVES'],
    ['Nível I', 'Nível I', 'Nível I', 'Nível I', 'Nível I', 'Nível I', 'Nível I', 'Nível I', 'Nível I', 'Nível I'],
    [1, 25, 7, 13, 5, 9, 8, 5, 11, 6],
    [2.45, 2.5, 2.51, 2.51, 2.52, 2.54, 2.54, 2.55, 2.55, 2.56],
    ['São Benedito do Rio Preto', 'Centro do Guilherme', 'Japurá', 'Santo Antônio do Içá', 'Macapá', 'São Gabriel da Cachoeira', 'Tonantins', 'Afuá', 'Breves', 'Chaves'],
    ['Maranhão', 'Maranhão', 'Amazonas', 'Amazonas', 'Amapá', 'Amazonas', 'Amazonas', 'Pará', 'Pará', 'Pará']
  ]
  return (
    <Paper
      style={{
        height: "100%",
        backgroundColor: "white",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        className="App"
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      >
        <Plot
          data={[
            {
              type: 'table',
              header: {
                values: [["<b>Codigo da escola</b>"], ["<b>Nome da Escola</b>"],
                     ["<b>INSE</b>"], ["<b>Qtde de alunos</b>"], ["<b>Media INSE</b>"],
                     ["<b>Municipio</b>"], ["<b>Estado</b>"]],
                align: "center",
                line: {width: 1, color: 'black'},
                fill: {color: "grey"},
                font: {family: "Arial", size: 12, color: "white"}
              },
              cells: {
                values: values,
                align: "center",
                line: {color: "black", width: 1},
                font: {family: "Arial", size: 11, color: ["black"]}
              }
            }
          ]}
          layout={{
            title: "Estados com os piores indicadores INSE",
            width: 1000,
            height: 900,
          }}
        />
      </div>
    </Paper>
  )
}

export default Dashboard