import {
  Box,
  InputBase,
  Pagination,
  Paper,
  TextField,
  alpha,
  styled,
} from "@mui/material";
import React, { useCallback, useEffect, useState } from "react";
import SelectCustomEstado from "../../atoms/selectEstado";
import SelectCustomMunicipio from "../../atoms/selectMunicipio";
import SelectType from "../../atoms/selectTipo";
import { useAppFetch } from "../../hooks/fetch";
import ListItemEscola from "../../molecules/listItem";

const DefaultPage = () => {
  const {
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
    // search,
    fetch_escolas,
    page,
    rede,
    redeList,
    setPage,
    setLocalizacao,
    setCapital,
    setRede,
    // setSearch,
  } = useAppFetch();

  const [search, setSearch] = useState("");

  const stringQuery = `?federacao=${estado}&municipio=${cidade}&rede=${rede}&localizacao=${localizacao}&capital=${capital}&search=${search}`;

  useEffect(() => {
    if (estados.length === 0){
      fetch_estados();
    }
    fetch_cidades(estado);
    fetch_escolas(stringQuery);
  }, [estado, cidade, rede, capital, localizacao, search]);

  const handleChange = useCallback((event, value) => {
    setPage(value++);
  }, []);

  const Search = styled("div")(({ theme }) => ({
    position: "relative",
    borderRadius: theme.shape.borderRadius,
    backgroundColor: alpha(theme.palette.common.white, 0.15),
    "&:hover": {
      backgroundColor: alpha(theme.palette.common.white, 0.25),
    },
    marginRight: theme.spacing(2),
    marginLeft: 0,
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      marginLeft: theme.spacing(3),
      width: "auto",
    },
  }));

  const SearchIconWrapper = styled("div")(({ theme }) => ({
    padding: theme.spacing(0, 2),
    height: "100%",
    position: "absolute",
    pointerEvents: "none",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  }));

  const StyledInputBase = styled(InputBase)(({ theme }) => ({
    color: "inherit",
    "& .MuiInputBase-input": {
      padding: theme.spacing(1, 1, 1, 0),
      // vertical padding + font size from searchIcon
      paddingLeft: `calc(1em + ${theme.spacing(4)})`,
      transition: theme.transitions.create("width"),
      width: "100%",
      [theme.breakpoints.up("md")]: {
        width: "20ch",
      },
    },
  }));

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
          <SelectCustomEstado nameMenu="Estado" itemsMenu={estados} />
          {estado !== 0 && (
            <SelectCustomMunicipio nameMenu="Cidade" itemsMenu={cidades} />
          )}
          <SelectType nameMenu="Tipo de rede" itemsMenu={redeList} tipo={rede} setTipo={setRede} />
          <SelectType nameMenu="Localização" itemsMenu={localizacaoList} tipo={localizacao} setTipo={setLocalizacao}  />
          <SelectType nameMenu="Capital" itemsMenu={capitalList} tipo={capital} setTipo={setCapital}  />
          <Box
          sx={{width: "100%"}}>
            <TextField 
              id="outlined-adornment" 
              placeholder="Search..."
              type="text"
              value={search} 
              onChange={(event) => {
                  event.preventDefault();
                  if (event.target.value) {
                    console.log(event.target.value)
                    setSearch(event.target.value.toLowerCase());
                  }
                }}
            />
          </Box>
          
          {/* <Search>
            <SearchIconWrapper>
              <SearchIcon />
            </SearchIconWrapper>
            <StyledInputBase
              placeholder="Search…"
              inputProps={{ "aria-label": "search" }}
              // value={search}
              defaultValue={search}
              onChange={(event) => {
                event.preventDefault();
                if (event.target.value) {
                  console.log(event.target.value)
                  setSearch(event.target.value.toLowerCase());
                }
              }}
            />
          </Search> */}
        </Box>
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
