import argparse
from reading_csv_file import read_csv_file
from managing_score import calculating_average
from managing_score import finding_top_scorer
from managing_score import filtering_score
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    log_file_path = args.file_path
    lines = read_csv_file(log_file_path)
    if not lines:
        return
    average_score= calculating_average(lines)
    print(average_score)
    top_scorer = finding_top_scorer(lines)
    print(top_scorer)
    filtered_score = filtering_score(lines)
    print(filtered_score)

main()