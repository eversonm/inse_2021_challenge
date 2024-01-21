import DeleteOutlineIcon from "@mui/icons-material/DeleteOutline";
import InfoOutlinedIcon from "@mui/icons-material/InfoOutlined";
import MoreHorizIcon from "@mui/icons-material/MoreHoriz";
import { Box, IconButton, List, ListItem, Typography } from "@mui/material";
import React from "react";
import { useNavigate } from "react-router-dom";

const ListItemEscola = ({ escolas }) => {
  const navigate = useNavigate();

  const redirect_escola_id = (id) => {
    navigate(`/confinedEnviroment/${id}`);
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
          <ListItem
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
            onClick={() => {}}
          >
            <Box
              sx={{
                width: "20%",
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
                width: "15%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.nomeE}</Typography>
            </Box>

            <Box
              sx={{
                width: "15%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.tipoRede}</Typography>
            </Box>

            <Box
              sx={{
                width: "15%",
                alignItems: "center",
                justifyContent: "center",
                display: "flex",
              }}
            >
              <Typography sx={typographyStyle}>{escola.tipoLocalizacao}</Typography>
            </Box>

            {/* Mocked escolas */}
            <Box
              sx={{
                width: "10%",
                alignItems: "end",
                justifyContent: "end",
                display: "flex",
              }}
            >
              <IconButton aria-label="info" onClick={() => {}}>
                <InfoOutlinedIcon />
              </IconButton>
              <IconButton aria-label="more_info" onClick={() => {}}>
                <MoreHorizIcon />
              </IconButton>
              <IconButton aria-label="delete" onClick={() => {}}>
                <DeleteOutlineIcon />
              </IconButton>
            </Box>
          </ListItem>
        ))}
    </List>
  );
};

export default ListItemEscola;
