# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "e4b85d50-26cd-4a72-8fc7-7baea3cd64bd",
# META       "default_lakehouse_name": "lakehouse_da",
# META       "default_lakehouse_workspace_id": "6a9ddf8c-c2db-4770-b750-e6a34e2c1ef2",
# META       "known_lakehouses": [
# META         {
# META           "id": "e4b85d50-26cd-4a72-8fc7-7baea3cd64bd"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC select * from his_reporting_patient.Patient limit 10

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
