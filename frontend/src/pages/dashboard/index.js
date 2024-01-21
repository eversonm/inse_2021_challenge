import { Paper } from "@mui/material";
import React from "react";
import Plot from "react-plotly.js";

const Dashboard = () => {
  return (
    <Paper
      style={{
        height: "100%",
        backgroundColor: "white",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
      height="80vh"
    >
      <div
        className="App"
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      >
        <Plot
          data={[
            {
              x: [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18],
              y: [32, 37, 40.5, 43, 49, 54, 59, 63.5, 69.5, 73, 74],
              mode: "markers",
              type: "scatter",
            },
          ]}
          layout={{
            title: "Growth Rate in Boys",
            xaxis: {
              title: "Age (years)",
            },
            yaxis: {
              title: "Height (inches)",
            },
          }}
        />
      </div>
    </Paper>
  )
}

export default Dashboard