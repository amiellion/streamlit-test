import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import "ag-grid-community/styles/ag-grid.css" // Core CSS
import "ag-grid-community/styles/ag-theme-quartz.css" // Theme

import { AgGridReact } from "ag-grid-react" // React Grid Logic

interface State {
  numClicks: number
  isFocused: boolean
}

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class MyComponent extends StreamlitComponentBase<State> {
  public state = {
    numClicks: 0,
    isFocused: false,
    rowData: [
      {
        mission: "Voyager",
        company: "NASA",
        location: "Cape Canaveral",
        date: "1977-09-05",
        rocket: "Titan-Centaur ",
        price: 86580000,
        successful: true,
      },
      {
        mission: "Apollo 13",
        company: "NASA",
        location: "Kennedy Space Center",
        date: "1970-04-11",
        rocket: "Saturn V",
        price: 3750000,
        successful: false,
      },
      {
        mission: "Falcon 9",
        company: "SpaceX",
        location: "Cape Canaveral",
        date: "2015-12-22",
        rocket: "Falcon 9",
        price: 9750000,
        successful: true,
      },
    ],
    colDefs: [
      { field: "mission" },
      { field: "company" },
      { field: "location" },
      { field: "date" },
      { field: "price" },
      { field: "successful" },
      { field: "rocket" },
    ],
  }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    const name = this.props?.args["name"] || "asdasd"
    const rowData = this.props?.args["rowData"] || "asdasd"

    // Streamlit sends us a theme object via props that we can use to ensure
    // that our component has visuals that match the active theme in a
    // streamlit app.
    const { theme } = this.props
    const style: React.CSSProperties = {}

    // Maintain compatibility with older versions of Streamlit that don't send
    // a theme object.
    if (theme) {
      // Use the theme object to style our button border. Alternatively, the
      // theme style is defined in CSS vars.
      const borderStyling = `1px solid ${
        this.state.isFocused ? theme.primaryColor : "gray"
      }`
      style.border = borderStyling
      style.outline = borderStyling
    }

    // Show a button and some text.
    // When the button is clicked, we'll increment our "numClicks" state
    // variable, and send its new value back to Streamlit, where it'll
    // be available to the Python program.
    return (
      <>
        <span>
          Hello, {name}! &nbsp;
          <button
            style={style}
            onClick={this.onClicked}
            disabled={this.props.disabled}
            onFocus={this._onFocus}
            onBlur={this._onBlur}
          >
            Click Me!
          </button>
          <div className="ag-theme-quartz" style={{ height: 400, overflow:"auto" }}>
            <AgGridReact
              rowData={this.state.rowData}
              columnDefs={[
                { field: "mission" },
                { field: "company" },
                { field: "location" },
                { field: "date" },
                { field: "price" },
                { field: "successful" },
                { field: "rocket" },
              ]}
            />
          </div>
        </span>
      </>
    )
  }

  /** Click handler for our "Click Me!" button. */
  private onClicked = (): void => {
    // Increment state.numClicks, and pass the new value back to
    // Streamlit via `Streamlit.setComponentValue`.
    this.setState(
      (prevState) => ({ numClicks: prevState.numClicks + 1 }),
      () => Streamlit.setComponentValue(this.state.numClicks)
    )
  }

  /** Focus handler for our "Click Me!" button. */
  private _onFocus = (): void => {
    this.setState({ isFocused: true })
  }

  /** Blur handler for our "Click Me!" button. */
  private _onBlur = (): void => {
    this.setState({ isFocused: false })
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyComponent)
// export default MyComponent
