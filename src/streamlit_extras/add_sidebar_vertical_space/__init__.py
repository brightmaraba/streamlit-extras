from streamlit as st

from .. import extra

@extra
def add_sidebar_vertical_space(num_lines: int = 1):
  """Add vertical space to the sidebar of your Streamlit app."""
  for _ in range(num_lines):
    st.sidebar.write("")

def example():
  st.sidebar.write("Move the slider and check the spacing between the messages in the sidebar")
  add_n_lines = st.slider("Add n vertical lines below this", 1, 20, 5)
  st.sidebar.subtitle("First Message: Hello, World")
  add_sidebar_verticle_space(add_n_lines)
  st.sidebar.subtitle("Final Message: Goodbye, World")

__title__ = "Add Vertical Space to Sidebar"  # title of your extra!
__desc__ = "Add n lines of vertical space to the sidebar of your Streamlit app in one command"  # description of your extra!
__icon__ = "👽"  # give your extra an icon!
__examples__ = [example]  # create some examples to show how cool your extra is!
__author__ = "Brian Koech"
__experimental_playground__ = False  # Optional
  
