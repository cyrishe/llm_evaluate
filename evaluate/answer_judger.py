def judge_selection(std_answer, model_answer):
    """
    :param std_answer: 可能是 [A, A、B、C, A|reason, B|reason1|C|reason2...]
    :type std_answer:
    :param model_answer:
    :type model_answer:
    :return:
    :rtype:
    """
    # A、B、C
    if "," in std_answer:
        cnt, total = 0, 0
        for item in std_answer.split(","):
            total += 1
            if item.strip() in model_answer:
                cnt += 1
        return 10 * (cnt / total)
    # A|reason1|B|reason2
    elif "|" in std_answer:
        cnt, total = 0, 0
        std_answer_list = std_answer.split("|")
        for i in range(0, len(std_answer_list), 2):
            total += 1
            if std_answer_list[i] in model_answer or std_answer_list[i + 1] in model_answer:
                cnt += 1
        return 10 * (cnt / total)
    # A
    else:
        if std_answer.strip() in model_answer:
            return 10
        else:
            return 0


def judge_true_false(std_answer, model_answer):
    false_set = ["不对", "不正确", "不合理", "不合适", "错", "不是的", "incorrect", "wrong", "false", "negative", "no"]
    true_set = ["对", "正确", "合理", "合适", "不错", "是的", "correct", "yes", "true", "positive"]

    for item in false_set:
        if item in std_answer:
            std_answer = "错"
        if item in model_answer:
            model_answer = "错"
    if std_answer != "错":
        for item in true_set:
            if item in std_answer:
                std_answer = "对"
    if model_answer != "错":
        for item in true_set:
            if item in model_answer:
                model_answer = "对"
    return 0 if std_answer != model_answer else 10


def judge_list(std_answer, model_answer):
    cnt = 0
    std_answer = std_answer.split(", ")
    for item in std_answer:
        if item.strip() in model_answer:
            cnt += 1
    score = 10 * cnt / len(std_answer)
    return score


def judge_execute(std_answer, model_answer):
    return 0


def judge_default(std_answer, model_answer):
    # 称述题，用最长公共子序列表示他们的相似度
    m, n = len(std_answer), len(model_answer)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if std_answer[i - 1] == model_answer[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    score = 10 * dp[m][n] / m
    return score


def answer_judger(std_answer, model_answer, question_type):
    if not std_answer or not question_type:
        print(f'empty std_answer \n')
        return -1
    if question_type == '选择题':
        score = judge_selection(std_answer, model_answer)

    elif question_type == '判断题':
        score = judge_true_false(std_answer, model_answer)

    elif question_type == '枚举题':
        score = judge_list(std_answer, model_answer)

    elif question_type == '执行题':
        score = judge_execute(std_answer, model_answer)
    else:
        score = judge_default(std_answer, model_answer)
    return score


if __name__ == "__main__":
    str1 = 'C|交通工具'
    str2 = '答案。'
    score = judge_selection(str1, str2)
    print(score)
