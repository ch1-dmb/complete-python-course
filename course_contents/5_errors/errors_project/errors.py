class RuntimeErrorWithCode(Exception):
    def __init__(self, message, code):
        # Exception is a built in error class in python
       
        super().__init__(f'Error code {self.code}: {message}')
        self.code = code #define it by urself
       

#Exception fors not ahve vode attribute by default
err = RuntimeErrorWithCode('An error happened.', 500)
print(err)