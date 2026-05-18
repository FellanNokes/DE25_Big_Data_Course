# Databricks notebook source
# MAGIC %md
# MAGIC # EDA on supply chain

# COMMAND ----------

VOLUME_PATH = "/Volumes/supply_chain/default/raw"

spark.sql(f"LIST '{VOLUME_PATH}'").display()

# COMMAND ----------

spark.sql(f"LIST '{VOLUME_PATH}/data'").display()
spark.sql(f"LIST '{VOLUME_PATH}/logs'").display()
spark.sql(f"LIST '{VOLUME_PATH}/metadata'").display()

# COMMAND ----------

df = spark.sql("SELECT * FROM supply_chain.bronze.raw_supply_chain")

df.display()

# COMMAND ----------

df_amount_order_status = spark.sql("""
                                   SELECT
                                       COUNT(*) AS amount,
                                       Order_Status
                                   FROM supply_chain.bronze.raw_supply_chain
                                   GROUP BY Order_Status
                                   """)

display(df_amount_order_status)

# COMMAND ----------

df_amount_order_status.plot(kind='bar', x='Order_Status', y='amount')
