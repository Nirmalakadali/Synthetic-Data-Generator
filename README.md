---
title: LLM Models
emoji: 🔥
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 5.4.0
app_file: app.py
pinned: false
---

### 🤔 What is it?
The Synthetic Data Generator allows users to input a prompt describing the type of data they want, and in return, it generates a CSV file containing the synthetic data. This can be incredibly useful for various applications, such as testing algorithms, training models,  beginner practice, or even prototyping new ideas without needing real datasets.

### Key Features
- User-Friendly Interface: Built with Gradio, the interface is simple and intuitive. Users can easily enter their data requirements and download the generated CSV.
- Generative AI Integration: By integrating with Google’s Generative AI , the model can understand prompts and create relevant data in a structured format.

### How It Works
- Prompt Input: Users enter a prompt describing the desired data.
- Data Generation: The model processes the prompt and generates synthetic data using AI.
- CSV Output: The generated data is saved as a CSV file, ready for download.

### Here are the few prompts i tried:
1. Generate a dataset of 300 patients with features: patient_id, age, gender, diagnosis, and treatment
2. Create a dataset of 200 transactions with the following fields: transaction_id, customer_id, transaction_date, amount, and category
3. Generate a dataset of 100 customers with the following features: customer_id, age, gender, income, and purchase_amount
4. Create a dataset of product reviews with review_id, product_id, user_id, rating, and review_text
5. Generate a dataset of sales data for a retail store with features: sale_id, item_name, quantity_sold, sale_price, and sale_date
