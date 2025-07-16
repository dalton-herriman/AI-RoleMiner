# ML-RoleMiner
# 🛡️ RoleMiner: ML-based Role Mining from User-Permission Data

This project uses synthetic RBAC data to train a machine learning model that predicts user roles based on their permission assignments. It's ideal for experimenting with role mining and identity governance automation.

---

## 📁 Project Structure
```plaintext
├── data/
│ └── raw/
│ ├── permissions.json
│ ├── roles.json
│ ├── user_roles.json
│ └── user_permissions.json
├── notebooks/
│ └── role_mining.ipynb
├── scripts/
│ └── generate_data.py
└── README.md
```

---

---

## 🧪 Features

- ✅ Synthetic RBAC data generation (users, permissions, roles)
- ✅ Multi-label supervised ML model to predict user roles
- ✅ Exploratory visualizations (role distribution, prediction analysis)
- ✅ Extendable for unsupervised clustering-based role mining

---

## 🔧 Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/roleminer.git
cd roleminer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📊 Usage
