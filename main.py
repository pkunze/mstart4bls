import streamlit as st

st.subheader("mSTaRT Vorsichtung")

walking_answer = st.radio("Patient gehfähig?", options=["Ja", "Nein"], index=None)

if walking_answer is None:
    st.stop()

if walking_answer == "Ja":
    st.success("**GRÜN** &rarr; Patient zur Sammelstelle schicken.")
    st.link_button("Neuer Patient", "/", use_container_width=True)
    st.stop()

breathing_answer = st.radio("Atmung vorhanden?", options=["Ja", "Nein"], index=None)

if breathing_answer is None:
    st.stop()

if breathing_answer == "Nein":
    st.markdown("**Atemwege freimachen, wenn nötig!**")

    atmung_nach_freimachen = st.radio("Atmung nach Freimachen vorhanden?", options=["Ja", "Nein"], index=None)
    
    if atmung_nach_freimachen is None:
        st.stop()

    if atmung_nach_freimachen == "Nein":
        st.info("**SCHWARZ** &rarr; Weiter mit nächstem Patienten.")
        st.link_button("Neuer Patient", "/", use_container_width=True)
        st.stop()

abnormal_breathing_frequency_answer = st.radio("**Abnormale** Atemfrequenz? (Mehr als 5 oder weniger als 2 Atemzüge innerhalb von 10 Sekunden)", options=["Ja", "Nein"], index=None)

if abnormal_breathing_frequency_answer is None:
    st.stop()

if abnormal_breathing_frequency_answer == "Ja":
    st.error("**ROT** &rarr; Stabile Seitenlage")
    st.link_button("Neuer Patient", "/", use_container_width=True)
    st.stop()

bleeding_answer = st.radio ("Spritzende Blutung vorhanden?", options=["Ja", "Nein"], index=None)

if bleeding_answer is None:
    st.stop()

if bleeding_answer == "Ja":
    st.error("**ROT** &rarr; wenn schnell möglich Druckverband/Tourniquet anlegen, ggfs. Stabile Seitenlage")
    st.link_button("Neuer Patient", "/", use_container_width=True)
    st.stop()

last_check = st.radio("Patient bewusstlos oder **Unfähig** einfache Aufforderungen zu befolgen? (Bspw. \"Folgen Sie mit den Augen meiner Handbewegung!\")", options=["Ja", "Nein"], index=None)
if last_check is None:
    st.stop()
elif last_check == "Ja":
    st.error("**ROT** &rarr; Stabile Seitenlage")
    st.link_button("Neuer Patient", "/", use_container_width=True)
elif last_check == "Nein":
    st.warning("**GELB**")
    st.link_button("Neuer Patient", "/", use_container_width=True)
