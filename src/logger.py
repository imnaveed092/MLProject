import logging
import datetime
import os

log_dir="logging_files"
current_time_stamp = datetime.datetime.now().strftime('%Y-%m-%h')
log_file = f'{current_time_stamp}.log'
log_file_path = os.path.join(os.getcwd(),log_file)
log_path = os.makedirs(log_dir,exist_ok=True)



logging.basicConfig(
    filename=log_file_path,
    filemode='w',
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s" ,
    level=logging.INFO ,
)

logging.info('log file created')