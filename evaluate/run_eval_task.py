from data_set_manager import get_data_set
from task_manager import submit_task_info
from eval_manager import eval_runner
# import multiprocessing as mp
import torch.multiprocessing as mp
import time, os


def run_test(eval_models_str, data_set_str, owner, tag):
    models_list = eval_models_str.split(",")
    data_set = get_data_set(data_set_str)

    eval_id = int(time.time() * 1000)
    submit_result = submit_task_info(eval_id, models_list, data_set, owner, tag)
    if submit_result:
        cmd = 'nohup python eval_manager.py ' \
              ' --eval_id %s' \
              ' --model_list %s' \
              ' --data_set %s' \
              ' --owner %s' \
              ' --tag %s' \
              ' &'
        cmd = cmd % (str(eval_id), eval_models_str, data_set_str, owner, tag)
        print(cmd)
        os.system(cmd)


if __name__ == '__main__':
    run_test('glm6B,llama,llama_for_chainv0.1,dvc,minimax,yuan', 'onedata', 'cyris', 'test_1')
#    run_test('glm6B,llama,llama_for_chainv0.1,dvc,minimax,yuan', 'default', 'cyris', 'test_1')
