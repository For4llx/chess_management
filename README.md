# Execute the following step to make the script work:

1. Create your virtual environnement by executing the command:

```
python -m venv env
```

2. Activate your virtual environnement by executing the command:

```
source env/bin/activate
```

3. Install all the needed packages by executing the command:

```
pip install -r requirements.txt
```

4. Run the script by executing the command:

```
python3 main.py
```

# Create a flake report:

1. Run the following command:

```
flake8 --format=html --htmldir=flake8_rapport --max-line-length 119
```
