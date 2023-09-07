# Tests

## Prerequisites
- unittest

## Tests scenarios

### Hash

| **Test name**         | **ID** | **Objective**                | **User action expected**                                | **System action expected**                                                                             | **Criteria sucess**          | **Status** |
|-----------------------|--------|------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------|------------|
| Password with hash    | 0      | Password should been hash    | Hash checkbox tick + click on Generated password button | Method generated password executed + hash password method + password showing in the bottom of the page | Password should been hash    | []         |
| Password without hash | 1      | Password shouldn't been hash | Click on Generated password button                      | Method generated password executed + password showing in the bottom of the page                        | Password shouldn't been hash | []         |


### Length

### Symbols

### Digits