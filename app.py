
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Estymator kampanii influencerskiej")

st.title("Estymator kampanii influencerskiej")

uploaded_file = st.file_uploader("Wgraj plik Excel z danymi kampanii (opcjonalne)", type=["xlsx"])

# Podgląd danych z Excela
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("Podgląd danych z pliku:")
    st.dataframe(df)

# Sekcja do wprowadzania danych kampanii
st.subheader("Wprowadź dane kampanii")

zasięg = st.number_input("Zasięg influencera", min_value=0, value=100000, step=1000)
cpc = st.number_input("CPC (zł)", min_value=0.01, value=0.40, step=0.01)
er = st.number_input("Engagement Rate (%)", min_value=0.0, max_value=100.0, value=3.5, step=0.1) / 100

# Budżet interaktywny
budżet = st.slider("Budżet kampanii (zł)", min_value=100, max_value=50000, value=5000, step=100)

# Obliczenia
kliknięcia = budżet / cpc if cpc > 0 else 0
interakcje = zasięg * er

st.markdown("### Szacowane wyniki kampanii:")
st.write(f"**Kliknięcia:** {int(kliknięcia)}")
st.write(f"**Interakcje (like, komentarze):** {int(interakcje)}")

# WYKRES: wpływ budżetu na wyniki
st.subheader("Wpływ zmiany budżetu na wyniki kampanii")

budżety = list(range(100, 50001, 500))
kliknięcia_lista = [b / cpc for b in budżety]
interakcje_lista = [zasięg * er for _ in budżety]

fig, ax = plt.subplots()
ax.plot(budżety, kliknięcia_lista, label="Kliknięcia", color="blue")
ax.plot(budżety, interakcje_lista, label="Interakcje", color="green", linestyle="--")
ax.set_xlabel("Budżet (zł)")
ax.set_ylabel("Szacowana liczba")
ax.set_title("Budżet vs Wyniki kampanii")
ax.legend()
st.pyplot(fig)
