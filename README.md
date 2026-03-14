# StudentAnalytics-FullStack 📊

A full-stack data management and visualization suite that tracks student academic progress. The application features a **Flask REST API** backend powered by **Pandas** for data manipulation and a **React** frontend for real-time interactivity and graphical insights.

---

## 🚀 The Solution
This project automates the tracking of student performance across multiple examination cycles (PA1 through Models). It allows educators to:
* **Perform CRUD Operations:** Add, update, and delete student records dynamically.
* **Persistent Storage:** Synchronizes in-memory data with a CSV-based "database" using Pandas.
* **Automated Visualization:** Generates time-series progress plots on-demand via Matplotlib and serves them as dynamic assets to the frontend.

---

## 🛠️ Tech Stack

### **Backend (Data Science & API)**
* **Flask:** RESTful API routing and CORS handling.
* **Pandas:** Dataframe manipulation, CSV serialization, and state management.
* **Matplotlib:** Server-side rendering of performance graphs.
* **NumPy:** Numerical data handling for progress tracking.

### **Frontend (Interactive UI)**
* **React.js:** Functional components with `useEffect` and `useState` for state synchronization.
* **Axios:** Asynchronous API communication and Blob handling for image rendering.
* **Modern CSS:** Responsive input fields and dynamic action buttons.

---

## 🏗️ System Architecture



1.  **Request Layer:** React sends JSON payloads (Student objects) or GET requests to the Flask server.
2.  **Logic Layer:** Flask routes the request. For data changes, **Pandas** updates the central DataFrame and flushes it to `students_progress.csv`.
3.  **Visualization Engine:** The `/api/progress` endpoint triggers **Matplotlib** to generate a `.png` plot. 
4.  **Response Layer:** The server sends back updated JSON or a binary Image Blob, which React renders as a URL object.

---

## 🧬 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/students` | Retrieves the full list of student records. |
| `POST` | `/api/students` | Appends a new student to the dataset. |
| `POST` | `/api/update` | Bulk updates existing records and recalculates progress. |
| `POST` | `/api/delete_user` | Removes a student record by `reg_id`. |
| `GET` | `/api/progress` | Generates and returns a PNG plot of class-wide progress. |

---

## ⚙️ Installation & Usage

### 1. Backend Setup
```bash
# Navigate to backend folder
pip install flask flask-cors pandas matplotlib
python app.py

# Navigate to frontend folder
npm install axios
npm start

## ⌨️ Project-2: CLI Interactive Management System

Located in the `/project-2` directory is a standalone, text-based interactive system designed for high-efficiency data entry and management without the overhead of a GUI.

### **Features:**
* **Interactive Command Loop:** A persistent terminal interface that processes user commands in real-time.
* **Streamlined CRUD:** Optimized for rapid student data manipulation and registration via CLI prompts.
* **Direct Data Interaction:** Directly interfaces with the Pandas backend to perform complex filtering and data viewing within the terminal.
* **Low-Latency Performance:** Ideal for environments where a full web stack is not required.
