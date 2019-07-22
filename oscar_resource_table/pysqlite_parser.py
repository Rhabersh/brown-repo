import re
import pandas as pd

rx_dict = {
    'Job ID': re.compile(r'Job ID = (?P<job_ID>.*)\n'),
    'CPUs': re.compile(r'CPUs = (?P<cpus>\d+)\n'),
    'Memory': re.compile(r'Mem/CPU = (?P<memory>\d+)\n'),
    'Time': re.compile(r'Started = (?P<time>\d+)\n'),
           }


def line_parser(line):
    """
        This function will search each line in the target file(s) and
        search for the regex's specified in rx_dict

        :param line: The line of the file that will be searched for regex matches.
        :return None:
    """
    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match

    return None, None


def file_parser(file_name):
    """
        This function will parse the file(s) with help from the line_parser function,
        it will then store those matches in a dictionary that will be used to
        create a data-frame.

        :param file_name: The file(s) to be parsed
        :return slurm_data: The completed data-frame
    """
    slurm_data = []

    with open(file_name, 'r') as file_object:
        line = file_object.readline()
        while line:

            key, match = line_parser(line)

            if key == 'Job ID':
                job_id = match.group('job_ID')

            if key == 'CPUs':
                cpus = match.group('cpus')
                cpus = int(cpus)

            if key == 'Memory':

                value_type = match.group('memory')
                line = file_object.readline()

                while line.strip():
                    number, value = line.strip().split(',')
                    value = value.strip()

                    row = {
                        'Job ID': job_id,
                        'CPUs': cpus,
                        'Memory': number,
                        value_type: value
                    }

                    slurm_data.append(row)
                    line = file_object.readline()

            line = file_object.readline()

        slurm_data = pd.DataFrame(slurm_data)

        if 'Job ID' in slurm_data:
            print 'The key exists'
        else:
            print 'The key does not exist'

        slurm_data.set_index(['Job ID', 'CPUs', 'Memory'], inplace=True)

        slurm_data = slurm_data.groupby(level=slurm_data.index.names).first()

        slurm_data = slurm_data.apply(pd.to_numeric, errors='ignore')
    return slurm_data


if __name__ == '__main__':
    print file_parser('SRS4807080_SRX5884550_1_slurm.out')
