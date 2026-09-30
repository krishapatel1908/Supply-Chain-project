create database supply_chain;
use supply_chain;

SELECT * FROM supply_chain_data
LIMIT 10;

select `product type`,sku, `stock levels`
from supply_chain_data
order by `stock levels` asc
limit 10; 


select `Product type`,`Order quantities`
from supply_chain_data
order by `Order Quantities` desc
limit 10;


SELECT 
    `Supplier name`,
    AVG(`Defect rates`) AS avg_defect_rate,
    AVG(`Manufacturing costs`) AS avg_manufacturing_cost
FROM supply_chain_data
GROUP BY `Supplier name`
HAVING AVG(`Defect rates`) > 2
   AND AVG(`Manufacturing costs`) > 40;
   
   
SELECT 
   `product type`,
   `stock levels`,
    CASE
      WHEN `stock levels` > 75 THEN "high"
	  WHEN `stock levels` BETWEEN 51 and 75 THEN "medium" 
      ELSE "low"
   END AS stock_category
FROM supply_chain_data;


select 
     `product type`,
     `revenue generated`
from supply_chain_data
where `revenue generated` > (
select avg(`revenue generated`)
from supply_chain_data
);


select 
    `transportation modes`,
    avg('costs') as avg_transport_cost
from supply_chain_data
group by `transportation modes`;


SELECT
    `Supplier name`,
    AVG(`Manufacturing costs`) AS avg_manufacturing_cost,
    RANK() OVER (
        ORDER BY AVG(`Manufacturing costs`) DESC
    ) AS supplier_rank
FROM supply_chain_data
GROUP BY `Supplier name`;


select `product type`,`revenue generated`,`defect rates`
from supply_chain_data
where `revenue generated`> 8000
and `defect rates`>4;

select 
       `supplier name`,
       avg(`lead time`) as avg_lead_time,
       avg(`defect rates`) as avg_defect_rates,
       avg(`manufacturing costs`) as avg_manufacturing_costs
from supply_chain_data
group by `supplier name`;
       

SELECT
     `supplier name`,
     AVG(`defect rates`) as avg_defect_rates,
 CASE
      WHEN AVG(`defect rates`) < 2 THEN 'best'
	  WHEN AVG(`defect rates`) BETWEEN 2 AND 2.5  THEN 'average'
	  ELSE 'risky'
      END AS supplier_category
FROM supply_chain_data
GROUP BY `supplier name`;