# Contents of this repository

You are on the **`html+css`** branch of this repository. It contains example code from the "[Introduction to HTML and CSS](https://hwrberlin.github.io/fswd/09-html-css.html)" session.

## Steps to execute the example code

**Step 1:** set up and activate a [Python Virtual Environment](https://hwrberlin.github.io/fswd/01-python-vscode.html#32-use-the-python-virtual-environment-as-default-for-this-workspace).

**Step 2:** install the required Python packages from the terminal with the command `pip install -r requirements.txt`:

```shell
(venv) C:\Users\me\projects\webapp> pip install -r requirements.txt
```

> I created the file `📄requirements.txt` with this command: `pip freeze > requirements.txt`

**Step 3:** initialize the app's SQLite database via `flask init-db`:

```shell
(venv) PS C:\Users\me\projects\webapp> flask init-db
Database has been initialized.
```

**Step 4:** start the web server via `flask run --reload`:

```shell
(venv) PS C:\Users\me\projects\webapp> flask run --reload
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
```

**Step 5:** visit [http://127.0.0.1:5000/insert/sample](http://127.0.0.1:5000/insert/sample) to populate the app's database with some sample data.

**Step 6:** visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the landing page.

**Step 7:** visit the following pages to display the examples of this session:

+ [http://127.0.0.1:5000/faq/](http://127.0.0.1:5000/faq/): FAQ page styled with CSS
+ [http://127.0.0.1:5000/faq/alt](http://127.0.0.1:5000/faq/alt): FAQ page with alternative color palette
+ [http://127.0.0.1:5000/faq/none](http://127.0.0.1:5000/faq/none): FAQ page without CSS
+ [http://127.0.0.1:5000/ex/](http://127.0.0.1:5000/ex/): CSS "Hello, World" example
+ [http://127.0.0.1:5000/ex/2](http://127.0.0.1:5000/ex/2): CSS "layout grid" example
