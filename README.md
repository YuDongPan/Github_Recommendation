# Github_Recommendation
## Introduction
This project is supported by the open source summer activity and the towhee community. It aims to design an efficient recommendation algorithm to recommend favorite projects for users.

![image](towhee.png)

## Development Progress
* **Data Collection**
* Baseline algorithm design
* ML algorithm design
* DL algorithm design
* Analysis and comparison

## Data Description
* The data field contains five fields, namely, the user name, the project name (full name), the number of stars and forks of the project, and whether the user has starred the project.The data is organized into CSV files as follows.

| user | project | star | fork | has_star |
| ---- | ---- | ---- |---- |---- |

* Based on different requirements, we provide three types of data for users to process:`data_demo`,`data_raw`,`data_clean`
    - `data_demo`:A small data set for users to do pre experiments,includes 505 users,274721 projects, 601027 records totally.
    - `data_raw`: Medium scale datasets for designing landing algorithms,includes 10654 users, 657347 projects, 2360861 records totally.
    - `data_clean`: Projects with no more than 3 stars are filtered in the `data_raw`, includes 10654 users, 128750 projects, 1749929 records totally.
