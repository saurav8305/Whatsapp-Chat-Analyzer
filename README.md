# 📊 WhatsApp Chat Analyzer

A powerful WhatsApp Chat Analysis application built using **Python, Pandas, Streamlit, NLP, and Data Visualization libraries**. This project provides deep insights into WhatsApp conversations through interactive statistics, visualizations, emoji analysis, activity trends, word clouds, and more.

---

## 🚀 Features

### 📈 Chat Statistics

* Total Messages
* Total Words
* Media Shared Count
* Links Shared Count

### 👥 User Analysis

* Most Active Users
* User-wise Message Statistics
* Individual Participant Analysis

### ☁️ Word Cloud

* Generate Word Clouds from chat messages
* Stop-word filtering support
* Hinglish stop-word removal

### 🔤 Most Common Words

* Top frequently used words
* Interactive visualizations

### 😂 Emoji Analysis

* Most Used Emojis
* Emoji Distribution Pie Chart
* Emoji Frequency Statistics

### 📅 Timeline Analysis

* Monthly Timeline
* Daily Timeline
* Activity Trends Over Time

### 🗓️ Activity Mapping

* Most Active Days
* Most Active Months
* Weekly Activity Heatmap
* Hourly Activity Analysis

### 🔗 URL Detection

* Detect and count links shared in conversations

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend / Data Processing

* Python
* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn
* Plotly

### NLP & Text Processing

* WordCloud
* Emoji
* URLExtract
* Regular Expressions (Regex)

---

## 📂 Project Structure

```text
Whatsapp-Chat-Analyzer/
│
├── app.py
├── helper.py
├── preprocessor.py
├── stop_hinglish.txt
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Whatsapp-Chat-Analyzer.git

cd Whatsapp-Chat-Analyzer
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will start at:

```text
http://localhost:8501
```

---

## 📱 How to Export WhatsApp Chat

1. Open WhatsApp.
2. Open any chat/group.
3. Click **More Options (⋮)**.
4. Select **Export Chat**.
5. Choose **Without Media**.
6. Upload the exported `.txt` file into the application.

---

## 📊 Supported WhatsApp Formats

### 24-Hour Format

```text
31/07/2019, 19:16 - User: Message
```

### 12-Hour Format

```text
21/08/23, 11:11 am - User: Message
```

Both formats are automatically parsed and processed.

---

## 🔍 Analytics Included

* Message Count Analysis
* Word Frequency Analysis
* User Participation Analysis
* Monthly Activity Trends
* Daily Activity Trends
* Weekly Heatmaps
* Emoji Analytics
* URL Analytics
* Word Cloud Visualization

---

## 📸 Screenshots

### Dashboard

(Add Screenshot Here)

### Word Cloud

(Add Screenshot Here)

### Emoji Analysis

(Add Screenshot Here)

### Weekly Activity Heatmap

(Add Screenshot Here)

---

## 🎯 Future Improvements

* Sentiment Analysis
* Conversation Starter Analysis
* Response Time Analysis
* Message Prediction
* AI-Powered Chat Summarization
* Topic Modeling
* Export Reports as PDF
* Multi-language Support
* Advanced NLP Insights

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Saurav**

Software Developer | Machine Learning Enthusiast

GitHub: https://github.com/saurav8305
