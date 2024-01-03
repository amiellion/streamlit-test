import os
import streamlit.components.v1 as components
import streamlit as st


# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "my_component",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    print("RELEASE")
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "aggrid_react\\frontend\\dist")
    print(build_dir)
    _component_func = components.declare_component("my_component", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def my_component(name, rowData=None, key=None):

    if rowData is None:
        rowData = [
            {
                "mission": "Voyager",
                "company": "NASA",
                "location": "Cape Canaveral",
                "date": "1977-09-05",
                "rocket": "Titan-Centaur",
                "price": 86580000,
                "successful": True,
            },
            {
                "mission": "Apollo 13",
                "company": "NASA",
                "location": "Kennedy Space Center",
                "date": "1970-04-11",
                "rocket": "Saturn V",
                "price": 3750000,
                "successful": False,
            },
            {
                "mission": "Falcon 9",
                "company": "SpaceX",
                "location": "Cape Canaveral",
                "date": "2015-12-22",
                "rocket": "Falcon 9",
                "price": 9750000,
                "successful": True,
            },
        ]

    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(name=name, rowData=rowData, key=key, default=0)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value


def aggrid_react(page_names_to_funcs): 
    st.markdown(f"# {list(page_names_to_funcs.keys())[5]}")
    st.write(
        """
        This demo shows how to use `AgGrid` as React component to visualize data.
        
        Based on [this example](https://streamlit-components-tutorial.netlify.app/introduction/project-setup/)
        """
    )

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    num_clicks = my_component("World")
    st.markdown("You've clicked %s times!" % int(num_clicks))

    # st.markdown("---")
    # st.subheader("Component with variable args")
    # my_component("React Component")

