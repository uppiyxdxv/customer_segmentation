# Customer Segmentation (K-Means) — Flask App

A **web-based Customer Segmentation tool** built with **Flask** and **K-Means clustering** to group customers based on their characteristics and behavior.  
Upload your own dataset or use the built-in sample data, choose the number of clusters, visualize the results, and download the labeled dataset.

---

## 🚀 Features
- 📂 Upload CSV or use sample dataset
- 🔍 Auto-detects numeric features (e.g., Age, Income, Spending Score)
- 🛠 Handles missing values (median imputation) and scales features
- 🎯 Choose **K** manually or auto-select using **Silhouette Score**
- 📊 Displays:
  - Cluster metrics (K used, inertia, silhouette score)
  - Cluster sizes
  - 2D PCA visualization of clusters
  - Preview table of labeled data
- 💾 Download segmented dataset as CSV
- 🗄 Saves trained models and plots for reuse

---

## 🛠 Tech Stack
- **Backend:** Python, Flask
- **ML & Data Processing:** scikit-learn, pandas, numpy, matplotlib
- **Frontend:** Bootstrap 5, HTML, CSS

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository.



##PROJECT STRUCTURE 
customer-segmentation/
├── app.py                # Flask application
├── utils.py              # Helper functions (data processing, clustering, plotting)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── data/                 # Sample data (auto-generated if not present)
├── uploads/              # Uploaded CSV files
├── results/              # Clustered CSV outputs
├── models/               # Saved K-Means pipelines
├── static/
│   ├── style.css         # Custom styling
│   └── plots/            # Cluster visualization images
└── templates/
    ├── base.html         # Main layout
    ├── index.html        # Upload & input page
    └── results.html      # Results display page
