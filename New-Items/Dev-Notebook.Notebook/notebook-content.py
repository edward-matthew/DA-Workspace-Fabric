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
# META           "id": "7f4564b6-6308-468b-834b-6c9b1ce47cb5"
# META         },
# META         {
# META           "id": "e4b85d50-26cd-4a72-8fc7-7baea3cd64bd"
# META         },
# META         {
# META           "id": "a7caf98a-87d9-4b80-8672-a8b780e22d99"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# config dlu

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC select * from his_reporting_patient.PatientOrganization po
# MAGIC inner join PROD_WS_BS_HIS.SILVER_LH_HIS_HIS.System.Organization o
# MAGIC     on o.OrganizationId = po.OrganizationId
# MAGIC limit 10

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC select * from his_reporting_patient.PatientOrganization po limit 5

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
