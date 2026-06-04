import streamlit as st

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="מסייע תוצאות מעבדה",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS – RTL + healthcare theme ───────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Heebo', sans-serif;
    direction: rtl;
    text-align: right;
}

/* Sidebar RTL */
section[data-testid="stSidebar"] {
    direction: rtl;
    text-align: right;
}

/* Main background */
.main { background-color: #f0f4f8; }
.block-container { padding: 2rem 2rem 4rem 2rem; }

/* Cards */
.card {
    background: white;
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
    direction: rtl;
}
.card-blue  { border-right: 5px solid #2563eb; }
.card-green { border-right: 5px solid #16a34a; }
.card-red   { border-right: 5px solid #dc2626; }
.card-amber { border-right: 5px solid #d97706; }
.card-gray  { border-right: 5px solid #6b7280; }

/* Patient header */
.patient-header {
    background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%);
    color: white;
    border-radius: 16px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.5rem;
    direction: rtl;
}
.patient-header h2 { color: white; margin: 0 0 0.3rem 0; font-size: 1.5rem; }
.patient-header p  { color: #bfdbfe; margin: 0; font-size: 0.95rem; }

/* Section titles */
.section-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #1e3a5f;
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    direction: rtl;
}

/* Test result rows */
.result-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.6rem 0;
    border-bottom: 1px solid #f1f5f9;
    direction: rtl;
    flex-wrap: wrap;
    gap: 0.3rem;
}
.result-row:last-child { border-bottom: none; }
.test-name  { font-weight: 600; color: #374151; min-width: 140px; }
.test-value { font-size: 1.05rem; font-weight: 700; }
.test-range { font-size: 0.82rem; color: #6b7280; }

.badge {
    display: inline-block;
    padding: 0.2rem 0.65rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
}
.badge-normal   { background:#dcfce7; color:#166534; }
.badge-abnormal { background:#fee2e2; color:#991b1b; }
.badge-warning  { background:#fef9c3; color:#92400e; }

/* Explanation bullets */
.explanation-item {
    background: #f8fafc;
    border-radius: 10px;
    padding: 0.8rem 1rem;
    margin-bottom: 0.6rem;
    border-right: 3px solid #2563eb;
    direction: rtl;
    font-size: 0.93rem;
    line-height: 1.6;
    color: #374151;
}

/* Question bullets */
.question-item {
    background: #f0fdf4;
    border-radius: 10px;
    padding: 0.75rem 1rem;
    margin-bottom: 0.55rem;
    border-right: 3px solid #16a34a;
    direction: rtl;
    font-size: 0.92rem;
    color: #14532d;
}

/* Disclaimer */
.disclaimer {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    direction: rtl;
    font-size: 0.88rem;
    color: #78350f;
    line-height: 1.7;
}

/* Sidebar patient cards */
.sidebar-patient {
    background: white;
    border-radius: 10px;
    padding: 0.75rem 1rem;
    margin-bottom: 0.5rem;
    cursor: pointer;
    direction: rtl;
    border: 2px solid transparent;
}
.sidebar-patient:hover { border-color: #2563eb; }

/* App title in sidebar */
.app-title {
    color: #1e3a5f;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
    direction: rtl;
}
.app-subtitle {
    color: #64748b;
    font-size: 0.82rem;
    margin-bottom: 1.2rem;
    direction: rtl;
}

h3, h4 { direction: rtl; text-align: right; }

/* Force RTL on all streamlit text */
p, li, label, span { direction: rtl; }
</style>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
REFERENCE_RANGES = {
    "WBC":        {"unit": "×10³/µL", "min": 4.5,  "max": 11.0, "name_he": "תאי דם לבנים (WBC)"},
    "Hemoglobin": {"unit": "g/dL",    "min": 12.0, "max": 17.5, "name_he": "המוגלובין"},
    "Ferritin":   {"unit": "ng/mL",   "min": 15.0, "max": 200.0,"name_he": "פריטין"},
    "HbA1c":      {"unit": "%",       "min": 4.0,  "max": 5.7,  "name_he": "המוגלובין מסוכרר (HbA1c)"},
    "LDL":        {"unit": "mg/dL",   "min": 0.0,  "max": 100.0,"name_he": "כולסטרול LDL"},
}

PATIENTS = [
    {
        "id": 1,
        "name": "מרים כהן",
        "age": 34,
        "gender": "נקבה",
        "scenario": "פריטין נמוך",
        "icon": "🩸",
        "results": {
            "WBC":        11.0,
            "Hemoglobin": 12.8,
            "Ferritin":   6.2,
            "HbA1c":      5.3,
            "LDL":        88.0,
        },
        "explanations": [
            "🔴 רמת הפריטין שלך נמוכה מהטווח המקובל. פריטין הוא חלבון שמאחסן ברזל בגוף – רמה נמוכה עלולה להצביע על מאגרי ברזל מנוצלים.",
            "זה עלול להיות קשור לתחושות עייפות, חולשה, קוצר נשימה וקשיי ריכוז.",
            "מחסור בברזל שכיח בקרב נשים בגיל הפוריות, בעיקר עקב מחזור חודשי, תזונה דלת ברזל, או צרכים מוגברים.",
            "✅ כל הערכים שנבדקו נמצאים בטווח התקין. יש להמשיך במעקב רפואי שגרתי בהתאם להמלצת הרופא המטפל.",
        ],
        "questions": [
            "מה גרם לירידה בפריטין שלי – תזונה, ספיגה, או סיבה אחרת?",
            "האם אני צריכה לקחת תוסף ברזל, ואם כן – באיזה סוג ומינון?",
            "האם כדאי לבדוק גורמים נוספים כמו מחלת מעי דלקתית או צליאק?",
            "מתי ומה כדאי לאכול כדי לשפר את ספיגת הברזל מהמזון?",
            "מתי לחזור לבדיקת מעקב לאחר תחילת הטיפול?",
        ],
    },
    {
        "id": 2,
        "name": "יוסף לוי",
        "age": 52,
        "gender": "זכר",
        "scenario": "WBC מוגבר",
        "icon": "🦠",
        "results": {
            "WBC":        14.3,
            "Hemoglobin": 14.1,
            "Ferritin":   87.0,
            "HbA1c":      5.5,
            "LDL":        95.0,
        },
        "explanations": [
            "🔴 ספירת תאי הדם הלבנים שלך גבוהה מהטווח הרגיל. תאי דם לבנים הם תאים שחלק מתפקידם קשור לתגובות בגוף.",
            "עלייה בספירה עלולה להיות קשורה לתגובה זמנית לזיהום, דלקת, סטרס פיזי, או לתרופות מסוימות.",
            "ברוב המקרים מדובר בממצא שכדאי לבחון בעת ביקור הרופא בכדי להבין את הסיבה.",
            "✅ כל שאר הבדיקות – המוגלובין, פריטין, HbA1c ו-LDL – בטווח תקין.",
        ],
        "questions": [
            "מה הסיבה הסבירה ביותר לעלייה בתאי דם לבנים שלי?",
            "האם יש צורך בבדיקות דם נוספות כדי לברר את הסיבה?",
            "האם מדובר בממצא חד-פעמי שכדאי לחזור ולבדוק?",
            "האם יש תסמינים שעליי לשים לב אליהם בתקופה הקרובה?",
            "מה הצעדים הבאים אם הבדיקה החוזרת תשאר מוגבהת?",
        ],
    },
    {
        "id": 3,
        "name": "דוד ורדי",
        "age": 61,
        "gender": "זכר",
        "scenario": "HbA1c ו-LDL מוגברים",
        "icon": "🫀",
        "results": {
            "WBC":        7.2,
            "Hemoglobin": 13.9,
            "Ferritin":   112.0,
            "HbA1c":      6.8,
            "LDL":        138.0,
        },
        "explanations": [
            "🔴 רמת ה-HbA1c שלך (6.8%) גבוהה מהטווח התקין. בדיקה זו משקפת את רמת הסוכר הממוצעת בדם בשלושת החודשים האחרונים.",
            "ערך זה גבוה מהטווח התקין ודורש דיון עם הרופא לגבי משמעותו והמשך הבירור.",
            "🔴 רמת ה-LDL שלך (138 mg/dL) גבוהה. LDL הוא סוג של כולסטרול שעלול להצטבר בעורקים.",
            "שני ממצאים אלה יחד מצביעים על חשיבות שינויים באורח החיים – תזונה, פעילות גופנית – וייתכן טיפול תרופתי.",
            "✅ ה-WBC, המוגלובין והפריטין שלך תקינים.",
        ],
        "questions": [
            "האם רמת ה-HbA1c שלי דורשת דיון עם הרופא בנוגע לצעדים הבאים?",
            "אילו שינויים תזונתיים יכולים להיות רלוונטיים?",
            "האם יש צורך בתרופות, ואם כן – איזה סוג?",
            "מה המלצות הרופא בנוגע לפעילות גופנית?",
            "מתי לחזור לבדיקת מעקב, ואיזה יעד עליי להגיע אליו?",
        ],
    },
    {
        "id": 4,
        "name": "שרה אברהם",
        "age": 45,
        "gender": "נקבה",
        "scenario": "המוגלובין נמוך",
        "icon": "💊",
        "results": {
            "WBC":        6.8,
            "Hemoglobin": 10.2,
            "Ferritin":   22.0,
            "HbA1c":      5.1,
            "LDL":        91.0,
        },
        "explanations": [
            "🔴 רמת ההמוגלובין שלך נמוכה מהטווח התקין לנשים. המוגלובין הוא החלבון בתאי הדם האדומים שתפקידו קשור להובלה בגוף.",
            "רמה נמוכה עלולה להיות קשורה לתחושות עייפות, חולשה, סחרחורת ודיפיקויות אחרות.",
            "הפריטין שלך נמצא בתחתית הטווח התקין – יש צורך במעקב ובדיון עם הרופא בנוגע לגורמים אפשריים.",
            "✅ ה-WBC, HbA1c ו-LDL שלך תקינים. כל הערכים שנבדקו נמצאים בטווח התקין.",
        ],
        "questions": [
            "מה הסיבה הפוטנציאלית לרמה הנמוכה – מחסור בברזל, בוויטמין B12, או אחר?",
            "האם נדרשות בדיקות נוספות כדי לבחון זאת?",
            "האם יש צורך בטיפול, ואם כן – מה הטיפול המתאים?",
            "אילו מזונות מומלץ לי לצרוך?",
            "מה עלי לצפות לאחר תחילת הטיפול, ובאיזה מסגרת זמנית?",
        ],
    },
]


# ── Helpers ────────────────────────────────────────────────────────────────────
def classify(test_key, value):
    ref = REFERENCE_RANGES[test_key]
    if value < ref["min"]:
        return "low"
    elif value > ref["max"]:
        return "high"
    return "normal"


def status_badge(status):
    if status == "normal":
        return '<span class="badge badge-normal">תקין ✓</span>'
    elif status == "low":
        return '<span class="badge badge-abnormal">נמוך ▼</span>'
    else:
        return '<span class="badge badge-abnormal">גבוה ▲</span>'


def value_color(status):
    if status == "normal":
        return "#16a34a"
    return "#dc2626"


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="app-title">🧬 מסייע תוצאות מעבדה</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">כלי AI להסבר בדיקות דם בשפה ידידותית למטופל</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**בחר/י תרחיש מטופל:**")

    patient_names = [f"{p['icon']} {p['name']} – {p['scenario']}" for p in PATIENTS]
    selected_idx = st.radio("", patient_names, label_visibility="collapsed")
    selected_patient = PATIENTS[patient_names.index(selected_idx)]

    st.markdown("---")
    st.markdown("""
<div style='font-size:0.78rem; color:#94a3b8; direction:rtl; line-height:1.6;'>
⚠️ <strong>כלי זה מיועד להמחשה בלבד.</strong><br>
כל הנתונים הם סינתטיים.<br>
אין להשתמש בו לצורכי אבחון או טיפול רפואי.
</div>
""", unsafe_allow_html=True)


# ── Main content ───────────────────────────────────────────────────────────────
p = selected_patient

# Patient header
st.markdown(f"""
<div class="patient-header">
    <h2>{p['icon']} {p['name']}</h2>
    <p>גיל: {p['age']} &nbsp;|&nbsp; מין: {p['gender']} &nbsp;|&nbsp; תרחיש: {p['scenario']}</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="medium")

# ── Left column: test results ──────────────────────────────────────────────────
with col1:
    st.markdown('<div class="section-title">🔬 תוצאות בדיקות דם</div>', unsafe_allow_html=True)

    rows_html = ""
    for test_key, value in p["results"].items():
        ref = REFERENCE_RANGES[test_key]
        status = classify(test_key, value)
        color = value_color(status)
        badge = status_badge(status)
        range_str = f"טווח תקין: {ref['min']}–{ref['max']} {ref['unit']}"
        rows_html += f"""
<div class="result-row">
    <span class="test-name">{ref['name_he']}</span>
    <span class="test-value" style="color:{color};">{value} {ref['unit']}</span>
    {badge}
    <span class="test-range">{range_str}</span>
</div>
"""

    st.markdown(f'<div class="card card-blue">{rows_html}</div>', unsafe_allow_html=True)

    # Summary badges
    abnormal_tests = [
        REFERENCE_RANGES[k]["name_he"]
        for k, v in p["results"].items()
        if classify(k, v) != "normal"
    ]
    normal_count = len(p["results"]) - len(abnormal_tests)

    st.markdown(f"""
<div class="card card-gray" style="padding:0.9rem 1.2rem;">
    <div style="display:flex; gap:1rem; flex-wrap:wrap; direction:rtl;">
        <span class="badge badge-normal">✓ {normal_count} ממצאים תקינים</span>
        <span class="badge badge-abnormal">⚠ {len(abnormal_tests)} ממצאים חריגים</span>
    </div>
    {'<p style="margin:0.6rem 0 0; font-size:0.87rem; color:#374151;">ממצאים הדורשים תשומת לב: ' + '، '.join(abnormal_tests) + '</p>' if abnormal_tests else ''}
</div>
""", unsafe_allow_html=True)


# ── Right column: explanations + questions ────────────────────────────────────
with col2:
    st.markdown('<div class="section-title">💬 הסבר בשפה ידידותית</div>', unsafe_allow_html=True)
    exp_html = "".join(
        f'<div class="explanation-item">{line}</div>'
        for line in p["explanations"]
    )
    st.markdown(f'<div class="card card-blue" style="padding:1rem 1.2rem;">{exp_html}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🩺 שאלות מומלצות לרופא/ה</div>', unsafe_allow_html=True)
    q_html = "".join(
        f'<div class="question-item">❓ {q}</div>'
        for q in p["questions"]
    )
    st.markdown(f'<div class="card card-green" style="padding:1rem 1.2rem;">{q_html}</div>', unsafe_allow_html=True)


# ── Disclaimer (full width) ────────────────────────────────────────────────────
st.markdown("""
<div class="disclaimer">
    <strong>⚠️ כתב ויתור חשוב:</strong>
    המידע המוצג בכלי זה מיועד למטרות <strong>חינוכיות והמחשה בלבד</strong>, ואינו מהווה ייעוץ רפואי, אבחון, או המלצה לטיפול.
    כל הנתונים הם <strong>סינתטיים לחלוטין</strong> ואינם שייכים למטופלים אמיתיים.
    בכל שאלה רפואית יש לפנות לרופא/ה המטפל/ת.
    אין להסתמך על כלי זה לקבלת החלטות רפואיות מכל סוג שהוא.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; direction:rtl; color:#94a3b8; font-size:0.78rem; margin-top:2rem;">
    מסייע תוצאות מעבדה – הוכחת היתכנות (PoC) | כל הנתונים סינתטיים | אינו מחליף ייעוץ רפואי
</div>
""", unsafe_allow_html=True)
