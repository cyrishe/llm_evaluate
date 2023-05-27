# -*- coding: utf-8 -*-
prompt_input = (
    "Below is an instruction that describes a specific task. "
    "Write a response that appropriately completes the request.\n\n"
    "task type prompt:\n\n{question-type}\n\n"
    "### Instruction:\n\n{instruction}\n\n### Response:\n\n"
)

def generate_prompt(instruction, question_type, input=None):
    prompt = get_prompt(question_type)
    if input:
        instruction = instruction + '\n' + input
    prompt_template = prompt_input.format_map({
        'question-type': prompt,
        'instruction': instruction
    })
    return prompt_template

def get_prompt(question_type):
    if not question_type:
        return ""
    elif question_type == "选择题":
        return "这是一道选择题，直接给出它的答案，不要有任何解释，如果有多个选择，用','把他们分割开，这道题应该选择"
    elif question_type == '判断题':
        return "这是一道判断题，直接回答正确或错误，不要有任何解释，这句话是"
    elif question_type == '枚举题':
        return "这是一道枚举题，写出你认为合理的答案，这道题的答案是"
    else:
        return "这是一道陈述题，你需要根据给出的条件，生成合适的回答，你的回答是"
