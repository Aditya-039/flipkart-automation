# Flipkart Payment-Flow Automation

Automates an end-to-end Flipkart purchase journey up to the OTP/“Order Pending” confirmation page using Selenium, pytest, and the Page Object Model.

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Setup](#setup)  
- [Generate Login Cookies](#generate-login-cookies)  
- [Run the Tests](#run-the-tests)  
- [Demo Recording](#demo-recording)  
- [Project Structure](#project-structure)  
- [Next Steps](#next-steps)  

---

## Features

- Bypasses Flipkart login via saved cookies  
- Adds a product to cart (handles “Add to Cart” vs. “Go to Cart”)  
- Clicks through Order Summary, pop-ups, and default address confirmation  
- Fills Credit/Debit card + billing details (pincode, country, city, state, address)  
- Lands on the OTP entry or “Order Pending” confirmation  

---

## Prerequisites

- **Python 3.8+**  
- **Git**  
- **Google Chrome**  
- **Windows / macOS / Linux** (with ChromeDriver managed automatically)  
- *(Optional)* NVIDIA ShadowPlay or another screen-recorder for demo capture  

---

## Setup

1. **Clone the repo**  
   ```bash
   git clone git@github.com:Aditya-039/flipkart-automation.git
   cd flipkart-automation
2. **Create and Activate a virtual enviorment**
    python3 -m venv venv
    # macOS/Linux
    source venv/bin/activate  
    # Windows (CMD)
    venv\Scripts\activate
3. **Install Dependencies**
    pip install --upgrade pip
    pip install -r requirements.txt
