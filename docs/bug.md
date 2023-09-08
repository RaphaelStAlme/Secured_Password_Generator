# Bug

This file is dedicated to list bugs encountered and solutions found
 
## 1. Bug: `TypeError: NetworkError when attempting to fetch resource.'`

We try to call API with this function:

```javascript

async updateTutorial() {
    const requestOptions = {
        method: "GET",
        mode: "no-cors",
        headers: { "Content-Type": "application/json" },
    } 

    await fetch(`http://127.0.0.1:5000/generate_password?digits=${digits}&symbols=${symbols}&length=${length}&hash=${hash}`, requestOptions);
   }
```

And this error is raised:

```bash
TypeError: NetworkError when attempting to fetch resource.
```

### Reason

The reason is that we try to call API with `mode: "no-cors"`.

And by default with no-cors, nothing is returned in body.

### Solution

We have added library `flask-cors` to our API:

```bash
pip install -U flask-cors
```

And we have added this line in our API:

```python
from flask_cors import CORS

CORS(app)
```

In javascript project, we have removed `mode: "no-cors"`:
    
```javascript
async updateTutorial() {
    const requestOptions = {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    } 
    
    await fetch(`http://127.0.0.1:5000/generate_password?digits=${digits}&symbols=${symbols}&length=${length}&hash=${hash}`, requestOptions);
}
```


And the issue is fixed.

## 2. Bug: `SyntaxError: JSON.parse: unexpected character at line 1 column 20 of the JSON data`

We try to call API with this function after to give instruction in order to generate password:

```javascript

static async generatePassword(digits: boolean, symbols: boolean, length: string | null, hash: boolean) {
        console.log(length);
        var response = await fetch(`http://127.0.0.1:5000/generate_password?digits=${digits}&symbols=${symbols}&length=${length}&hash=${hash}`);
        return response.json();
    }

```

And this error is raised:

```bash
SyntaxError: JSON.parse: unexpected character at line 1 column 20 of the JSON data
```

### Reason

The reason is that we try to parse a string in JSON format which contains special char like `'`, `"`, `,`, `{` or `}`.
And the generated password on the back-end side was in simple format like this:

```python
return '{ "password" : ' + '"' + password + '" }' 
```

That means if password contains same character which compose json format, it will raise an error. 

Example:
```bash
password = "test"@,rkeorkezk{'ejejrzjijetioj"
```

Because json understand that password is finished at the first `"`, and the rest is not in json format. 

### Solution

We have used jsonify function from flask library to return json format even if password contains special char which compose json format:

```python
jsonify({ "password" : password})
```

And the issue is fixed.

## 3. Bug: `TypeError: NetworkError when attempting to fetch resource.` with password length which contains character.

We try to call API with this function after to give instruction in order to generate password:

```javascript
static async generatePassword(digits: boolean, symbols: boolean, length: string | null, hash: boolean) {
        console.log(length);
        var response = await fetch(`http://127.0.0.1:5000/generate_password?digits=${digits}&symbols=${symbols}&length=${length}&hash=${hash}`);
        return response.json();
    }
```

And this error is raised if you give a password length which contains character like `A`:

```bash
TypeError: NetworkError when attempting to fetch resource.
```

### Reason

The reason is that we try to call API with a password length which contains character like `A`. And javascript code doesn't verify correctly if password length contains only number.

### Solution

We have added a verification in javascript code to check if password length contains only number:

```javascript
if (passwordLength.value.length != 0 && /[a-zA-Z]+/.test(passwordLength.value)) {
	alert("Password length must be a number");
}
```

And the issue is fixed.

## 4. Bug: `Localhost cannot be reached` with Safari.

When trying to call the front page of our application

```javascript
driver.get("http://localhost:4321")
```

And this this error is raised:

```bash
TypeError: Safari cannot reached localhost
```

## 5. Bug: Default length password doesn't display in front

When we tried to generate a password whithout a length the password don't show up

### Reason
The input where the length is define was not set at all.

### Solution

This was fixed by changing the type of the input by "number" instead of "text" and set the value to 8 by default.








