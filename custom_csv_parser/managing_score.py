def calculating_average(lines):
    average = 0
    for index,values in enumerate(lines):
        average += int(lines[index]['score'])
    return int(average/len(lines))
def finding_top_scorer(lines):
    top_scorer = 0
    for index,values in enumerate(lines):
        current_score =int(lines[index]['score'])
        if top_scorer < current_score:
            top_scorer = current_score
    return top_scorer
def filtering_score(lines):
    filtered_score = []
    for index, values in enumerate(lines):
        current_score = int(lines[index]['score'])
        if current_score > 85:
            filtered_score.append(current_score)
    return filtered_score