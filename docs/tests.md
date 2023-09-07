# Tests

## Prerequisites
- unittest

## Tests scenarios

### Hash

| **ID**         | **Test name** | **Objective**                | **User action expected**                                | **System action expected**                                                                             | **Criteria sucess**          | **Status** |
|-----------------------|--------|------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------|------------|
| 0    | Password with hash  | Password should been hash    | Hash checkbox tick + click on Generated password button | Method generated password executed + hash password method + password showing in the bottom of the page | Password should been hash    | :x: |
| 1 | Password without hash | Password shouldn't been hash | Click on Generated password button | Method generated password executed + password showing in the bottom of the page | Password shouldn't been hash | :x: |


### Length

| **ID**         | **Test name** | **Objective**                | **User action expected**                                | **System action expected**                                                                             | **Criteria sucess**          | **Status** |
|-----------------------|--------|------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------|------------|
| 2    | Password with a size of 0  | Password should be null | Define length to 0 + click on Generated password button | Method generated password executed + password showing in the bottom of the page | Password should been hash    | :x: |
| 3 | Password with a size of 1 | Length of the password should be 1 | Define length to 1 + Click on Generated password button | Method generated password executed + password showing in the bottom of the page | Length of the password should be 1 | :x: |
| 4 | Password with a size of 10 | Length of the password should be 10 | Define length to 10 + Click on Generated password button | Method generated password executed + password showing in the bottom of the page | Length of the password should be 10 | :x: |
### Symbols

| **ID**         | **Test name** | **Objective**                | **User action expected**                                | **System action expected**                                                                             | **Criteria sucess**          | **Status** |
|-----------------------|--------|------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------|------------|
| 5 | Password with symbols | Password should contains symbols | Symbols checkbox tick + click on Generated password button | Method generated password executed + password showing in the bottom of the page | Password should contains symbols | :x: |
| 6 | Password without symbols | Password shouldn't contains symbols | Click on Generated password button | Method generated password executed + password showing in the bottom of the page | Password shouldn't contains symbols | :x: |

### Digits

| **ID**         | **Test name** | **Objective**                | **User action expected**                                | **System action expected**                                                                             | **Criteria sucess**          | **Status** |
|-----------------------|--------|------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------|------------|
| 7    | Password with digits | Password should contains digits | Digits checkbox tick + click on Generated password button | Method generated password executed + password showing in the bottom of the page | Password should been hash    | :x:         |
| 8 | Password without digits | Password shouldn't contains digits | Click on Generated password button | Method generated password executed + password showing in the bottom of the page | Password shouldn't been hash | :x: |
