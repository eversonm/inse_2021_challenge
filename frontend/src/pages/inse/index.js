import SearchIcon from '@mui/icons-material/Search';
import { Box, Button, InputAdornment, Pagination, Paper, TextField, Typography } from "@mui/material";
import React, { useCallback, useEffect } from "react";
import SelectCustomEstado from "../../atoms/selectEstado";
import SelectCustomMunicipio from "../../atoms/selectMunicipio";
import SelectType from "../../atoms/selectTipo";
import { useAppFetch } from "../../hooks/fetch";
import HeaderListItemEscola from "../../molecules/headerListItem";
import ListItemEscola from "../../molecules/listItem";

const DefaultPage = () => {
  const {
    classificacao,
    classificacaoList,
    capital,
    capitalList,
    countPages,
    estado,
    estados,
    fetch_estados,
    cidade,
    cidades,
    localizacao,
    localizacaoList,
    fetch_cidades,
    escolas,
    search,
    fetch_escolas,
    page,
    rede,
    resetData,
    redeList,
    setPage,
    setLocalizacao,
    setCapital,
    setRede,
    setSearch,
    setClassificacao
  } = useAppFetch();

  const stringQuery = `?page=${page}&federacao=${estado}&municipio=${cidade}&rede=${rede}&localizacao=${localizacao}&capital=${capital}&search=${search.toUpperCase()}&classificacao=${classificacao}`;

  useEffect(() => {
    if (estados.length === 0) {
      fetch_estados();
    }
    fetch_cidades(estado);
    fetch_escolas(stringQuery);
  }, [estado, cidade, rede, capital, localizacao, search, page, classificacao]);

  const handleChange = useCallback((event, value) => {
    setPage(value++);
  }, [setPage]);

  const typographyStyle = {
    color: "#727272",
    fontFamily: "Trebuchet MS",
    fontStyle: "normal",
    fontWeight: 700,
    lineHeight: "normal",
    fontSize: "35px",
    alignItems: "center",
  };

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
      <Box
        sx={{
          width: "90%",
          justifyItems: "space-between",
          justifyContent: "center",
        }}
      >
        <Box
          sx={{
            marginTop: "20px",
            height: "100%",
            backgroundColor: "white",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Typography sx={typographyStyle}>Tabela de Escolas</Typography>
        </Box>
        <Box
          sx={{
            marginTop: "20px",
            height: "100%",
            backgroundColor: "white",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <SelectCustomEstado nameMenu="Estado" itemsMenu={estados} />
          {estado !== 0 && (
            <SelectCustomMunicipio nameMenu="Cidade" itemsMenu={cidades} />
          )}
          <SelectType
            nameMenu="Tipo de rede"
            itemsMenu={redeList}
            tipo={rede}
            setTipo={setRede}
          />
          <SelectType
            nameMenu="Localização"
            itemsMenu={localizacaoList}
            tipo={localizacao}
            setTipo={setLocalizacao}
          />
          <SelectType
            nameMenu="Capital"
            itemsMenu={capitalList}
            tipo={capital}
            setTipo={setCapital}
          />
          
        </Box>

        <Box
          sx={{
            marginTop: "12px",
            backgroundColor: "white",
            display: "flex",
            justifyContent: "space-around",
            alignItems: "center",
          }}
        >
          <Box sx={{ width: "100%" }}>
            <TextField
              fullWidth
              id="outlined-adornment"
              placeholder="Search..."
              type="text"
              value={search}
              InputProps={{
                startAdornment:
                <InputAdornment position="start">
                  <SearchIcon />
                </InputAdornment>
              }}
              onChange={(event) => {
                event.preventDefault();
                setSearch(event.target.value);
              }}
            />
          </Box>
          <Box width="200px">
            <SelectType
              nameMenu="Classificação"
              itemsMenu={classificacaoList}
              tipo={classificacao}
              setTipo={setClassificacao}
            />
          </Box>
          
          <Button 
            variant="outlined"
            sx={{textTransform: "none"}}
            onClick={(event) => {
              event.preventDefault();
              resetData();
            }}
          >
            Apagar Filtros
          </Button>
        </Box>

        <HeaderListItemEscola />
        <ListItemEscola escolas={escolas} />
        <Pagination
          style={{
            display: "flex",
            justifyContent: "center",
          }}
          page={page}
          count={countPages}
          onChange={handleChange}
        />
      </Box>
    </Paper>
  );
};

export default DefaultPage;
