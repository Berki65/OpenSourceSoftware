"""
Assignment from Berkay Bentetik - 24170078
Python Lab 02 - Midterm and Final Exam Analysis
"""

import csv

def read_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = []
        next(reader)  # Skips the header row otherwise error occurs
        for row in reader:
            midterm_score = int(row[0])
            final_score = int(row[1])
            data.append((midterm_score, final_score))
    return data

def calc_weighted_average(data_2d, weight):
    average = []
    for scores in data_2d:
        average.append(sum([s * w for s, w in zip(scores, weight)]))
    return average

def analyze_data(data_1d):
    # Note) Please don't use NumPy and other libraries. Do it yourself.
    n = len(data_1d)
    mean = sum(data_1d) / n
    var = sum((x - mean) ** 2 for x in data_1d) / n
    median = sorted(data_1d)[n // 2] if n % 2 == 1 else (sorted(data_1d)[n // 2 - 1] + sorted(data_1d)[n // 2]) / 2
    return mean, var, median, min(data_1d), max(data_1d)


if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        average = calc_weighted_average(data, [40/125, 60/100])

        # Write the analysis report as a markdown file
        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Average |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final'  : [f_score for _, f_score in data],
                'Average': average }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')