import { Box, Paper, TextField, Typography } from "@mui/material";
import React, { useEffect } from "react";
import Plot from "react-plotly.js";
import { useParams } from "react-router-dom";
import { useAppFetch } from "../../hooks/fetch";

const Escola = () => {
  const { escola, fetch_escola } = useAppFetch();
  const { id } = useParams();
  useEffect(() => {
    if (id) {
      console.log(id);
      fetch_escola(id);
    }
  }, [id]);
  const typographyStyle = {
    color: "#727272",
    fontFamily: "Trebuchet MS",
    fontStyle: "normal",
    fontWeight: 700,
    lineHeight: "normal",
    fontSize: "35px",
    alignItems: "center",
  };

  const textFieldStyle = {
    "& .MuiInputBase-input.Mui-disabled": {
      WebkitTextFillColor: "#000000",
    },
    "& .MuiFormLabel-root":{
      WebkitTextFillColor: "#1976d2",
    },
  }

  return (
    <Paper
      style={{
        height: "100%",
        backgroundColor: "white",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        alignItems: "center",
        boxShadow: "0px 0px 7px 0px rgba(0, 0, 0, 0.30)",
      }}
    >
      {id && escola && (
        <>
          <Box sx={{ display: "flex", flexDirection: "row", marginTop: 2 }}>
            <Typography sx={typographyStyle}>{escola.nomeE}</Typography>
          </Box>
          <Box
            sx={{
              marginTop: 3,
              width: "70%",
              display: "flex",
              flexDirection: "column",
              justifyItems: "space-between",
              justifyContent: "center",
              gap: 4,
            }}
          >
            <Box
              sx={{
                width: "100%",
                display: "flex",
                justifyContent: "space-around",
                flexDirection: "row",
              }}
            >
              <TextField
                disabled
                id="outlined-basic"
                label="Ano"
                variant="outlined"
                value={2021}
                sx={textFieldStyle}
              />
              <TextField
                disabled
                id="outlined-basic"
                label="Código da Unidade da Federação"
                variant="outlined"
                value={escola.codigoUf}
                sx={textFieldStyle}
              />
              <TextField
                disabled
                id="outlined-basic"
                label="Sigla da Unidade da Federação"
                variant="outlined"
                value={escola.siglaUf}
                sx={textFieldStyle}
              />
              <TextField
                disabled
                id="outlined-basic"
                label="Nome da Unidade da Federação"
                variant="outlined"
                value={escola.nomeUf}
                sx={textFieldStyle}
              />
            </Box>
            <Box
              sx={{
                width: "100%",
                display: "flex",
                justifyContent: "space-around",
                flexDirection: "row",
              }}
            >
              <TextField
                disabled
                id="outlined-basic"
                label="Código do Município"
                variant="outlined"
                value={escola.codigoM}
                sx={textFieldStyle}
              />
              <TextField
                disabled
                id="outlined-basic"
                label="Nome do Município"
                variant="outlined"
                value={escola.nomeM}
                sx={textFieldStyle}
              />
              <TextField
                disabled
                id="outlined-basic"
                label="Código da Escola no CENSO Escolar"
                variant="outlined"
                value={escola.codigoE}
                sx={textFieldStyle}
              />
              <TextField
                disabled
                width="100%"
                id="outlined-basic"
                label="Dependência Administrativa da Escola"
                variant="outlined"
                sx={textFieldStyle}
                value={escola.tipoRede}
              />
            </Box>

            <Box
              sx={{
                width: "100%",
                display: "flex",
                justifyContent: "space-around",
                flexDirection: "row",
              }}
            >
              <TextField
                width="50%"
                disabled
                id="outlined-basic"
                label="Localização da Escola"
                variant="outlined"
                value={escola.tipoLocalizacao}
                sx={textFieldStyle}
              />
              <TextField
                width="50%"
                disabled
                id="outlined-basic"
                label="Área da Escola (relacionado ao Município)"
                variant="outlined"
                sx={textFieldStyle}
                value={escola.tipoCapital}
              />
            </Box>
            <Box
              sx={{
                display: "flex",
                flexDirection: "row",
                justifyContent: "center",
              }}
            >
              <Typography sx={typographyStyle}>
                Estatísticas da Escola
              </Typography>
            </Box>

            <Box
              sx={{
                width: "100%",
                display: "flex",
                justifyContent: "space-around",
                flexDirection: "row",
              }}
            >
              <Box
                sx={{
                  width: "100%",
                  display: "flex",
                  justifyContent: "space-around",
                  flexDirection: "column",
                }}
              >
                <TextField
                  disabled
                  id="outlined-basic"
                  label="Quantidade de Alunos com INSE calculado utilizado para o cálculo das médias"
                  variant="outlined"
                  value={escola.qtdeAlunos}
                  sx={textFieldStyle}
                />
                <TextField
                  disabled
                  id="outlined-basic"
                  label="Média do Indicador de Nível Socioeconômico dos alunos da escola"
                  variant="outlined"
                  value={escola.mediaInse}
                  sx={textFieldStyle}
                />
                <TextField
                  disabled
                  id="outlined-basic"
                  label="Classificação do Indicador de Nível Socioeconômico"
                  variant="outlined"
                  value={escola.inseClassificacao}
                  sx={textFieldStyle}
                />
              </Box>
              <Plot
                data={[
                  {
                    values: [
                      escola.percentualNivel1,
                      escola.percentualNivel2,
                      escola.percentualNivel3,
                      escola.percentualNivel4,
                      escola.percentualNivel5,
                      escola.percentualNivel6,
                      escola.percentualNivel7,
                      escola.percentualNivel8,
                    ],
                    labels: [
                      "Nível I", 
                      "Nível II",
                      "Nível III",
                      "Nível IV",
                      "Nível V",
                      "Nível VI",
                      "Nível VII",
                      "Nível VIII",
                    ],
                    type: "pie",
                  },
                ]}
                layout={{
                  title:
                    "Percentual de alunos da Escola classificados por nível",
                  height: 400,
                  width: 500,
                  colorway: [
                    "#0A3192",
                    "#0E46A8",
                    "#135DBD",
                    "#1976d2",
                    "#43BDDF",
                    "#70EAE2",
                    "#9EF3D6",
                    "#CDFADE",
                  ]
                }}
              />
            </Box>
          </Box>
        </>
      )}
    </Paper>
  );
};

export default Escola;
