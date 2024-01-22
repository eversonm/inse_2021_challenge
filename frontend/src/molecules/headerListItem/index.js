import { Box, ListItem, Typography } from "@mui/material";
import React from "react";

const HeaderListItemEscola = () => {
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
    <ListItem
      key='escola-header-list-item'
      sx={{
        height: "10px",
        alignItems: "left",
        borderRadius: 1,
        marginBottom: 1,
        padding: 2,
        marginTop: 0.5,
        display: "inline-flex",
        width: "100%",
      }}
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
        <Typography sx={typographyStyle}>Código da Escola</Typography>
      </Box>

      <Box
        sx={{
          width: "30%",
          alignItems: "center",
          justifyContent: "center",
          display: "flex",
        }}
      >
        <Typography sx={typographyStyle}>Nome da Escola</Typography>
      </Box>
      <Box
        sx={{
          width: "10%",
          alignItems: "center",
          justifyContent: "center",
          display: "flex",
        }}
      >
        <Typography sx={typographyStyle}>Estado</Typography>
      </Box>
      <Box
        sx={{
          width: "10%",
          alignItems: "center",
          justifyContent: "center",
          display: "flex",
        }}
      >
        <Typography sx={typographyStyle}>Município</Typography>
      </Box>
      <Box
        sx={{
          width: "10%",
          alignItems: "center",
          justifyContent: "center",
          display: "flex",
        }}
      >
        <Typography sx={typographyStyle}>Rede</Typography>
      </Box>

      <Box
        sx={{
          width: "7%",
          alignItems: "center",
          justifyContent: "center",
          display: "flex",
        }}
      >
        <Typography sx={typographyStyle}>Localização</Typography>
      </Box>
      <Box
        sx={{
          width: "7%",
          alignItems: "center",
          justifyContent: "center",
          display: "flex",
        }}
      >
        <Typography sx={typographyStyle}>Capital</Typography>
      </Box>
      <Box
        sx={{
          width: "7%",
          alignItems: "center",
          justifyContent: "center",
          display: "flex",
        }}
      >
        <Typography sx={typographyStyle}>INSE</Typography>
      </Box>
    </ListItem>
  );
};

export default HeaderListItemEscola;
