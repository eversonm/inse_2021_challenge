import { FormControl, InputLabel, MenuItem, Select } from "@mui/material";
import React from "react";
import { useAppFetch } from "../../hooks/fetch";

const SelectCustomMunicipio = ({ nameMenu, itemsMenu }) => {
  const {cidade, setCidade} = useAppFetch();

  const handleChange = (event) => {
    setCidade(event.target.value);
  };

  return (
    <FormControl fullWidth>
      <InputLabel id="demo-simple-select-label">{nameMenu}</InputLabel>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        value={cidade}
        label={nameMenu}
        onChange={handleChange}
      >
        {itemsMenu.map((item) => (
          <MenuItem key={`${item.codigoM}-${item.federativaCodigoUf}`} value={item.codigoM}>
            {item.nomeM}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default SelectCustomMunicipio;
