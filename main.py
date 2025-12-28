import streamlit as st

st.subheader("mSTaRT Vorsichtung")

if st.radio("Patient gefähig?", options=["Ja", "Nein"], index=None) == "Ja":
    st.success("GRÜN &rarr; Patient zur Sammelstelle schicken.")
    st.link_button("Neuer Patient", "/", use_container_width=True)
    st.stop()

if st.radio("Atmung vorhanden?", options=["Ja", "Nein"], index=None) == "Nein":
    st.markdown("**Atemwege freimachen, wenn nötig!**")

    atmung_nach_freimachen = st.radio("Atmung nach Freimachen vorhanden?", options=["Ja", "Nein"], index=None)
    if atmung_nach_freimachen == "Nein":
        st.warning("Schwarz &rarr; Weiter mit nächstem Patienten.")
        st.link_button("Neuer Patient", "/", use_container_width=True)
        st.stop()

if st.radio("Abnormale Atemfrequenz? (Mehr als 5 oder weniger als 2 Atemzüge innerhalb von 10 Sekunden)", options=["Ja", "Nein"], index=None) == "Ja":
    st.error("Rot &rarr; Stabile Seitenlage")
    st.link_button("Neuer Patient", "/", use_container_width=True)
    st.stop()

if st.radio ("Spritzende Blutung vorhanden?", options=["Ja", "Nein"], index=None) == "Ja":
    st.error("Rot &rarr; ggfs. Stabile Seitenlage")
    st.link_button("Neuer Patient", "/", use_container_width=True)
    st.stop()

last_check = st.radio("Unfähig einfache Aufforderungen zu befolgen? (z.B. \"Folgen Sie mit den Augen meiner Handbewegung!\")", options=["Ja", "Nein"], index=None)
if last_check == "Ja":
    st.error("Rot &rarr; Stabile Seitenlage")
    st.link_button("Neuer Patient", "/", use_container_width=True)
elif last_check == "Nein":
    st.warning("Gelb")
    st.link_button("Neuer Patient", "/", use_container_width=True)
