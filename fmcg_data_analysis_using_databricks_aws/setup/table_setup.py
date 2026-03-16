# Databricks notebook source
# MAGIC %sql
# MAGIC Create catalog if not exists fmcg;
# MAGIC use catalog fmcg;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA if not EXISTS fmcg_bronze;
# MAGIC CREATE SCHEMA if not EXISTS fmcg_silver;
# MAGIC CREATE SCHEMA if not EXISTS fmcg_gold;

# COMMAND ----------

# MAGIC %sql 
# MAGIC select count(*) from fmcg.fmcg_gold.fact_orders;

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC