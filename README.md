```python
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="מערכת הסבר תוצאות בדיקות דם",
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
.main { background-color: #f5f7fa; }
.block-container { padding: 2rem 2.5rem 4rem 2.5rem; }

/* Cards */
.card {
    background: white;
    border-radius: 14px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    direction: rtl;
}
.card-blue  { border-right: 5px solid #2563eb; }
.card-green { border-right: 5px solid #16a34a; }
.card-red   { border-right: 5px solid #ef4444; }
.card-amber { border-right: 5px solid #f59e0b; }
.card-gray  { border-right: 5px solid #6b7280; }

/* Patient header */
.patient-header {
    background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%);
    color: white;
    border-radius: 16px;
    padding: 1.8rem 2.2rem;
    margin-bottom: 1.8rem;
    direction: rtl;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15);
}
.patient-header h2 { color: white; margin: 0 0 0.4rem 0; font-size: 1.6rem; font-weight: 700; }
.patient-header p  { color: #bfdbfe; margin: 0; font-size: 0.95rem; }

/* Section titles */
.section-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #1e3a5f;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    direction: rtl;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #e0e7ff;
}

/* Intro section */
.intro-section {
    background: linear-gradient(135deg, #eff6ff 0%, #f0fdfa 100%);
    border-radius: 14px;
    padding: 2rem 2.2rem;
    margin-bottom: 2rem;
    border-right: 5px solid #06b6d4;
    direction: rtl;
}
.intro-section h3 {
    font-size: 1.4rem;
    color: #0369a1;
    margin: 0 0 1rem 0;
    font-weight: 700;
    direction: rtl;
    text-align: right;
}
.intro-section p {
    font-size: 0.95rem;
    color: #164e63;
    line-height: 1.7;
    margin: 0.6rem 0;
    direction: rtl;
    text-align: right;
}

/* How it works section */
.how-it-works {
    background: white;
    border-radius: 14px;
    padding: 2rem;
    margin-bottom: 2rem;
    border-right: 5px solid #8b5cf6;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    direction: rtl;
}
.steps-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-top: 1.5rem;
    direction: rtl;
}
.step-box {
    background: linear-gradient(135deg, #f3e8ff 0%, #faf5ff 100%);
    border-radius: 12px;
    padding: 1.5rem 1rem;
    text-align: center;
    border: 1px solid #e9d5ff;
    direction: rtl;
}
.step-number {
    font-size: 2rem;
    font-weight: 700;
    color: #7c3aed;
    margin-bottom: 0.5rem;
}
.step-text {
    font-size: 0.9rem;
    color: #5b21b6;
    line-height: 1.5;
    font-weight: 500;
}

/* Why not ChatGPT section */
.why-not-section {
    background: #fef3c7;
    border-radius: 14px;
    padding: 1.8rem 2rem;
    margin-bottom: 2rem;
    border-right: 5px solid #f59e0b;
    direction: rtl;
}
.why-not-section h4 {
    color: #92400e;
    margin: 0 0 1rem 0;
    font-size: 1.1rem;
    font-weight: 700;
    direction: rtl;
    text-align: right;
}
.why-item {
    color: #78350f;
    font-size: 0.93rem;
    margin: 0.6rem 0;
    padding-right: 1.5rem;
    direction: rtl;
    text-align: right;
}

/* Limitations section */
.limitations-section {
    background: #fee2e2;
    border-radius: 14px;
    padding: 1.8rem 2rem;
    margin: 2rem 0;
    border-right: 5px solid #dc2626;
    direction: rtl;
}
.limitations-section h4 {
    color: #7f1d1d;
    margin: 0 0 1rem 0;
    font-size: 1.1rem;
    font-weight: 700;
    direction: rtl;
    text-align: right;
}
.limit-item {
    color: #7f1d1d;
    font-size: 0.92rem;
    margin: 0.5rem 0;
    padding-right: 1.5rem;
    direction: rtl;
    text-align: right;
}

/* Test result rows */
.result-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.8rem 0;
    border-bottom: 1px solid #f1f5f9;
    direction: rtl;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.result-row:last-child { border-bottom: none; }
.test-name  { font-weight: 600; color: #374151; min-width: 140px; text-align: right; }
.test-value { font-size: 1.05rem; font-weight: 700; }
.test-range { font-size: 0.82rem; color: #6b7280; text-align: right; }

.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
}
.badge-normal   { background: #dcfce7; color: #166534; }
.badge-borderline { background: #fef3c3; color: #92400e; }
.badge-abnormal { background: #fee2e2; color: #991b1b; }

/* Category badges */
.category-normal { background: #d1fae5; color: #065f46; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.82rem; font-weight: 600; }
.category-borderline { background: #fef9e7; color: #78350f; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.82rem; font-weight: 600; }
.category-abnormal { background: #fee2e2; color: #991b1b; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.82rem; font-weight: 600; }

/* Explanation bullets */
.explanation-item {
    background: #f8fafc;
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.7rem;
    border-right: 3px solid #2563eb;
    direction: rtl;
    font-size: 0.93rem;
    line-height: 1.6;
    color: #374151;
    text-align: right;
}

/* Question bullets */
.question-item {
    background: #f0fdf4;
    border-radius: 10px;
    padding: 0.85rem 1.2rem;
    margin-bottom: 0.6rem;
    border-right: 3px solid #16a34a;
    direction: rtl;
    font-size: 0.92rem;
    color: #14532d;
    text-align: right;
}

/* Reassuring result */
.reassuring-card {
    background: linear-gradient(135deg, #dcfce7 0%, #f0fdf4 100%);
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    border-right: 5px solid #16a34a;
    direction: rtl;
}
.reassuring-text {
    font-size: 1rem;
    color: #14532d;
    line-height: 1.7;
    font-weight: 500;
    text-align: right;
}

/* Disclaimer */
.disclaimer {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    direction: rtl;
    font-size: 0.88rem;
    color: #78350f;
    line-height: 1.7;
    text-align: right;
}

/* Sidebar patient cards */
.sidebar-patient {
    background: white;
    border-radius: 10px;
    padding: 0.85rem 1.2rem;
    margin-bottom: 0.6rem;
    cursor: pointer;
    direction: rtl;
    border: 2px solid transparent;
    transition: all 0.2s;
}
.sidebar-patient:hover { border-color: #2563eb; background: #f0f9ff; }

/* App title in sidebar */
.app-title {
    color: #1e3a5f;
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
    direction: rtl;
    text-align: right;
}
.app-subtitle {
    color: #64748b;
    font-size: 0.84rem;
    margin-bottom: 1.5rem;
    direction: rtl;
    text-align: right;
}

h1, h2, h3, h4, h5, h6 { direction: rtl; text-align: right; }
p, li, label, span, a { direction: rtl; }

/* Expander */
.streamlit-expanderHeader { direction: rtl; text-align: right; }
details > summary { direction: rtl; text-align: right; }

/* Responsive */
@media (max-width: 900px) {
    .steps-grid { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# ── Data ────────────────────────────────────────────────────────────────────────
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
            "WBC":        7.8,
            "Hemoglobin": 12.8,
            "Ferritin":   6.2,
            "HbA1c":      5.3,
            "LDL":        88.0,
        },
        "explanations": [
            "רמת הפריטין שלך נמוכה מהטווח המקובל. פריטין הוא חלבון שמאחסן ברזל בגוף – רמה נמוכה עשויה להצביע על מאגרי ברזל מדוללים.",
            "זה עשוי להתייחס לעייפות, חולשה, קוצר נשימה וקשיי ריכוז, תלוי בחומרה – אך יש צורך בהערכה קלינית מלאה.",
            "מחסור בברזל שכיח אצל נשים בגיל הפוריות. הרופא יוכל לקבוע את הסיבה ולהמליץ על צעדים הבאים.",
            "✅ ערכי ה-WBC, המוגלובין, HbA1c ו-LDL שלך בטווח תקין.",
        ],
        "questions": [
            "מה יכול להיות הגורם לנמוכות בפריטין שלי?",
            "האם יש צורך בבדיקות נוספות לברור הגורם?",
            "אילו אפשרויות טיפול עשויות להיות רלוונטיות?",
            "איזה תזונה עשויה להסייע בשיפור רמות הברזל?",
            "מתי מומלץ לחזור לבדיקת מעקב?",
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
            "ספירת תאי הדם הלבנים שלך גבוהה מהטווח הרגיל. תאי דם לבנים הם חלק ממערכת החיסון שלך.",
            "עלייה בספירה עשויה להיות תגובה לזיהום, דלקת, סטרס פיזי, או תוכן תרופות – אך יש צורך בהערכה רפואית לברור הגורם.",
            "ברוב המקרים מדובר בממצא שיכול להיות זמני ודורש מעקב – בדיקה חוזרת עשויה להיות מדווחת.",
            "✅ כל שאר הבדיקות – המוגלובין, פריטין, HbA1c ו-LDL – בטווח תקין.",
        ],
        "questions": [
            "מה יכול להיות הגורם לעלייה בתאי הדם הלבנים?",
            "האם יש צורך בבדיקות דם נוספות?",
            "כמה זמן עד לבדיקה חוזרת?",
            "האם יש תסמינים שעליי לשים לב אליהם?",
            "מה יוצע במקרה שהערך יישאר מוגבה בבדיקה החוזרת?",
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
            "רמת ה-HbA1c שלך (6.8%) גבוהה מהטווח התקין. בדיקה זו משקפת את רמת הסוכר הממוצעת בדם בשלושת החודשים האחרונים.",
            "ערך זה גבוה מהטווח התקין ודורש דיון עם הרופא לגבי משמעותו והמשך הבירור.",
            "רמת ה-LDL שלך (138 mg/dL) גם היא גבוהה מטווח היעד. הרופא יוכל להעריך את החשיבות בהקשר הקליני שלך.",
            "שני ממצאים אלה עשויים להצביע על הצורך בדיון עם הרופא על אפשרויות טיפול, כולל שינויי אורח חיים.",
            "✅ ה-WBC, המוגלובין והפריטין שלך בטווח תקין.",
        ],
        "questions": [
            "מה משמעות הערך הגבוה ב-HbA1c שלי?",
            "אילו צעדים מומלצים עבור ה-LDL הגבוה?",
            "מה אפשרויות השינוי בתזונה ובאורח חיים?",
            "האם טיפול תרופתי עשוי להיות נדרש?",
            "מתי לחזור לבדיקת מעקב?",
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
            "רמת ההמוגלובין שלך נמוכה מהטווח התקין לנשים. המוגלובין הוא החלבון בתאי הדם האדומים שנושא חמצן לגוף.",
            "רמה נמוכה (אנמיה) עשויה להתייחס לעייפות, חולשה, סחרחורת ודפיקות לב, תלוי בחומרה – אך יש צורך בהערכה קלינית.",
            "הפריטין שלך נמוך גם הוא – זה עשוי לעזור לרופא בקביעת הגורם לאנמיה. בדיקות נוספות עשויות להיות מדווחות.",
            "✅ ה-WBC, HbA1c ו-LDL שלך בטווח תקין.",
        ],
        "questions": [
            "מה יכול להיות הגורם לאנמיה שלי?",
            "אילו בדיקות נוספות מומלצות?",
            "אילו אפשרויות טיפול עשויות להיות רלוונטיות?",
            "איזה מזונות מומלצים לשיפור ההמוגלובין?",
            "כמה זמן עד לתוצאות טיפול?",
        ],
    },
    {
        "id": 5,
        "name": "נעמי ישראלי",
        "age": 28,
        "gender": "נקבה",
        "scenario": "ערכים גבוליים",
        "icon": "⚖️",
        "results": {
            "WBC":        6.5,
            "Hemoglobin": 11.8,
            "Ferritin":   18.5,
            "HbA1c":      5.6,
            "LDL":        102.0,
        },
        "explanations": [
            "לרוב הערכים שלך ממצאים שנמצאים בקצה התחתי או העליון של הטווח התקין – אלו נחשבים ערכים גבוליים.",
            "המוגלובין שלך (11.8) קרוב לטווח הנמוך. פריטין (18.5) גם הוא בקצה התחתי. הרופא עשוי לשקול מעקב.",
            "HbA1c (5.6) ו-LDL (102) מעט מעל היעד המקובל – ערכים גבוליים הדורשים מעקב.",
            "מומלץ לחזור לבדיקה תוך 2-3 חודשים כדי לעקוב אחר המגמות ולהסתייע בהחלטות מניעה.",
        ],
        "questions": [
            "מה משמעות הערכים הגבוליים שלי?",
            "אילו צעדים מוקדמים אוכל/אוכלת לנקוט למניעה?",
            "איזה שינויים בתזונה ואורח חיים עשויים להיות מועילים?",
            "כמה זמן עד לבדיקה חוזרת?",
            "האם יש צורך בטיפול בשלב זה?",
        ],
    },
    {
        "id": 6,
        "name": "אור דניאלי",
        "age": 38,
        "gender": "זכר",
        "scenario": "כל הערכים תקינים",
        "icon": "✅",
        "results": {
            "WBC":        7.1,
            "Hemoglobin": 14.5,
            "Ferritin":   95.0,
            "HbA1c":      4.9,
            "LDL":        82.0,
        },
        "explanations": [
            "כל הערכים המעבדתיים שלך נמצאים בטווח התקין.",
            "יש להמשיך במעקב רפואי שגרתי בהתאם להמלצת הרופא המטפל.",
        ],
        "questions": [
            "מה הנקודות החיוביות בבדיקות שלי?",
            "כיצד אוכל/אוכלת להמשיך בשגרה בריאה?",
            "מתי מומלץ לעשות בדיקה חוזרת?",
            "האם יש דברים ספציפיים שעלי להמשיך לעשות?",
            "מה מומלץ לשמירה על בריאות לטווח ארוך?",
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


def get_category(status):
    """Return Hebrew category name."""
    if status == "normal":
        return "תקין"
    elif status == "low":
        return "נמוך"
    else:
        return "גבוה"


def status_badge(status):
    if status == "normal":
        return '<span class="badge badge-normal">✓ תקין</span>'
    elif status == "low":
        return '<span class="badge badge-abnormal">▼ נמוך</span>'
    else:
        return '<span class="badge badge-abnormal">▲ גבוה</span>'


def value_color(status):
    if status == "normal":
        return "#16a34a"
    return "#dc2626"


def is_all_normal(patient):
    """Check if all results are normal."""
    return all(classify(k, v) == "normal" for k, v in patient["results"].items())


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="app-title">🧬 מערכת הסבר תוצאות דם</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">כלי AI להסבר בדיקות דם בשפה ידידותית למטופל</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**בחר/י תרחיש מטופל:**", )

    patient_names = [f"{p['icon']} {p['name']} – {p['scenario']}" for p in PATIENTS]
    selected_idx = st.radio("", patient_names, label_visibility="collapsed")
    selected_patient = PATIENTS[patient_names.index(selected_idx)]

    st.markdown("---")
    st.markdown("""
<div style='font-size:0.78rem; color:#94a3b8; direction:rtl; line-height:1.6; text-align:right;'>
⚠️ <strong>כלי זה מיועד להמחשה בלבד.</strong><br>
כל הנתונים הם סינתטיים.<br>
אין להשתמש בו לצורכי אבחון או טיפול רפואי.
</div>
""", unsafe_allow_html=True)


# ── Main content ───────────────────────────────────────────────────────────────
p = selected_patient

# ── Intro section ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="intro-section">
    <h3>🩺 מערכת AI להסבר תוצאות בדיקות דם</h3>
    <p>
    המערכת מסבירה תוצאות בדיקות דם נפוצות בשפה פשוטה וקלה להבנה.
    </p>
    <p>
    המטרה היא להקטין חרדה ולשפר את התקשורת בין המטופל לרופא – לא להחליף ייעוץ רפואי.
    </p>
    <p>
    כלי זה אינו מחליף פגישה עם רופא ואינו מהווה אבחנה או המלצה על טיפול.
    </p>
</div>
""", unsafe_allow_html=True)

# ── How it works section ───────────────────────────────────────────────────────
st.markdown("""
<div class="how-it-works">
    <div class="section-title">❓ איך זה עובד?</div>
    <div class="steps-grid">
        <div class="step-box">
            <div class="step-number">1</div>
            <div class="step-text">תוצאות המעבדה מופיעות באפליקציית הקופה</div>
        </div>
        <div class="step-box">
            <div class="step-number">2</div>
            <div class="step-text">המערכת מזהה ערכים חריגים או גבוליים</div>
        </div>
        <div class="step-box">
            <div class="step-number">3</div>
            <div class="step-text">מתקבל הסבר בשפה פשוטה</div>
        </div>
        <div class="step-box">
            <div class="step-number">4</div>
            <div class="step-text">המטופל מקבל שאלות מומלצות לרופא</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Why not regular ChatGPT section ────────────────────────────────────────────
st.markdown("""
<div class="why-not-section">
    <h4>🔐 למה לא ChatGPT רגיל?</h4>
    <div class="why-item">
        • <strong>פרטיות:</strong> אין צורך להעתיק נתונים רפואיים רגישים לכלי חיצוני פומבי.
    </div>
    <div class="why-item">
        • <strong>זמינות:</strong> הנתונים כבר קיימים במערכת הקופה – אנחנו משתמשים בהם ישירות.
    </div>
    <div class="why-item">
        • <strong>בטיחות:</strong> ההסבר מוגבל לשפה בטוחה, לא-אבחנית.
    </div>
    <div class="why-item">
        • <strong>רופא בשליטה:</strong> הרופא המטפל הוא הסמכות הקלינית היחידה ואחראי על כל החלטה רפואית.
    </div>
</div>
""", unsafe_allow_html=True)

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
    <div style="display:flex; gap:1rem; flex-wrap:wrap; direction:rtl; justify-content:flex-end;">
        <span class="badge badge-normal">✓ {normal_count} תקינים</span>
        {f'<span class="badge badge-abnormal">⚠ {len(abnormal_tests)} חריגים</span>' if abnormal_tests else ''}
    </div>
    {'<p style="margin:0.6rem 0 0; font-size:0.87rem; color:#374151; text-align:right; direction:rtl;">ממצאים הדורשים תשומת לב: ' + '، '.join(abnormal_tests) + '</p>' if abnormal_tests else ''}
</div>
""", unsafe_allow_html=True)


# ── Right column: explanations + questions ────────────────────────────────────
with col2:
    if is_all_normal(p):
        st.markdown('<div class="section-title">✅ סיכום חיובי</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="reassuring-card">
    <div class="reassuring-text">
    ✨ כל הערכים שנבדקו נמצאים בטווח התקין. יש להמשיך במעקב רפואי שגרתי בהתאם להמלצת הרופא המטפל.
    </div>
</div>
""", unsafe_allow_html=True)
    else:
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


# ── Limitations section (full width) ───────────────────────────────────────────
st.markdown("""
<div class="limitations-section">
    <h4>⚖️ מגבלות המערכת</h4>
    <div class="limit-item">
        • <strong>אינה מספקת אבחנה:</strong> המערכת אינה יכולה לאבחן מחלה או בעיה רפואית.
    </div>
    <div class="limit-item">
        • <strong>אינה ממליצה על טיפול:</strong> כל החלטה טיפולית תתקבל רק על ידי הרופא.
    </div>
    <div class="limit-item">
        • <strong>אינה מתחשבת בהיסטוריה רפואית מלאה:</strong> המערכת אינה מתחשבת בהיסטוריה רפואית מלאה, תרופות קיימות, או הקשר קליני מלא.
    </div>
    <div class="limit-item">
        • <strong>הסקה בהקשר קליני:</strong> כל התוצאות צריכות להיות מפורשות בהקשר קליני מלא יחד עם הרופא המטפל.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Disclaimer (full width) ────────────────────────────────────────────────────
st.markdown("""
<div class="disclaimer">
    <strong>⚠️ כתב ויתור חשוב:</strong>
    המידע המוצג בכלי זה מיועד למטרות <strong>חינוכיות והמחשה בלבד</strong>, ואינו מהווה ייעוץ רפואי, אבחון, או המלצה תרופתית.
    כל הנתונים הם <strong>סינתטיים לחלוטין</strong> ואינם שייכים למטופלים אמיתיים.
    בכל שאלה רפואית יש לפנות לרופא/ה המטפל/ת.
    אין להסתמך על כלי זה לקבלת החלטות רפואיות מכל סוג שהוא.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; direction:rtl; color:#94a3b8; font-size:0.78rem; margin-top:2.5rem;">
    מערכת הסבר תוצאות דם – הוכחת היתכנות (PoC) | כל הנתונים סינתטיים | אינו מחליף ייעוץ רפואי
</div>
""", unsafe_allow_html=True)
```
