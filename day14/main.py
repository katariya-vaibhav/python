import streamlit as st


def main():
    st.title("Test Streamlit App")
    st.subheader("Challenge")
    st.write("This is a placeholder for the Explore Streamlit.")
    
    if st.button("Click me!"):
        st.success("Button clicked!")
        st.balloons()


if __name__ == "__main__":
    main()
