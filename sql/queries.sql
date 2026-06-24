-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Month

SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 4. Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 5. Top 5 Sharpe Ratio Funds

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- 6. Average Investment by Age Group

SELECT
    age_group,
    ROUND(AVG(amount_inr),2)
FROM fact_transactions
GROUP BY age_group;


-- 7. Transaction Type Distribution

SELECT
    transaction_type,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;


-- 8. KYC Status Distribution

SELECT
    kyc_status,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;


-- 9. AUM by Fund House

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;


-- 10. Fund Count by Category

SELECT
    category,
    COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;