PENSION_HEB_TO_ENG = {
    "אג\"ח קונצרני": "Corporate Bond",
    "אופציות": "Option",
    "ארץ": "Country",
    "אתר": "Web",
    "גוף מוסדי": "Institutional body",
    "דירוג": "Rating",
    "הלוואות": "Loans",
    "הצמדה": "Protected",
    "השקעה בחברות מוחזקות": "Investee Companies",
    "השקעות אחרות": "Other Investments",
    "זכויות מקרקעין": "Real Estate",
    "חברות": "Commercial Country",
    "חוזים עתידיים": "Future",
    "יעודיות": "Designated Bond",
    "כתבי אופציה": "Warrant",
    "כתובת הנכס": "Real Estate address",
    "מוצרים מובנים": "Structured",
    "מזומנים": "Cash",
    "מח\"מ": "Duration",
    "ממשלה": "Government Bond",
    "מניות": "Stock",
    "מספר מנפיק": "Issuer Nunber",
    "מספר ני\"ע": "Instrument Number",
    "מספר קרן": "Fund Number",
    "נדלן": "Real Estate Type",
    "נכס בסיס": "Underlying",
    "סוג הלוואה": "Loan Type",
    "סוג מוצר": "Structured Type",
    "סוג מטבע": "Currency",
    "סוג נגזר": "Derivative Type",
    "סוג קרן": "Investmnet Fund Type",
    "סחירות": "Tradable",
    "ענף פעילות": "Industry",
    "ערך נקוב": "Nominal Value",
    "פקדונות מעל 3 חודשים": "Deposits",
    "קונסורציום כן/לא": "Consortium",
    "קרנות השקעה": "Private Equity",
    "שווי הוגן": "Fair Value",
    "שווי שוק": "Market Value",
    "שייך למדד": "Index",
    "שיעור ריבית": "Rate",
    "שם המדרג": "Rating Agencies",
    "שם המנפיק/שם נייר ערך": "Instrument Name",
    "שם מנפיק": "Issuer Mane",
    "שם קרן": "Fund Nane",
    "שעור מנכסי אפיק ההשקעה": "Rate of Instrument Type",
    "שעור מסך נכסי השקעה": "Rafe of Funde Holding",
    "שעור מערך נקוב מונפק": "Rafe of Register",
    "שער": "Price",
    "תעודות השתתפות בקרנות נאמנות": "Mutual Fund",
    "תעודות התחייבות ממשלתיות": "Government Bond",
    "תעודות חוב מסחריות": "Commercial Debt",
    "תעודות סל": "ETF",
    "תשואה לפידיון": "yield",

    # Custom translations.
    "תאריך הדיווח": "Date",
    "החברה המדווחת": "Publishing body",
    "שם מסלול/קרן/קופה": "Track name",
    "מספר מסלול/קרן/קופה": "Track number",
    "1.ד. הלוואות": "1.d loans",
    "1.ה. פקדונות מעל 3 חודשים": "1.h deposites",
    "1. ו. זכויות במקרקעין": "1. mekarkein",
    "1. ז. השקעה בחברות מוחזקות": "1.z investments",
    "1. ט. יתרות התחייבות להשקעה": "1.t plus",
}


def translate_from_hebrew(word):
    if word in PENSION_HEB_TO_ENG:
        return PENSION_HEB_TO_ENG[word]