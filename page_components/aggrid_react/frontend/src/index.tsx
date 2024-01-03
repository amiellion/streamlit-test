import React, { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import ReactDOM from "react-dom"
import MyComponent from "./MyComponent"
import "ag-grid-community/styles/ag-grid.css" // Core CSS
import "ag-grid-community/styles/ag-theme-quartz.css" // Theme

const container = document.getElementById("root")
const root = createRoot(container!) // createRoot(container!) if you use TypeScript
root.render(
  <StrictMode>
    <MyComponent />
  </StrictMode>
)
