import sys


def error_message_details(error, error_detail:sys): # type: ignore
    _,_,exec_tb=error_detail.exc_info()
    file_name=exec_tb.tb_frame.f_code.co_filename # type: ignore
    error_message="Error occured in python script name [{0}] line mumber [{1}] error message[{2}]".format(file_name,exec_tb.tb_lineno,str(error)) # type: ignore

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): # type: ignore
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


