import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import base64


# ---------------- LOAD MODEL ----------------

model = joblib.load("employee_model.pkl")
encoders = joblib.load("encoders.pkl")


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Employee Retention Predictor",
    page_icon="📊",
    layout="wide"
)


# ---------------- CSS ----------------

# Custom Styling

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right,#6fa8dc,#e3f2fd);
}

h1 {
    color: #0d47a1;
    text-align: center;
}

.block-container {
    padding-top: 2rem;
}
.white-bg-container {
    background-color: white;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}
div[data-testid="stVerticalBlockBorderWrapper"]:has(div.white-bg) {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
    }
.employee-card {
    background-color: white !important;
    padding: 25px;
    border-radius: 30px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.15);
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Use !important to override Streamlit's default colors */
.personal-header { 
    color: #6a1b9a !important; 
    font-size: 20px !important; 
    font-weight: bold !important; 
    margin-bottom: 10px !important;
}
 /* Target labels in the first column to make them purple */
  [data-testid="column"]:(nth-of-type(1)) 
   div[data-testid="stWidget"] label {
    color: #6a1b9a !important;
    font-weight: 600 !important;
}

.work-header { 
    color: #2e7d32 !important; 
    font-size: 20px !important; 
    font-weight: bold !important; 
    margin-bottom: 10px !important;
}
 [data-testid="column"]:(nth-of-type(2)) 
    div[data-testid="stWidget"] label {
    color: #2e7d32 !important;
    font-weight: 600 !important;
}
/* Prediction Button - Make it full width and colored */
div.stButton > button {
    width: 100%;
    background-color: #6a1b9a;
    color: white;
    font-size: 18px;
    height: 3em;
}

</style>
""", unsafe_allow_html=True)



# ---------------- TITLE ----------------
def get_base64(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64("banner.jpg")
st.markdown(f"""
<style>
.hero-container {{
    position: relative;
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    border-radius: 20px;
    padding: 60px 40px;
    margin-bottom: 30px;
    /* This creates the dark overlay */
    background-color: rgba(0, 0, 0, 0.5); 
    background-blend-mode: darken;
}}

.hero-text {{
    color: white;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}}

.hero-text h1 {{
    color: white !important;
    font-size: 3rem;
    margin-bottom: 10px;
}}

.hero-text p {{
    color: #e0e0e0;
    font-size: 1.25rem;
    max-width: 70%;
}}
</style>

<div class="hero-container">
    <div class="hero-text">
        <h1>📊 Employee Retention Prediction</h1>
        <p>Predict whether an employee is likely to leave the company based on profile and work experience.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- EMPLOYEE INFORMATION ----------------
