# App User Retention

This project analyzes user retention and engagement for a mobile app across different operating systems, age groups, and genders. The goal is to identify patterns in the user conversion stages, measure conversion rates, and provide actionable business recommendations to improve engagement and monetization.

## Key Questions Addressed:
- Which users are most likely to activate, trial, and purchase a paid plan?
- How does user behavior vary by Operating System, age, and gender?
- What strategies can improve retention and revenue?

## Tools & Technologies:
Python, Pandas, Matplotlib.
## Metrics Calculated
- Conversion percentages between funnel stages.
- Average app usage time.
- Segment-level engagement (Operating System, Age and Gender).


## Key Insights

- **Operating System:** 
- Android users downloaded 3x more than iOS users. 
- They show 100% activation and higher paid conversions which suggests users who downloaded the app actually activated it. 
- iOS users drop off after downloading (1/3 do not activate or use the app).

  [
](https://github.com/HillaryIkhais/Mobile-App-User-Retention./blob/main/Visualizations/User%20Retention%20Based%20On%20Operating%20System.png?raw=true)<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/105eb5c2-6342-4c36-88c3-e0e87e037975" />


- **Age Groups:** 
- Users aged 18-22 are the most engaged, with a higher percentage converting to the paid version. 
- Users from ages 23-32 show strong monetization potential.

  


- **Gender:** 
- Female users are the most engaged and convert better in early stages (download to activation to trial).
- Male users dominate paid users because of higher initial downloads and very high trial to paid conversion. 


- **App Usage Time:** 
- Paid users spend 4x longer than trial users which indicates high engagement and retention.


## Recommendations

1. **Marketing:** 
 - Marketing  budgets should focus more on android users for maximum ROI.
- Improve iOS onboarding to reduce drop offs.
- Focus more on users within the age group of 18-32. They show highest engagement and monetization potential.
- Consider targeting campaigns to middle age users to increase trial adoption.
   - Younger users might respond to social proof 
   - Older users might respond to value and utility.

2. **Gender Specific Strategy:** 

- Target females for engagement campaigns, this will help to improve quality of early stage conversions.

- Target males for revenue via in-app purchases and  capitalize on their higher trial to paid potential.

3. **Product & Retention:** 
 - Monetize trial users with targeted offers and call-to-action. 
 - Paid users already represent a core loyal base, consider loyalty rewards or premium features to keep them engaged. 

## Technical Approach
1. **Data Preprocessing:**
Grouped users by Operating Systems,  Age Group, and Gender.
2. **Metric Calculation:** Calculated unique user counts per conversion stage.
3. **Conversion Rates:** Computed conversion stage percentages and visualized trends.
4. **Engagement Analysis:** Calculated average app usage time per conversion stage.
