import streamlit as st
pazartesi = {
    "Legs": [
        {
            "isim": "Bulgarian Split Squat",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Goblet Squat",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Hip Thrusts",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Romanian Deadlift",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Standing Cable Hip Abduction",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Standing Cable Hip Adduction",
            "sets": 3,
            "reps": 8
        }
    ],
    "Core": [
        {
            "isim": "Plank",
            "sets": 2,
            "duration_seconds": 30 
        },
        {
            "isim": "Side Plank",
            "sets": 2,
            "duration_seconds": 30
        }
    ]
}



sali = {
    "Back" : [
        {
            "isim": "Lat Pulldown",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Single Arm Row",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Bent Over Row",
            "sets": 3,
            "reps": 8
        }
    ],
    "Shoulders": [
        {
            "isim": "Seated Dumbbell Press",
            "sets": 4,
            "reps": 8
        },
        {
            "isim": "Lateral Raises",
            "sets": 4,
            "reps": 8
        }
    ],
    "Arms": [
        {
            "isim": "Bicep Curls",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Standing Hammer Curls",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Triceps Extensions",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Seated Dumbbell Wrist Curls",
            "sets": 3,
            "reps": 8
        }
    ]
}

carsamba = {
    "Legs": [
        {
            "isim": "Bulgarian Split Squat",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Goblet Squat",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Hip Thrusts",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Romanian Deadlift",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Standing Cable Hip Abduction",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Standing Cable Hip Adduction",
            "sets": 3,
            "reps": 8
        }
    ],
    "Core": [
        {
            "isim": "Plank",
            "sets": 2,
            "duration_seconds": 30 
        },
        {
            "isim": "Side Plank",
            "sets": 2,
            "duration_seconds": 30
        }
    ]
}


persembe = {
    "Chest": [
        {
        "isim": "Bench Press",
        "sets": 4,
        "reps": 8
        }
    ],
    "Arms": [
            {
                "isim": "Bicep Curls",
                "sets": 3,
                "reps": 8
            },
            {
                "isim": "Standing Hammer Curls",
                "sets": 3,
                "reps": 8
            },
            {
                "isim": "Triceps Extensions",
                "sets": 3,
                "reps": 8
            },
            {
                "isim": "Seated Dumbbell Wrist Curls",
                "sets": 3,
                "reps": 8
            }
        ]
}


cuma = {
    "Legs": [
        {
            "isim": "Bulgarian Split Squat",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Goblet Squat",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Hip Thrusts",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Romanian Deadlift",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Standing Cable Hip Abduction",
            "sets": 3,
            "reps": 8
        },
        {
            "isim": "Standing Cable Hip Adduction",
            "sets": 3,
            "reps": 8
        }
    ],
    "Core": [
        {
            "isim": "Plank",
            "sets": 2,
            "duration_seconds": 30 
        },
        {
            "isim": "Side Plank",
            "sets": 2,
            "duration_seconds": 30
        }
    ]
}

haftalik_program = {
    "Pazartesi": pazartesi,
    "Salı": sali,
    "Çarşamba": carsamba,
    "Perşembe": persembe,
    "Cuma": cuma
}

st.title("Gym Planner")

secilen_gun = st.selectbox(
    "Antrenman gününü seç:",
    list(haftalik_program.keys())
)
gun_programi = haftalik_program[secilen_gun]

secilen_kas = st.selectbox(
    "Kas grubunu seç:",
    list(gun_programi.keys())
)

st.write(secilen_kas)


for egzersiz in gun_programi[secilen_kas]:
    kimlik = f"{secilen_gun}_{secilen_kas}_{egzersiz['isim']}"

    kayit_anahtari = f"kayit_{kimlik}"
    kutu_anahtari = f"kutu_{kimlik}"

    if kayit_anahtari not in st.session_state:
        st.session_state[kayit_anahtari] = False

    if kutu_anahtari not in st.session_state:
        st.session_state[kutu_anahtari] = st.session_state[kayit_anahtari]

    if "duration_seconds" in egzersiz:
        etiket = f"{egzersiz['isim']} - {egzersiz['sets']} set x {egzersiz['duration_seconds']} saniye"
    else:
        etiket = f"{egzersiz['isim']} - {egzersiz['sets']} set x {egzersiz['reps']} tekrar"

    st.checkbox(
        etiket,
        key=kutu_anahtari,
        on_change=lambda k=kayit_anahtari, w=kutu_anahtari: st.session_state.update(
            {k: st.session_state[w]}
        )
    )
