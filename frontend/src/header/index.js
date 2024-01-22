import { AppBar, Box, Button } from "@mui/material";
import React from "react";
import { useNavigate } from "react-router-dom";

const Header = () => {
  const navigate = useNavigate();
  const pages = ["Tela inicial", "Dashboard", "Escolas"];

  const switchPage = (page) => {
    switch (page) {
      case "Dashboard":
        return "/dashboard";
      case "Tela inicial":
        return "/";
      case "Escolas":
        return "/escolas";
      default:
        return "/";
    }
  };

  return (
    <AppBar position="static">
      <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
        {pages.map((page) => (
          <Button
            key={page}
            sx={{ my: 2, color: "white", display: "block" }}
            onClick={() => navigate(switchPage(page))}
          >
            {page}
          </Button>
        ))}
      </Box>
    </AppBar>
  );
};

export default Header;
