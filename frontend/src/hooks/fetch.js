import React, { createContext, useContext, useState } from "react";
import {
  _fetch_cidades,
  _fetch_escola,
  _fetch_escolas,
  _fetch_estados,
} from "../services/dados";

const AppContext = createContext({});

export const AppProvider = ({ children }) => {
  const [cidades, setCidades] = useState([]);
  const [cidade, setCidade] = useState(0);

  const [escolas, setEscolas] = useState([]);
  const [escola, setEscola] = useState();

  const [estados, setEstados] = useState([]);
  const [estado, setEstado] = useState(0);

  const [page, setPage] = useState(1);
  const [countPages, setCountPages] = useState(1);

  const [capital, setCapital] = useState(0);
  const [localizacao, setLocalizacao] = useState(0);
  const [rede, setRede] = useState(0);

  const [search, setSearch] = useState("");

  const capitalList = [
    { id: 0, tipo: "Todos" },
    { id: 1, tipo: "Capital" },
    { id: 2, tipo: "Interior" },
  ];

  const localizacaoList = [
    { id: 0, tipo: "Todos" },
    { id: 1, tipo: "Urbana" },
    { id: 2, tipo: "Rural" },
  ];

  const redeList = [
    { id: 0, tipo: "Todos" },
    { id: 1, tipo: "Federal" },
    { id: 2, tipo: "Estadual" },
    { id: 3, tipo: "Municipal" },
  ];

  const fetch_estados = async () => {
    const old_estados = await _fetch_estados();
    const new_estados = [
      { codigoUf: 0, siglaUf: "ZZ", nomeUf: "Todos" },
    ].concat(old_estados);
    setEstados(new_estados);
  };

  const fetch_cidades = async (estado) => {
    if (estado !== 0) {
      const old_cidades = await _fetch_cidades(estado);
      const new_cidades = [
        { codigoM: 0, federativaCodigoUf: 0, nomeM: "Todos" },
      ].concat(old_cidades);
      setCidades(new_cidades);
    }
  };

  const fetch_escolas = async (params) => {
    const old_escolas = await _fetch_escolas(params);
    setCountPages(Math.ceil(old_escolas[0]));
    setEscolas(old_escolas[1]);
  };

  const fetch_escola = async (id) => {
    const escola_fetch = await _fetch_escola(id);
    setEscola(escola_fetch);
  };

  const resetData = () => {
    setPage(1);
    setEstado(0);
    setCidade(0);
    setRede(0);
    setLocalizacao(0);
    setCapital(0);
    setSearch("");
  };

  return (
    <AppContext.Provider
      value={{
        capital,
        cidade,
        cidades,
        countPages,
        escola,
        escolas,
        estado,
        estados,
        localizacao,
        rede,
        search,
        page,
        capitalList,
        localizacaoList,
        redeList,
        fetch_cidades,
        fetch_escola,
        fetch_escolas,
        fetch_estados,
        resetData,
        setCapital,
        setCidade,
        setCidades,
        setCountPages,
        setEscola,
        setEscolas,
        setEstado,
        setEstados,
        setLocalizacao,
        setPage,
        setRede,
        setSearch,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export function useAppFetch() {
  const context = useContext(AppContext);

  if (!context) {
    throw new Error("useAppFetch must be used within an AppProvider");
  }

  return context;
}
