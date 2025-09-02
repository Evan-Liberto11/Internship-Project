# 📊 Internship Project – Service Project Labor Rate Automation

This project automates **service project labor rate lookups** using Tableau data. It was developed during an internship to improve efficiency and eliminate manual lookup processes.

## 🚀 Features
- 🔎 **Automated Labor Rate Lookup** – Query and fetch labor rates directly from Tableau data sources.
- 📂 **Data Integration** – Uses mock CSV and YAML role definitions for testing and extensibility.
- 🐍 **Python Application** – Modular code structure with an `app/` package.
- 🛠️ **Containerized Development** – Includes Docker and DevContainer setup for consistent environments.
- 📑 **Script Utilities** – Helper scripts for dependency management and reproducible builds.

## 🗂️ Project Structure
```
Internship-Project-main/
├── app/
│   ├── __init__.py
│   ├── __main__.py            # Entry point
│   ├── ia_labor_rates.py      # Core automation logic
│   ├── location_uids.py       # Location ID handling
│   └── data/
│       ├── mock_csv_response.csv
│       └── roles.yml
├── requirements/
│   ├── requirements.in
│   └── requirements.txt
├── scripts/
│   └── copy_requirements.sh
├── .devcontainer/             # VS Code Dev Container
├── Dockerfile.dev             # Development Dockerfile
├── .dockerignore
├── .gitignore
├── LICENSE
└── README.md
```

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Internship-Project-main.git
   cd Internship-Project-main
   ```

2. **Set up a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements/requirements.txt
   ```

4. **Run the application**
   ```bash
   python -m app
   ```

## 🐳 Run with Docker
Build and run inside a containerized environment:
```bash
docker build -t internship-project -f Dockerfile.dev .
docker run -it internship-project
```

## 📖 Usage
- Modify `app/data/mock_csv_response.csv` for test inputs.
- Update role filters in `app/data/roles.yml`.
- Run with `python -m app` to test lookups.

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
