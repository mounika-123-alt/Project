def calculate_clv(pf, aov, lifespan):
    try:
        clv = pf * aov * lifespan

        if clv < 5000:
            insight = "Low value customer. Improve engagement and offers."
        elif clv < 20000:
            insight = "Moderate value customer. Focus on upselling."
        else:
            insight = "High value customer. Retain with loyalty programs."

        return clv, insight

    except Exception as e:
        return 0, f"Error: {str(e)}"