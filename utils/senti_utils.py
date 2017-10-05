import subprocess

"""
runsenti takes as input text(string) and returns it's sentiStrength score as a list of size 2

senti_file_path should be set to the path of SentiStrengthCom.jar and senti_data_path 
should be the path to data files required for sentiStrength

refer to http://sentistrength.wlv.ac.uk/ to understand what the sentiStrength scores represent
"""
def runsenti(text, senti_file_path="./", senti_data_path="./SentiLookup/"):
    command_to_run = 'java -jar %s sentidata %s text "%s"' % (senti_file_path, senti_data_path, text)
    senti_output = subprocess.check_output(command_to_run, shell=True)
    return list(map(int, senti_output.split()))
