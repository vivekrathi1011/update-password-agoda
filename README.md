# Password Update
A password change function, which runs through the given validation and then compares with the old password.
If all the validation pass and password is not similar to old password < 80% match, then it returns true else false {mock}. 


###Function 
```
change_password( old_passwd, new_passwd )
```
#####Password requirement
1. At least 18 alphanumeric characters and list of special chars !@#$&amp;*
2. At least 1 Upper case, 1 lower case ,least 1 numeric, 1 special character
3. No duplicate repeat characters more than 4
4. No more than 4 special characters
5. 50 % of password should not be a number


#####Change password requirement
1. Old password should match with system
2. New password should be a valid password
3. password is not similar to old password &lt; 80% match.
#####Project Structure
```
├── README.md
├── app.py
├── config
│   ├── old_passwd.txt
│   └── rules.yaml
├── logging_config.ini
├── password_update
│   ├── __init__.py
│   ├── password_validation_utils
│   │   ├── __init__.py
│   │   └── validation.py
│   └── similar_check
│       ├── __init__.py
│       └── check_similarity_oldpassword.py
├── requirements.txt
└── tests
    ├── test_app.py
    ├── test_data
    │   ├── test_data_app.yaml
    │   ├── test_data_password_validation_utils.yaml
    │   └── test_data_similar_check.yaml
    ├── test_password_validation_utils
    │   ├── __init__.py
    │   ├── test_check_allowed_special_chars.py
    │   ├── test_check_case_alphabet.py
    │   ├── test_check_case_integer.py
    │   ├── test_check_percentage_on_number.py
    │   ├── test_check_repeats.py
    │   ├── test_check_special_char.py
    │   ├── test_check_special_char_count.py
    │   └── test_length_check.py
    └── test_similar_check
        ├── __init__.py
        └── test_similar.py
```
###How To Use This
    1.git pull "Password Update"
    2.Run pip install -r requirements.txt to install dependencies
    3.Run python app.py
    4.Enter New Passsword :<enter new password>
    
    
`    Note: old password store in 'config/old_passwd.txt' 
`

###Testing
#### Test Report: 



```
Test Data :
     |── tests/test_data : Please refer project structure.
Test Cases :
     │── tests/test_password_validation_utils
     |── test_app.py
     └── test_similar_check


To execute and generate a complete test case execution report in html format.
Run:
        $ python -m pytest --html=report.html
        
Open Html Report : 
  <system_path>/updatePassword/report.html
Console:       
======================================================================================================== test session starts ============================================================
collected 31 items                                                                                                                                                                                                                   

tests/test_app.py .............                                                        [ 41%]
tests/test_password_validation_utils/test_check_allowed_special_chars.py ..            [ 48%]
tests/test_password_validation_utils/test_check_case_alphabet.py ..                    [ 54%]
tests/test_password_validation_utils/test_check_case_integer.py ..                     [ 61%]
tests/test_password_validation_utils/test_check_percentage_on_number.py ..             [ 67%]
tests/test_password_validation_utils/test_check_repeats.py ..                          [ 74%]
tests/test_password_validation_utils/test_check_special_char.py ..                     [ 80%]
tests/test_password_validation_utils/test_check_special_char_count.py ..               [ 87%]
tests/test_password_validation_utils/test_length_check.py ..                           [ 93%]
tests/test_similar_check/test_similar.py ..                                            [100%]

------ generated html file: file:///<project-path>/updatePassword/report.html ---------------
========================== 31 passed in 0.33 seconds ======================================== 
```

### Code Coverage Report: 
```
TO generate code coverage report:
Run:
        $ coverage run --source . -m py.test
        $ coverage report 

Name                                                                       Stmts   Miss  Cover
----------------------------------------------------------------------------------------------
app.py                                                                        35      3    91%
password_update/__init__.py                                                    0      0   100%
password_update/password_validation_utils/__init__.py                          0      0   100%
password_update/password_validation_utils/validation.py                       53      0   100%
password_update/similar_check/__init__.py                                      0      0   100%
password_update/similar_check/check_similarity_oldpassword.py                  9      0   100%
tests/test_app.py                                                             31      0   100%
tests/test_password_validation_utils/__init__.py                               0      0   100%
tests/test_password_validation_utils/test_check_allowed_special_chars.py       9      0   100%
tests/test_password_validation_utils/test_check_case_alphabet.py               9      0   100%
tests/test_password_validation_utils/test_check_case_integer.py                9      0   100%
tests/test_password_validation_utils/test_check_percentage_on_number.py        9      0   100%
tests/test_password_validation_utils/test_check_repeats.py                     9      0   100%
tests/test_password_validation_utils/test_check_special_char.py                9      0   100%
tests/test_password_validation_utils/test_check_special_char_count.py          9      0   100%
tests/test_password_validation_utils/test_length_check.py                      9      0   100%
tests/test_similar_check/__init__.py                                           0      0   100%
tests/test_similar_check/test_similar.py                                       9      0   100%
----------------------------------------------------------------------------------------------
TOTAL                                                                        209      3    99%

```