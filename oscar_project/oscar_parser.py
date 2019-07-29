import re
import subprocess
import string


class OscarParser:

    def __init__(self):
        pass

    def get_id(self):
        slurm_log = open('SRS4807080_SRX5884550_1_slurm.out', 'r')
        slurm_data = slurm_log.read()

        pattern = re.compile('\s+ Job ID : \d+')
        rx_id = re.findall(pattern, slurm_data)

        temp = str(rx_id)
        all_chars = string.maketrans('', '')
        just_digits = all_chars.translate(all_chars, string.digits)
        self.job_id = temp.translate(all_chars, just_digits)

        print self.job_id

        return self.job_id

    def parser(self):
        subprocess.call('sacct', '-l', '-j', self.job_id, shell=True)


parsed_data = OscarParser()
parsed_data.get_id()
