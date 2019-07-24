import re
import subprocess


class OscarParser:

    def __init__(self, job_id):
        self.job_id = job_id

    def get_id(self):
        slurm_log = open('SRS4807080_SRX5884550_1_slurm.out', 'r')
        rx_id = re.search('\s+ Job ID : \d+', slurm_log)

        print rx_id

        return rx_id


    def parser(self, job_id):
        pass
