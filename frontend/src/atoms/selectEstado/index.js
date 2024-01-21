import { FormControl, InputLabel, MenuItem, Select } from "@mui/material";
import React from "react";
import { useAppFetch } from "../../hooks/fetch";

const SelectCustomEstado = ({ nameMenu, itemsMenu }) => {
  const { estado, setEstado } = useAppFetch();

  const handleChange = (event) => {
    setEstado(event.target.value);
  };

  return (
    <FormControl fullWidth>
      <InputLabel id="demo-simple-select-label">{nameMenu}</InputLabel>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        value={estado}
        label={nameMenu}
        onChange={handleChange}
      >
        {itemsMenu.map((item) => (
          <MenuItem
            key={`${item.codigoUf}-${item.siglaUf}`}
            value={item.codigoUf}
          >
            {item.nomeUf}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default SelectCustomEstado;
