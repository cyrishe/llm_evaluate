CUDA_VISIBLE_DEVICES=0,1 python c_llama.py \
    --base_model ../../Chinese_llama/models/llama-7b-hf \
    --lora_model ../../Chinese_llama/models/chinese-alpaca-lora-7b \
    --data_file std_questions \
    --with_prompt
