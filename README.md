@'
# Enterprise Customer Lifetime Value (CLV), Churn & Cohort Retention Suite

[![Tableau Public](https://img.shields.io/badge/Tableau%20Public-Live%20Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/rajashekar.chinthala/viz/EnterpriseCLVCohortRetentionSuite/Dashboard1)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Portfolio%20Site-222222?style=for-the-badge&logo=github&logoColor=white)](https://rajashekar098.github.io/Candy_Project/)
[![Credly](https://img.shields.io/badge/Credly-IBM%20Data%20Analytics-blue?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/3bc9a43a-1fef-495b-a336-b058f02bb37b/public_url)
[![EduBridge](https://img.shields.io/badge/EduBridge-Java%20Full%20Stack%20Certified-darkgreen?style=for-the-badge)](http://www.edubridgeindia.com/certificate-detail?enrollment_number=EBEON1023850952)

---

## 📌 Executive Summary
An enterprise analytics suite built upon **6,000 commercial retail transaction records** (`candy_shop_data.csv`). This project evaluates multi-channel customer retention across In-Store, Online Web, and On-Demand Delivery channels, isolates cohort attrition dynamics, and calculates Customer Lifetime Value (CLV) using custom Level of Detail (LOD) formulas in Tableau.

* **Live Interactive Tableau Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/rajashekar.chinthala/viz/EnterpriseCLVCohortRetentionSuite/Dashboard1)
* **Hosted Web Application:** [View on GitHub Pages](https://rajashekar098.github.io/Candy_Project/)

---

## 📊 Analytical Methodology & LOD Calculations

### 1. Cohort Analysis via Level of Detail (LOD)
Tracks monthly customer retention rates by pegging all transactions to each customer's first purchase month:
```tableau
// Customer First Order Date (Acquisition Cohort)
{ FIXED [Customer ID] : MIN([Order Date]) }