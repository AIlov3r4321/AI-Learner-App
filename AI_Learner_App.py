
import streamlit as st
import pandas as pd

# Bestandsnaam om voortgang op te slaan
FILE_NAME = "ai_learning_progress.csv"

# Controleer of er een bestaand voortgangsbestand is
try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    df = pd.DataFrame({
        "Week": list(range(1, 13)),
        "Thema": [
            "Eerste AI-model trainen", "Automatiseren met AI", "AI-chatbots en tekst", "Data en AI",
            "AI en beeldherkenning", "Simpele trading bot", "AI en e-mailautomatisering", "AI en stemherkenning",
            "AI en sentimentanalyse", "AI en data scraping", "AI en trading bots combineren", "Jouw AI-project presenteren"
        ],
        "Doel": [
            "Begrijpen hoe AI patronen herkent en je eigen AI trainen",
            "Een AI laten helpen bij automatisering zonder code",
            "Een chatbot bouwen en testen",
            "AI gebruiken om data te analyseren",
            "AI laten herkennen wat op een afbeelding staat",
            "Een geautomatiseerd handelssysteem maken",
            "AI inzetten om e-mails automatisch te verwerken",
            "AI gebruiken voor spraakherkenning",
            "AI laten analyseren wat mensen schrijven",
            "Data van websites scrapen en AI inzetten voor analyse",
            "Een trading bot maken die AI gebruikt",
            "Een showcase maken van je AI-projecten"
        ],
        "Status": ["Niet gestart"] * 12,
        "Notities": [""] * 12
    })

st.title("📌 AI Leerplan Tracker")
st.write("Gebruik deze web-app om je AI-leerproces bij te houden en uit te breiden.")

# Loop door elke week en geef interactieve invoer
for index, row in df.iterrows():
    st.subheader(f"Week {row['Week']}: {row['Thema']}")
    st.write(f"**Doel:** {row['Doel']}")

    # Status dropdown
    status_options = ["Niet gestart", "Bezig", "Afgerond"]
    new_status = st.selectbox(f"Status voor Week {row['Week']}:", status_options, index=status_options.index(row["Status"]), key=f"status_{row['Week']}")

    # Notities invoeren
    new_notes = st.text_area(f"Notities voor Week {row['Week']}:", row["Notities"], key=f"notes_{row['Week']}")

    # Update dataframe
    df.at[index, "Status"] = new_status
    df.at[index, "Notities"] = new_notes

# Opslaan knop
if st.button("💾 Voortgang opslaan"):
    df.to_csv(FILE_NAME, index=False)
    st.success("Voortgang opgeslagen!")

st.write("🚀 Blijf experimenteren en leren!")
