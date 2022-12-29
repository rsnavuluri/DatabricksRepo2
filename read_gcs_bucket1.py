# Databricks notebook source
bucket_name = "niaan-bucket-3"
mount_name = "/mnt/niaan-bucket-3"
dbutils.fs.mount(f"gs://{bucket_name}", f"/mnt/{mount_name}")
display(dbutils.fs.ls("/mnt/{mount_name}"))
