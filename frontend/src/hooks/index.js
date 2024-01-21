import React from "react";
import { AppProvider } from "./fetch";

const HooksProvider = ({ children }) => {
  return (
    <AppProvider>{children}</AppProvider>
  );
};


export default HooksProvider;
