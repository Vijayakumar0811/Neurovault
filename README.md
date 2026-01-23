
#  Brute Force Attack Detection System

###  Overview

This project detects brute force login attacks by monitoring repeated failed authentication attempts. It prevents unauthorized access by automatically blocking suspicious users or IPs. The system is designed with an **ML-ready architecture** for future enhancement.



###  How It Works

1. User attempts to log in
2. System tracks login attempts and time intervals
3. Rule-based logic detects suspicious behavior
4. User/IP is blocked after threshold is exceeded
5. All events are logged and shown in the admin dashboard



###  Machine Learning (Status)

* ML model is **designed and trained offline**
* Intended for advanced risk-based detection
* **Not connected to live demo**
* Live demo uses **rule-based detection**



### Future Scope

* Real-time ML-based risk scoring
* Detection of distributed brute force attacks
* Integration with MFA systems
* Suitable for banking, fintech, and enterprise applications



### Tech Stack

* Backend: Python, Django
* Frontend: HTML, CSS, JavaScript
* Database: SQLite
* Security Logic: Rule-based
* ML: Scikit-learn (offline)



###  Project Status

Working brute force detection
 Admin monitoring dashboard
 ML integration – future enhancement



 