with st.container(border=True):
    st.markdown('<div class="white-bg"></div>', unsafe_allow_html=True)

    st.markdown("## 📊 Employee Information")
    st.caption("Fill in the details below to get the prediction")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown('<div class="personal-header">🎓 Personal & Education Details</div>',unsafe_allow_html=True)
        st.markdown('<p style="color:#6a1b9a;font-weight:bold;margin-bottom:0px;">🏙️ City </p>',unsafe_allow_html=True)
        city = st.selectbox("City", encoders["city"].classes_,label_visibility="collapsed")

        st.markdown('<p style="color:#6a1b9a;font-weight:bold;margin-bottom:0px;"> 👤 Gender</p>',unsafe_allow_html=True)
        gender = st.selectbox("👤 Gender", encoders["gender"].classes_,label_visibility="collapsed")

        st.markdown('<p style="color:#6a1b9a;font-weight:bold;margin-bottom:0px;">💼 Relevant Experience </p>',unsafe_allow_html=True)
        relevent_experience = st.selectbox(
            "💼 Relevant Experience",
            encoders["relevent_experience"].classes_,label_visibility="collapsed"
        )

        st.markdown('<p style="color:#6a1b9a;font-weight:bold;margin-bottom:0px;"> 🎓 Enrolled University</p>',unsafe_allow_html=True)
        enrolled_university = st.selectbox(
            "🎓 Enrolled University",
            encoders["enrolled_university"].classes_,label_visibility="collapsed"
        )
        
        st.markdown('<p style="color:#6a1b9a;font-weight:bold;margin-bottom:0px;">📚 Education Level</p>',unsafe_allow_html=True)
        education_level = st.selectbox(
            "📚 Education Level",
            encoders["education_level"].classes_,label_visibility="collapsed"
        )

        st.markdown('<p style="color:#6a1b9a;font-weight:bold;margin-bottom:0px;">🧑‍🎓 Major Discipline</p>',unsafe_allow_html=True)
        major_discipline = st.selectbox(
            "🧑‍🎓 Major Discipline",
            encoders["major_discipline"].classes_,label_visibility="collapsed"
        )

    with col2:

        st.markdown('<div class="work-header"> 💼 Work & Experience Details</div>',unsafe_allow_html=True)

        st.markdown('<p style="color:#2e7d32;font-weight:bold;margin-bottom:0px;">🏢 Company Size</p>',unsafe_allow_html=True)
        company_size = st.selectbox(
            "🏢 Company Size",
            encoders["company_size"].classes_,label_visibility="collapsed"
        )
        st.markdown('<p style="color:#2e7d32;font-weight:bold;margin-bottom:0px;">🏭 Company Type</p>',unsafe_allow_html=True)
        company_type = st.selectbox(
            "🏭 Company Type",
            encoders["company_type"].classes_,label_visibility="collapsed"
        )
        st.markdown('<p style="color:#2e7d32;font-weight:bold;margin-bottom:0px;">🔄 Last New Job</p>',unsafe_allow_html=True)
        last_new_job = st.selectbox(
            "🔄 Last New Job",
            encoders["last_new_job"].classes_,label_visibility="collapsed"
        )
        st.markdown('<p style="color:#2e7d32;font-weight:bold;margin-bottom:0px;">📈 City Development Index</p>',unsafe_allow_html=True)
        city_development_index = st.slider(
            "📈 City Development Index",
            0.0, 1.0, 0.65,label_visibility="collapsed"
        )
        st.markdown('<p style="color:#2e7d32;font-weight:bold;margin-bottom:0px;">🛠️ Years of Experience</p>',unsafe_allow_html=True)
        experience = st.number_input(
            "🛠️ Years of Experience",
            0, 30, 8,label_visibility="collapsed"
        )
        st.markdown('<p style="color:#2e7d32;font-weight:bold;margin-bottom:0px;">⏰ Training Hours</p>',unsafe_allow_html=True)
        training_hours = st.number_input(
            "⏰ Training Hours",
            1, 200, 60,label_visibility="collapsed"
        )

predict_btn=st.button("🚀 Predict Now")

st.markdown('</div>',unsafe_allow_html=True)

# ---------------- PREDICTION ----------------


if predict_btn:


    data = pd.DataFrame({

        "city":[
            encoders["city"].transform([city])[0]
        ],

        "city_development_index":[
            city_development_index
        ],

        "gender":[
            encoders["gender"].transform([gender])[0]
        ],

        "relevent_experience":[
            encoders["relevent_experience"].transform([relevent_experience])[0]
        ],

        "enrolled_university":[
            encoders["enrolled_university"].transform([enrolled_university])[0]
        ],

        "education_level":[
            encoders["education_level"].transform([education_level])[0]
        ],

        "major_discipline":[
            encoders["major_discipline"].transform([major_discipline])[0]
        ],

        "experience":[experience],

        "company_size":[
            encoders["company_size"].transform([company_size])[0]
        ],

        "company_type":[
            encoders["company_type"].transform([company_type])[0]
        ],

        "last_new_job":[
            encoders["last_new_job"].transform([last_new_job])[0]
        ],

        "training_hours":[training_hours]

    })



    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]



    st.markdown("---")

    st.subheader("📋 Prediction Result")


    if prediction == 1:

        st.error(
            f"⚠️ Employee is likely to change job\n\nConfidence: {probability:.2%}"
        )

    else:

        st.success(
            f"✅ Employee is likely to stay\n\nConfidence: {(1-probability):.2%}"
        )



    stay = (1-probability)*100

    change = probability*100



    st.markdown("## 📊 Retention Analysis")



    c1,c2 = st.columns(2)



    with c1:

        fig,ax = plt.subplots(figsize=(3,3))

        ax.pie(
            [stay,100-stay],
            startangle=90,
            colors=["green","#eeeeee"],
            wedgeprops={"width":0.25}
        )

        ax.text(
            0,0,
            f"{stay:.2f}%",
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold"
        )

        ax.set_title("Stay Probability")

        st.pyplot(fig)




    with c2:

        fig,ax = plt.subplots(figsize=(3,3))

        ax.pie(
            [change,100-change],
            startangle=90,
            colors=["red","#eeeeee"],
            wedgeprops={"width":0.25}
        )

        ax.text(
            0,0,
            f"{change:.2f}%",
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold"
        )


        ax.set_title("Job Change Probability")

        st.pyplot(fig)