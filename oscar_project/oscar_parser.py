import re
import subprocess
import string


class OscarParser:

    def __init__(self):
        self.slurm_files = ['SRS4807080_SRX5884550_1_slurm.out', 'SRS4807080_SRX5884550_fastqc_slurm.stdout',
                            'SRS4807080_SRX5884550_gsnap_slurm.stdout',
                            'SRS4807080_SRX5884550_samtools_view_round_2_slurm.stdout',
                            'SRS4807080_SRX5884550_samtools_view_slurm.stdout']

    def get_id(self):
        job_id_list = []
        for i in range(len(self.slurm_files)):
            slurm_data = open(self.slurm_files[i], 'r')

            slurm_log = slurm_data.read()
            pattern = re.compile('\s+ Job ID : \d+')
            rx_id = re.findall(pattern, slurm_log)

            temp = str(rx_id)
            all_chars = string.maketrans('', '')
            just_digits = all_chars.translate(all_chars, string.digits)
            self.job_id = temp.translate(all_chars, just_digits)

            job_id_list.append(self.job_id)

            i = i + 1

        print job_id_list
        return job_id_list

    def parser(self):
        subprocess.call('sacct -u -j self.job_id', shell=True)


parsed_data = OscarParser()
parsed_data.get_id()
# parsed_data.parser()
