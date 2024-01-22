import { Box, List, ListItemButton, Typography } from "@mui/material";
import React from "react";
import { useNavigate } from "react-router-dom";

const ListItemEscola = ({ escolas }) => {
  const navigate = useNavigate();

  const redirect_escola_id = (escola) => {
    navigate(`/escola/${escola.codigoE}`);
  };

  const typographyStyle = {
    color: "#727272",
    fontFamily: "Trebuchet MS",
    fontStyle: "normal",
    fontWeight: 700,
    lineHeight: "normal",
    fontSize: "12px",
    alignItems: "center",
  };

  return (
    <List>
      {Array.isArray(escolas) &&
        escolas.map((escola) => (
          <ListItemButton
            key={escola.codigoE}
            sx={{
              maxHeight: "6vh",
              alignItems: "left",
              borderRadius: 1,
              marginBottom: 1,
              padding: 2,
              marginTop: 0.5,
              boxShadow: "0px 0px 7px 0px rgba(0, 0, 0, 0.30)",
              display: "inline-flex",
              width: "100%",
            }}
            onClick={() => redirect_escola_id(escola)}
          >
            <Box
              sx={{
                width: "10%",
                alignItems: "center",
                justifyContent: "left",
                display: "flex",
                marginLeft: 2,
              }}
            >
              <Typography sx={typographyStyle}>{escola.codigoE}</Typography>
            </Box>

            <Box
              sx={{
                width: "30%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.nomeE}</Typography>
            </Box>
            <Box
              sx={{
                width: "10%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.nomeUf}</Typography>
            </Box>
            <Box
              sx={{
                width: "10%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.nomeM}</Typography>
            </Box>
            <Box
              sx={{
                width: "10%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.tipoRede}</Typography>
            </Box>

            <Box
              sx={{
                width: "7%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.tipoLocalizacao}</Typography>
            </Box>
            <Box
              sx={{
                width: "7%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.tipoCapital}</Typography>
            </Box>
            <Box
              sx={{
                width: "7%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.inseClassificacao}</Typography>
            </Box>
            
            
          </ListItemButton>
        ))}
    </List>
  );
};

export default ListItemEscola;
