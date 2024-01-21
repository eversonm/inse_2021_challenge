import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Header from "../header";
import HooksProvider from "../hooks";
import Dashboard from "../pages/dashboard";
import DefaultPage from "../pages/inse";

const AppRoutes = () => {
  return (
    <HooksProvider>
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/"  element={<DefaultPage />}/>
          <Route path="/dashboard"  element={<Dashboard />}/>
          <Route path="/escolas"  element={<Dashboard />}/>
        </Routes>
      </BrowserRouter>
    </HooksProvider>
    )
  };
  
  export default AppRoutes;
