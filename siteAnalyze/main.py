"""
Site Data Analysis
@author: Francisco P. Guimarães
@since: 2023-10-02
"""
import pandas as pd

# Read exel and filter (year = 2023)
siteList = pd.read_excel('data/SiteList.xlsx')
results = pd.read_excel('data/Results.xlsx')
siteList2023 = siteList[siteList['Year'] == 2023]
results2023 = results[results['Year'] == 2023]

# Joining tables
report = pd.merge(siteList2023, results2023, how='inner')
report = report[['Site Name', 'Site ID', 'State', 'Equipment', 'Signal (%)', 'Quality (0-10)', 'Mbps']]
report = report.sort_values(by='State')

# Create excel with final report
report.to_excel('data/report.xlsx', index=False)
print("Report: \n" + report + "\n")

# Sites with alerts
alert = results[results['Alerts'] == 'Yes']
alert = alert[['Site ID', 'Site Name', 'Alerts']]
print("Sites with Alerts: \n" + alert + "\n")

# Sites with quality = 0
quality = results[results['Quality (0-10)'] == 0]
quality = quality[['Site ID', 'Site Name', 'Quality (0-10)']]
print("Sites with quality = 0: \n" + quality + "\n")

# Sites with Mbps > 80
HightSpeed = results[results['Mbps'] > 80]
HightSpeed = HightSpeed[['Site ID', 'Site Name', 'Mbps']]
print("Sites with Mbps > 80: \n" + HightSpeed + "\n")

# Sites with Mbps < 10
LowSpeed = results[results['Mbps'] < 10]
LowSpeed = LowSpeed[['Site ID', 'Site Name', 'Mbps']]
print("Sites with Mbps < 10: \n" + LowSpeed + "\n")

# Missing Sites
missingSites = pd.merge(results, siteList, how='left', indicator=True)
missingSites = missingSites[missingSites['_merge'] == 'left_only']
missingSites = missingSites.drop(columns=['_merge'])
missingSites = missingSites[['Site ID', 'Site Name']]
print("Missing Sites: \n" + missingSites + "\n")
