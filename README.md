# Financial-Transaction-Fraud-Detection-on-AWS
Machine learning fraud detection pipeline built on AWS to classify high-risk financial transactions using behavioral feature engineering, Gradient Boosting models, and real-time inference architecture with SageMaker, Lambda, and API Gateway.

📖 Project Description

Financial fraud detection is a critical challenge for banks and digital payment platforms due to the large volume of real-time transactions processed daily. Undetected fraudulent activity can lead to significant financial losses, regulatory risks, and reduced customer trust.

This project focuses on designing and implementing a scalable machine learning pipeline for financial transaction fraud detection using behavioral and transactional risk indicators. The solution leverages cloud-native machine learning workflows on Amazon Web Services (AWS) to perform data ingestion, exploratory analysis, feature engineering, predictive modeling, and real-time inference deployment.

The objective of this system is to develop a robust classification model capable of identifying high-risk fraudulent transactions and supporting data-driven decision intelligence for financial risk monitoring scenarios.
🎯 Business Objective

Modern financial institutions require intelligent predictive analytics systems to:

Detect suspicious transaction patterns in real time

Reduce financial losses due to fraudulent activity

Improve operational risk management

Support automated fraud investigation workflows

Enhance trust and security in digital financial ecosystems

This project demonstrates how machine learning models can be integrated into a production-style cloud architecture to enable scalable and low-latency fraud risk scoring.
📊 Dataset

Dataset Used: IEEE-CIS Financial Transaction Fraud Detection Dataset

Dataset Characteristics:

Large-scale anonymized financial transaction records

Contains behavioral transaction signals and engineered risk indicators

Highly imbalanced fraud classification problem

Use Case: Supervised learning based fraud classification

⚙️ Technology Stack

Programming Language: Python

Machine Learning Algorithms:

Logistic Regression

Random Forest

Gradient Boosting (XGBoost – final selected model)

Cloud Platform: Amazon Web Services (AWS)

Amazon S3 – data storage

Amazon SageMaker Studio – model experimentation

AWS Lambda – serverless inference

Amazon API Gateway – real-time scoring endpoint

Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

🧠 Machine Learning Methodology

The fraud detection pipeline was implemented using a structured modeling workflow:

1. Data Ingestion

Raw transaction datasets were uploaded to Amazon S3 and accessed through SageMaker notebooks for scalable cloud-based experimentation.

2. Exploratory Data Analysis

Distribution analysis of fraud vs non-fraud transactions

Missing value assessment

Temporal behavioral pattern analysis

Feature correlation inspection

3. Feature Engineering

Behavioral fraud indicators were derived including:

Transaction velocity features

Device switching frequency

Spending deviation signals

Transaction time-based risk patterns

Aggregated behavioral activity features

4. Model Development

Multiple supervised classification models were trained and compared:

Logistic Regression baseline model

Random Forest ensemble model

Gradient Boosting model (final selected architecture)

Model selection was based on predictive stability and fraud detection capability.

5. Model Evaluation

The primary evaluation metric used was ROC-AUC score to measure classification performance under imbalanced data conditions.

📈 Results

Final Selected Model: Gradient Boosting (XGBoost)

Validation Performance:

ROC-AUC Score: 0.91

The model demonstrated strong capability in identifying high-risk transaction patterns and reducing false-negative fraud classifications.

☁️ Cloud Deployment Architecture

The fraud detection workflow follows a simplified production-style architecture:

Transaction data stored in Amazon S3

Model training and experimentation performed in Amazon SageMaker Studio

Trained model deployed as a serverless inference function using AWS Lambda

Real-time scoring enabled via Amazon API Gateway endpoint

This architecture supports scalable fraud risk prediction suitable for real-world financial monitoring environments.
