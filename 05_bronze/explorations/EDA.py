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
