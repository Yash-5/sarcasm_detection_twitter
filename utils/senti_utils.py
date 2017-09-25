import subprocess

def runsenti(text, senti_file_path="./", senti_data_path="./SentiLookup/"):
    command_to_run = 'java -jar %sSentiStrengthCom.jar sentidata %s text "%s"' % (senti_file_path, senti_data_path, text)
    senti_output = subprocess.check_output(command_to_run, shell=True)
    return list(map(int, senti_output.split()))
