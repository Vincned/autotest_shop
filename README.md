Вот готовый `README.md`, адаптированный под твой проект на GitHub:

---

```markdown
# 🛒 Autotest Shop – UI Test Automation for saucedemo.com

This project is a UI automation test suite for [saucedemo.com](https://www.saucedemo.com/), built using **Python**, **Selenium WebDriver**, and **Pytest**.  
It uses the **Page Object Model (POM)** design pattern for clean and scalable test architecture.

## 📁 Project Structure

```

autotest\_shop/
├── pages/
│   ├── cart\_page.py             # Cart page logic
│   ├── inventory\_page.py        # Inventory/products page logic
│   └── login\_page\_v2.py         # Login page logic
├── tests/
│   └── test\_add\_to\_cart.py      # Main UI test scenario
├── conftest.py                  # Pytest fixture with WebDriver setup
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation

````

## ✅ Test Scenarios Covered

- ✅ Valid login with correct credentials
- ✅ Adding an item (Sauce Labs Backpack) to cart
- ✅ Verifying the item count badge on the cart
- ✅ Navigating to the cart and checking product presence
- ✅ Removing the item from the cart
- ✅ Returning to the shopping (inventory) page
- ✅ Checking login with invalid username or password

## 🛠️ Tech Stack

- **Python 3.10+**
- **Selenium WebDriver**
- **Pytest**
- **POM (Page Object Model)**

## ▶️ How to Run the Tests

### 1. Clone the repository

```bash
git clone https://github.com/Vincned/autotest_shop.git
cd autotest_shop
````

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the test

```bash
pytest tests/test_add_to_cart.py
```

## 🔐 Test Data

* URL: [https://www.saucedemo.com/](https://www.saucedemo.com/)
* Username: `standard_user`
* Password: `secret_sauce`

## 📌 Future Ideas

* ⏳ Add negative scenarios for checkout
* 🧪 Generate HTML or Allure test reports
* 🔄 Integrate with GitHub Actions for CI
* 🧼 Add teardown logic to reset state if needed

---

🧑‍💻 Author: [Jack Mur](https://github.com/Vincned)
📅 Project start: 2025
🔖 License: MIT (if applicable)

```