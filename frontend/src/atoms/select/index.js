import { FormControl, InputLabel, MenuItem, Select } from "@mui/material";
import React from "react";

const SelectCustom = ({nameMenu, itemsMenu}) => {

  const [age, setAge] = React.useState('');

  const handleChange = (event) => {
    setAge(event.target.value);
  };

  return (
    <FormControl fullWidth>
      <InputLabel id="demo-simple-select-label">{nameMenu}</InputLabel>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        value={age}
        label={nameMenu}
        onChange={handleChange}
      >
        {itemsMenu.map((item) => (
          <MenuItem key={`${item.id}-${item.tipo}`} value={item.id}>{item.tipo}</MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default SelectCustom