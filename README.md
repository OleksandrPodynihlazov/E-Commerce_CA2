# Automated Irrigation Systems E-Shopping Website (CA2)
## Team Members:
- [Oleksandr Podynihlazov (X00215403)](https://github.com/OleksandrPodynihlazov)
- [Dmytro Zuba (X00225759)](https://github.com/dmytrozubal)

## Website URL:
- [Automated Irrigation Systems E-Shopping Website](exclmark.pythonanywhere.com)

## Test Data:
| Username | Password | Role  | email |
|:--------:|:--------:|:-----:|:-----:|
| admin    | admin    | SuperUser | - |
| user     | TestUserAccount     | Customer  | user@example.com |

| Card Number | Date | CVV |
|:-----------:|:----:|:---:|
| 4242 4242 4242 4242 | 02/42 | 242 |

| Voucher Code | Discount |
|:------------:|:--------:|
| CA2          | 25%      |


## Assignment Development Breakdown:
- [Oleksandr Podynihlazov](https://github.com/OleksandrPodynihlazov)
  - Data scraping for products
  - Accounts
  - Change and reset password
  - User Profile
  - Support app
  - Vouchers app
  - Orders app

- [Dmytro Zubal](https://github.com/dmytrozubal)
  - Shop app
  - Products database population
  - Search app
  - Cart app
  - Stripe integration
  - Deploy

# Development notes:
### Init:
```bash
python3 -m venv env
source env/bin/activate   # For Linux
env\Scripts\activate      # For Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
```

### Load database:
```bash
python manage.py loaddata data.json
```

### Dump database:
```bash
python manage.py dumpdata --natural-foreign --natural-primary --indent 4 > data.json
```
