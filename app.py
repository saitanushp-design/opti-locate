import streamlit as st

# -----------------------
# Franchise Location Analyzer
# -----------------------

st.set_page_config(page_title="Franchise Location Analyzer", layout="wide")

st.title("🏬 Franchise Location Analyzer")
st.write("Enter a city/location to analyze its potential for setting up a new franchise.")

# User input
location = st.text_input("📍 Enter Location (e.g., Bangalore, Hyderabad, Chennai):")

# Expanded database with 10 locations
location_data = {
    "bangalore": {
        "avg_budget": "₹15–25 lakhs (depending on area)",
        "pros": [
            "High IT hub population with good spending power",
            "Strong demand for food, retail, and fitness businesses",
            "Young working-class demographic"
        ],
        "challenges": [
            "High rental costs in prime areas",
            "Heavy traffic can affect accessibility",
            "High competition in urban centers"
        ],
        "marketing": [
            "Leverage social media & tech events",
            "Offer student and corporate discounts",
            "Partner with food delivery and e-commerce platforms"
        ],
        "legal": [
            "Shop & Establishment Act registration",
            "GST registration",
            "Trade license from BBMP"
        ]
    },
    "hyderabad": {
        "avg_budget": "₹10–20 lakhs (depending on area)",
        "pros": [
            "Growing IT & pharma hub",
            "Lower rentals than Bangalore",
            "Good demand for food and educational franchises"
        ],
        "challenges": [
            "Emerging competition in urban pockets",
            "Seasonal business fluctuations"
        ],
        "marketing": [
            "Focus on student & family audiences",
            "Digital ads targeting tech employees",
            "Local event sponsorships"
        ],
        "legal": [
            "Trade license from GHMC",
            "GST registration",
            "Labour law compliance"
        ]
    },
    "chennai": {
        "avg_budget": "₹12–22 lakhs",
        "pros": [
            "Strong automobile & IT hub",
            "High literacy and education demand",
            "Cultural affinity for food & retail"
        ],
        "challenges": [
            "Monsoon floods affect businesses",
            "Competition in core areas like T Nagar"
        ],
        "marketing": [
            "Local language promotions",
            "Cinema-based advertising",
            "University tie-ups"
        ],
        "legal": [
            "Trade license from Chennai Corporation",
            "Shops & Establishments Act compliance",
            "Pollution board clearance (for food outlets)"
        ]
    },
    "delhi": {
        "avg_budget": "₹20–30 lakhs",
        "pros": [
            "Large cosmopolitan market",
            "High disposable income",
            "Strong retail & food culture"
        ],
        "challenges": [
            "High rentals in malls & Connaught Place",
            "Regulatory hurdles in licensing"
        ],
        "marketing": [
            "Social media + metro ads",
            "Influencer tie-ups",
            "Event sponsorships in colleges"
        ],
        "legal": [
            "MCD trade license",
            "Food Safety license (if applicable)",
            "GST registration"
        ]
    },
    "mumbai": {
        "avg_budget": "₹25–35 lakhs",
        "pros": [
            "India’s financial capital",
            "Diverse customer base",
            "High tourist influx"
        ],
        "challenges": [
            "Very high rentals in prime areas",
            "Fierce competition"
        ],
        "marketing": [
            "Local train & metro advertising",
            "Bollywood tie-ups",
            "High social media engagement"
        ],
        "legal": [
            "BMC trade license",
            "FSSAI license (if food-based)",
            "GST registration"
        ]
    },
    "pune": {
        "avg_budget": "₹10–18 lakhs",
        "pros": [
            "Student city with huge youth market",
            "Affordable rentals compared to metros",
            "Strong IT & education presence"
        ],
        "challenges": [
            "Seasonal demand variations",
            "Limited high-street exposure"
        ],
        "marketing": [
            "Campus marketing campaigns",
            "Student discounts",
            "Tech park tie-ups"
        ],
        "legal": [
            "PMC trade license",
            "GST registration",
            "Labour law compliance"
        ]
    },
    "kolkata": {
        "avg_budget": "₹8–15 lakhs",
        "pros": [
            "Affordable rentals",
            "Huge cultural & festival-driven demand",
            "Good scope for food & apparel businesses"
        ],
        "challenges": [
            "Lower disposable income compared to metros",
            "Slow adoption of luxury brands"
        ],
        "marketing": [
            "Festival-based promotions (Durga Puja)",
            "Local newspaper ads",
            "Community sponsorships"
        ],
        "legal": [
            "KMC trade license",
            "Shops & Establishments Act compliance",
            "GST registration"
        ]
    },
    "ahmedabad": {
        "avg_budget": "₹9–17 lakhs",
        "pros": [
            "Rapidly growing business hub",
            "Strong food culture",
            "Affordable rentals compared to metros"
        ],
        "challenges": [
            "Seasonal demand shifts",
            "Language barriers in promotions"
        ],
        "marketing": [
            "Local language ads",
            "Festival promotions (Navratri)",
            "Tie-ups with colleges"
        ],
        "legal": [
            "AMC trade license",
            "FSSAI license (if food-based)",
            "GST registration"
        ]
    },
    "jaipur": {
        "avg_budget": "₹7–12 lakhs",
        "pros": [
            "Tourism-driven market",
            "Affordable rentals",
            "Growing student population"
        ],
        "challenges": [
            "Seasonal tourist fluctuations",
            "Limited exposure outside city center"
        ],
        "marketing": [
            "Tourist-focused promotions",
            "Festival sponsorships",
            "Local fairs and exhibitions"
        ],
        "legal": [
            "JMC trade license",
            "GST registration",
            "Tourism-related compliance"
        ]
    },
    "coimbatore": {
        "avg_budget": "₹6–12 lakhs",
        "pros": [
            "Strong textile & educational hub",
            "Affordable rentals",
            "Good demand for food & retail"
        ],
        "challenges": [
            "Limited cosmopolitan exposure",
            "Seasonal business demand"
        ],
        "marketing": [
            "Local college tie-ups",
            "Print media ads",
            "Festival offers"
        ],
        "legal": [
            "CMC trade license",
            "GST registration",
            "Labour compliance"
        ]
    }
}

# Display info if location found
if location:
    loc_key = location.lower()
    if loc_key in location_data:
        data = location_data[loc_key]
        st.subheader(f"📊 Analysis for {location.title()}")

        st.metric("💰 Estimated Setup Budget", data["avg_budget"])

        st.write("### ✅ Advantages")
        for p in data["pros"]:
            st.write(f"- {p}")

        st.write("### ⚠️ Challenges")
        for c in data["challenges"]:
            st.write(f"- {c}")

        st.write("### 📢 Marketing Suggestions")
        for m in data["marketing"]:
            st.write(f"- {m}")

        st.write("### 📜 Legal & Regulatory Notes")
        for l in data["legal"]:
            st.write(f"- {l}")

    else:
        st.warning("❌ Sorry, location not found in database. Please try one of the 10 supported cities.")
