// Method which check the strength of a password
export function checkPasswordStrength(password: string) {

    let strengthPassword = 0
    let strengthBadge = document.getElementById('strengthBadge')

    if (/[a-z]+/.test(password)) {
        strengthPassword += 1
    }
    if (/[A-Z]+/.test(password)) {
        strengthPassword += 1
    }
    if (/[0-9]+/.test(password)) {
        strengthPassword += 1
    }
    if (/[^A-Za-z0-9]+/.test(password)) {
        strengthPassword += 1
    }
    if (password.length > 10) {
        strengthPassword += 1
    } else {
        strengthPassword -= 1
    }
    
   
    console.log(strengthPassword)

    if (strengthBadge != null) {
        switch (strengthPassword) {
            case 2:
                strengthBadge.style.backgroundColor = "orange"
                strengthBadge.textContent = 'Medium'
                break;
            case 3:
                strengthBadge.style.backgroundColor = "lightgreen"
                strengthBadge.textContent = 'Strong'
                break;
            case 4: case 5:
                strengthBadge.style.backgroundColor = "green"
                strengthBadge.textContent = 'Very Strong'
                break;
            default:
                strengthBadge.style.backgroundColor = "red"
                strengthBadge.textContent = 'Weak'
                break;
        }
    }
}

